"""Nodes for SQL processing pipeline."""

import logging
from typing import Dict, Any, List, TypedDict, Annotated
import json
import subprocess
import platform
import operator
from datetime import datetime
from crewai import Agent, Task, Crew, Process
from langgraph.graph import StateGraph, END
from sql_bigbrother.pipelines.sql_processing.services.database import DatabaseManager
from sql_bigbrother.pipelines.sql_processing.services.utils import filterSchema, filterSchema_v2, markdownSQL, extractMarkdown, process_data
from sql_bigbrother.pipelines.sql_processing.prompts.agents import SQLAgents
from sql_bigbrother.pipelines.sql_processing.prompts.tasks import SQLTasks

logger = logging.getLogger(__name__)


def initialize_schema_processing(schema_content: str) -> Dict[str, Any]:
    """Initialize chat by processing uploaded SQL schema.
    
    Args:
        schema_content: Raw SQL schema content
        
    Returns:
        Dictionary containing title, recommendations, and schema content
    """
    try:
        agents = SQLAgents()
        tasks = SQLTasks()
        
        filtered_schema = filterSchema_v2(schema_content)
        
        title_agent = agents.sql_title_agent()
        title_task = tasks.sql_title_task(title_agent, filtered_schema)

        recommended_agent = agents.sql_recommended_agent()
        recommended_task = tasks.sql_recommended_task(recommended_agent, filtered_schema)
        
        crew = Crew(
                agents=[title_agent, recommended_agent],
                tasks=[title_task, recommended_task],
                verbose=True,
            )
        crew.kickoff()
        
        title = title_task.output.raw
        recommends_raw = recommended_task.output.raw
        
        # Extract JSON from markdown code block if present
        try:
            if recommends_raw.strip().startswith('```'):
                # Find JSON content between code block markers
                start_idx = recommends_raw.find('[')
                end_idx = recommends_raw.rfind(']') + 1
                if start_idx != -1 and end_idx != 0:
                    recommends_json = recommends_raw[start_idx:end_idx]
                else:
                    recommends_json = recommends_raw
            else:
                recommends_json = recommends_raw
                
            recommends = json.loads(recommends_json)
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse recommends as JSON: {e}, using raw output")
            # Fallback to empty list if JSON parsing fails
            recommends = []
        
        return {
            'title': title, 
            'recommends': recommends, 
            'sql_content': schema_content
        }
    except Exception as e:
        logger.error(f"Schema processing error: {str(e)}")
        raise


def process_sql_query(requirement: str, schema: str, model: str, is_explain: bool = False, chat_history: List[Dict[str, str]] = None, execute_query: bool = False) -> Dict[str, Any]:
    """Process SQL query request using AI agents with conversation context.
    
    Args:
        requirement: User's query requirement
        schema: SQL schema
        model: AI model to use
        is_explain: Whether to include explanation
        chat_history: Previous conversation messages for context
        execute_query: Whether to execute the query (False by default, only generates SQL)
        
    Returns:
        Dictionary containing query, explanation, rows, and columns
    """
    try:
        agents = SQLAgents()
        tasks = SQLTasks()
        database = DatabaseManager("mysql")
        
        filtered_schema = filterSchema_v2(schema)
        
        # Step 1: Use coordinator to classify the question type
        coordinator = agents.conversation_coordinator_agent(model)
        coordinator_task = tasks.conversation_coordinator_task(
            coordinator, 
            requirement, 
            filtered_schema,
            chat_history or []
        )
        
        # Run coordinator to determine intent
        coordinator_crew = Crew(
            agents=[coordinator],
            tasks=[coordinator_task],
            verbose=True,
            process=Process.sequential
        )
        coordinator_crew.kickoff()
        
        coordinator_response = coordinator_task.output.raw
        
        # Check if this is a conversational question (greetings, schema questions, etc.)
        conversational_keywords = ['hello', 'hi', 'help', 'what can you', 'how does this work', 'explain', 'what tables', 'what is', 'tell me about']
        is_conversational = any(keyword in requirement.lower() for keyword in conversational_keywords) and 'NEEDS_SQL_QUERY' not in coordinator_response
        
        if is_conversational or ('NEEDS_SQL_QUERY' not in coordinator_response and not any(word in requirement.lower() for word in ['show', 'get', 'find', 'list', 'count', 'how many', 'total', 'sum', 'average'])):
            # Direct conversational response - no SQL needed
            return {
                'query': '',
                'explain': f"💬 {coordinator_response}",
                'rows': [],
                'columns': [],
                'conversational_response': True
            }
        
        # Step 2: SQL query needed - Build context from chat history
        context = ""
        if chat_history and len(chat_history) > 0:
            context = "\n\nPrevious conversation:\n"
            for msg in chat_history[-5:]:
                role = msg.get("role", "user")
                content = msg.get("content", "")[:200]
                context += f"{role.upper()}: {content}\n"
            context += "\nCurrent question:\n"
        
        contextualized_requirement = context + requirement if context else requirement
        
        query_output = ""
        explain_output = ""
        
        if is_explain:
            specialist = agents.sql_specialist_agent(model)
            expert = agents.sql_expert_agent(model)
            agent_list = [specialist, expert]

            design_task = tasks.sql_design_task(specialist, contextualized_requirement, filtered_schema)  
            analyze_task = tasks.sql_expert_task(expert, design_task)
            task_list = [design_task, analyze_task]

            crew = Crew(agents=agent_list, tasks=task_list, verbose=True, process=Process.sequential)       
            crew.kickoff()
            
            query_output = extractMarkdown(design_task.output.raw) 
            explain_output = analyze_task.output.raw
        else:
            specialist = agents.sql_specialist_agent(model)
            design_task = tasks.sql_design_task(specialist, contextualized_requirement, filtered_schema)

            crew = Crew(agents=[specialist], tasks=[design_task], verbose=True)
            crew.kickoff()

            query_output = extractMarkdown(design_task.output.raw)
        
        # Step 3: Execute the query ONLY if explicitly requested
        if execute_query:
            try:
                setup_success = database.setup(schema)
                if setup_success:
                    metadata = database.execute(query_output)
                    query = markdownSQL(query_output)
                    
                    return {
                        'query': query, 
                        'explain': explain_output, 
                        'rows': process_data(metadata['rows']), 
                        'columns': metadata['columns'],
                        'executed': True
                    }
            except Exception as db_error:
                logger.warning(f"Database execution failed: {str(db_error)}")
                query = markdownSQL(query_output)
                return {
                    'query': query, 
                    'explain': explain_output, 
                    'rows': [], 
                    'columns': [],
                    'error': f'Execution failed: {str(db_error)}',
                    'executed': False
                }
        
        # Return generated query without execution
        query = markdownSQL(query_output)
        return {
            'query': query, 
            'explain': explain_output + '\n\n💡 Query generated successfully.', 
            'rows': [], 
            'columns': [],
            'executed': False,
            'note': 'Query generated successfully.'
        }
            
    except Exception as e:
        logger.error(f"SQL query processing error: {str(e)}")
        raise


class DatabaseDiscoveryState(TypedDict):
    """State for database discovery agent."""
    os_type: str
    discovered_databases: Annotated[list, operator.add]
    commands_executed: Annotated[list, operator.add]
    current_db_type: str
    raw_output: str
    error_message: str


def check_os(state: DatabaseDiscoveryState) -> DatabaseDiscoveryState:
    """Detect the operating system."""
    os_type = platform.system().lower()
    return {
        **state,
        "os_type": os_type,
        "discovered_databases": [],
        "commands_executed": []
    }


def discover_postgres(state: DatabaseDiscoveryState) -> DatabaseDiscoveryState:
    """Discover PostgreSQL databases."""
    commands = []
    if state["os_type"] == "darwin":  # macOS
        commands = ["psql --version", "pg_isready"]
    elif state["os_type"] == "linux":
        commands = ["psql --version", "systemctl status postgresql"]
    elif state["os_type"] == "windows":
        commands = ["psql --version"]
    
    databases = []
    executed = []
    
    # Check if PostgreSQL is available
    for cmd in commands:
        try:
            result = subprocess.run(
                cmd.split(), 
                capture_output=True, 
                text=True, 
                timeout=5
            )
            executed.append(f"{cmd}: SUCCESS")
            if result.returncode == 0:
                # Try to connect and list databases
                try:
                    import psycopg2
                    # Try to connect with common default credentials
                    connection_attempts = [
                        {"host": "localhost", "user": "postgres", "password": ""},
                        {"host": "localhost", "user": "postgres", "password": "postgres"},
                    ]
                    
                    for conn_params in connection_attempts:
                        try:
                            conn = psycopg2.connect(**conn_params, database="postgres", port=5432)
                            cursor = conn.cursor()
                            cursor.execute("""
                                SELECT datname FROM pg_database 
                                WHERE datistemplate = false 
                                AND datname NOT IN ('postgres')
                            """)
                            db_list = cursor.fetchall()
                            
                            for (db_name,) in db_list:
                                databases.append({
                                    "type": "postgresql",
                                    "database": db_name,
                                    "name": db_name,
                                    "host": conn_params["host"],
                                    "status": "accessible"
                                })
                            
                            cursor.close()
                            conn.close()
                            executed.append(f"Listed {len(db_list)} PostgreSQL databases")
                            break  # Successfully connected
                        except Exception as conn_error:
                            executed.append(f"Connection attempt failed: {str(conn_error)[:50]}")
                            continue
                    
                    if not databases:
                        # If we can't connect, at least report PostgreSQL is available
                        databases.append({
                            "type": "postgresql",
                            "database": "postgres",
                            "name": "PostgreSQL Server",
                            "status": "available",
                            "note": "Unable to list databases - connection failed"
                        })
                        
                except ImportError:
                    executed.append("psycopg2 not installed")
                    databases.append({
                        "type": "postgresql",
                        "status": "available",
                        "note": "psycopg2 library required to list databases"
                    })
                break
        except Exception as e:
            executed.append(f"{cmd}: FAILED - {str(e)}")
    
    return {
        **state,
        "discovered_databases": state["discovered_databases"] + databases,
        "commands_executed": state["commands_executed"] + executed,
        "current_db_type": "postgresql"
    }


def discover_mysql(state: DatabaseDiscoveryState) -> DatabaseDiscoveryState:
    """Discover MySQL databases."""
    databases = []
    executed = []
    
    # First check if MySQL is available
    try:
        result = subprocess.run(
            ["mysql", "--version"], 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        executed.append(f"mysql --version: SUCCESS")
        
        if result.returncode == 0:
            # Try to connect and list databases
            try:
                import pymysql
                # Try to connect with common default credentials
                connection_attempts = [
                    {"host": "localhost", "user": "root", "password": ""},
                    {"host": "localhost", "user": "root", "password": "root"},
                ]
                
                for conn_params in connection_attempts:
                    try:
                        conn = pymysql.connect(**conn_params, port=3306)
                        cursor = conn.cursor()
                        cursor.execute("SHOW DATABASES")
                        db_list = cursor.fetchall()
                        
                        # Filter out system databases
                        system_dbs = ['information_schema', 'mysql', 'performance_schema', 'sys']
                        user_databases = [db[0] for db in db_list if db[0] not in system_dbs]
                        
                        for db_name in user_databases:
                            databases.append({
                                "type": "mysql",
                                "database": db_name,
                                "name": db_name,
                                "host": conn_params["host"],
                                "status": "accessible"
                            })
                        
                        cursor.close()
                        conn.close()
                        executed.append(f"Listed {len(user_databases)} MySQL databases")
                        break  # Successfully connected
                    except Exception as conn_error:
                        executed.append(f"Connection attempt failed: {str(conn_error)[:50]}")
                        continue
                
                if not databases:
                    # If we can't connect, at least report MySQL is available
                    databases.append({
                        "type": "mysql",
                        "database": "mysql",
                        "name": "MySQL Server",
                        "status": "available",
                        "note": "Unable to list databases - connection failed"
                    })
                    
            except ImportError:
                executed.append("pymysql not installed")
                databases.append({
                    "type": "mysql",
                    "status": "available",
                    "note": "pymysql library required to list databases"
                })
                
    except Exception as e:
        executed.append(f"mysql --version: FAILED - {str(e)}")
    
    return {
        **state,
        "discovered_databases": state["discovered_databases"] + databases,
        "commands_executed": state["commands_executed"] + executed,
        "current_db_type": "mysql"
    }


def discover_sqlite(state: DatabaseDiscoveryState) -> DatabaseDiscoveryState:
    """Discover SQLite databases."""
    import os
    import glob
    
    databases = []
    executed = []
    
    # System/internal database patterns to exclude
    excluded_patterns = [
        'cloudkit', 'icloud', 'notes', 'calendar', 'contacts', 'mail',
        'cache', 'cookies', 'history', '.apple', 'system', 'library',
        'webkit', 'safari', 'chrome', 'firefox', 'slack', 'zoom'
    ]
    
    # Check for SQLite installation
    try:
        result = subprocess.run(
            ["sqlite3", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        executed.append("sqlite3 --version: SUCCESS")
        
        # Look for .db and .sqlite files in common locations
        search_paths = [
            os.path.expanduser("~"),
            "/tmp",
            "/var/lib"
        ]
        
        for path in search_paths:
            try:
                db_files = glob.glob(f"{path}/**/*.db", recursive=True)
                db_files += glob.glob(f"{path}/**/*.sqlite", recursive=True)
                
                for db_file in db_files[:50]:  # Check more files
                    # Filter out system/internal databases
                    db_lower = db_file.lower()
                    if any(pattern in db_lower for pattern in excluded_patterns):
                        continue
                    
                    databases.append({
                        "type": "sqlite",
                        "status": "available",
                        "path": db_file
                    })
                    
                    if len(databases) >= 10:  # Limit to 10 user databases
                        break
            except:
                pass
                
    except Exception as e:
        executed.append(f"sqlite3 --version: FAILED - {str(e)}")
    
    return {
        **state,
        "discovered_databases": databases,
        "commands_executed": executed,
        "current_db_type": "sqlite"
    }


def summarize_discovery(state: DatabaseDiscoveryState) -> DatabaseDiscoveryState:
    """Summarize all discovered databases."""
    summary = {
        "total_found": len(state["discovered_databases"]),
        "databases_by_type": {},
        "commands_executed": state["commands_executed"]
    }
    
    for db in state["discovered_databases"]:
        db_type = db["type"]
        if db_type not in summary["databases_by_type"]:
            summary["databases_by_type"][db_type] = 0
        summary["databases_by_type"][db_type] += 1
    
    return {
        **state,
        "raw_output": str(summary)
    }


def discover_local_databases(database_config: dict = None) -> Dict[str, Any]:
    """Discover available local databases using an agentic approach.
    
    Args:
        database_config: Optional configuration containing database discovery parameters
        
    Returns:
        Dictionary containing discovered databases and their metadata
    """
    try:
        logger.info("Starting database discovery agent...")
        
        # Create the agent graph
        workflow = StateGraph(DatabaseDiscoveryState)
        
        # Add nodes
        workflow.add_node("check_os", check_os)
        workflow.add_node("discover_postgres", discover_postgres)
        workflow.add_node("discover_mysql", discover_mysql)
        workflow.add_node("discover_sqlite", discover_sqlite)
        workflow.add_node("summarize", summarize_discovery)
        
        # Define the flow
        workflow.set_entry_point("check_os")
        workflow.add_edge("check_os", "discover_postgres")
        workflow.add_edge("discover_postgres", "discover_mysql")
        workflow.add_edge("discover_mysql", "discover_sqlite")
        workflow.add_edge("discover_sqlite", "summarize")
        workflow.add_edge("summarize", END)
        
        # Compile and run
        app = workflow.compile()
        
        initial_state = DatabaseDiscoveryState(
            os_type="",
            discovered_databases=[],
            commands_executed=[],
            current_db_type="",
            raw_output="",
            error_message=""
        )
        
        result = app.invoke(initial_state)
        
        logger.info(f"Database discovery completed: {result['raw_output']}")
        
        return {
            "databases": result["discovered_databases"],
            "os_type": result["os_type"],
            "commands_executed": result["commands_executed"],
            "summary": result["raw_output"],
            "discovery_timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Database discovery error: {str(e)}")
        raise


def extract_schema_from_database(db_type: str, connection_params: Dict[str, Any]) -> str:
    """Extract schema from a discovered database.
    
    Args:
        db_type: Type of database (postgresql, mysql, sqlite)
        connection_params: Connection parameters for the database
        
    Returns:
        SQL schema as a string
    """
    try:
        if db_type == "postgresql":
            return _extract_postgres_schema(connection_params)
        elif db_type == "mysql":
            return _extract_mysql_schema(connection_params)
        elif db_type == "sqlite":
            return _extract_sqlite_schema(connection_params)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
    except Exception as e:
        logger.error(f"Schema extraction error for {db_type}: {str(e)}")
        raise


def _extract_postgres_schema(connection_params: Dict[str, Any]) -> str:
    """Extract schema from PostgreSQL database."""
    try:
        import psycopg2
        
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()
        
        # Get all tables in public schema
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_type = 'BASE TABLE'
        """)
        
        tables = cursor.fetchall()
        schema_sql = []
        
        for (table_name,) in tables:
            # Get CREATE TABLE statement
            cursor.execute(f"""
                SELECT column_name, data_type, character_maximum_length, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_name = '{table_name}'
                ORDER BY ordinal_position
            """)
            
            columns = cursor.fetchall()
            create_stmt = f"CREATE TABLE {table_name} (\n"
            col_defs = []
            
            for col_name, data_type, max_length, nullable, default in columns:
                col_def = f"  {col_name} {data_type}"
                if max_length:
                    col_def += f"({max_length})"
                if nullable == 'NO':
                    col_def += " NOT NULL"
                if default:
                    col_def += f" DEFAULT {default}"
                col_defs.append(col_def)
            
            create_stmt += ",\n".join(col_defs) + "\n);"
            schema_sql.append(create_stmt)
        
        cursor.close()
        conn.close()
        
        return "\n\n".join(schema_sql)
        
    except Exception as e:
        logger.error(f"PostgreSQL schema extraction error: {str(e)}")
        raise


def _extract_mysql_schema(connection_params: Dict[str, Any]) -> str:
    """Extract schema from MySQL database."""
    try:
        import pymysql
        
        conn = pymysql.connect(**connection_params)
        cursor = conn.cursor()
        
        # Get database name
        database = connection_params.get('database', connection_params.get('db'))
        
        # Get all tables
        cursor.execute(f"SHOW TABLES FROM {database}")
        tables = cursor.fetchall()
        
        schema_sql = []
        
        for (table_name,) in tables:
            # Get CREATE TABLE statement
            cursor.execute(f"SHOW CREATE TABLE {database}.{table_name}")
            result = cursor.fetchone()
            if result:
                schema_sql.append(result[1])
        
        cursor.close()
        conn.close()
        
        return "\n\n".join(schema_sql)
        
    except Exception as e:
        logger.error(f"MySQL schema extraction error: {str(e)}")
        raise


def _extract_sqlite_schema(connection_params: Dict[str, Any]) -> str:
    """Extract schema from SQLite database."""
    try:
        import sqlite3
        
        db_path = connection_params.get('database', connection_params.get('path'))
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all CREATE statements
        cursor.execute("""
            SELECT sql FROM sqlite_master 
            WHERE type='table' AND sql IS NOT NULL
            ORDER BY name
        """)
        
        schemas = cursor.fetchall()
        schema_sql = [sql[0] for sql in schemas]
        
        cursor.close()
        conn.close()
        
        return ";\n\n".join(schema_sql) + ";"
        
    except Exception as e:
        logger.error(f"SQLite schema extraction error: {str(e)}")
        raise


def auto_create_schema(discovered_databases: Dict[str, Any], db_index: int = 0) -> Dict[str, Any]:
    """Automatically create schema from a discovered database.
    
    Args:
        discovered_databases: Dictionary containing discovered databases
        db_index: Index of the database to extract schema from
        
    Returns:
        Dictionary containing schema content and metadata
    """
    try:
        databases = discovered_databases.get("databases", [])
        
        if not databases:
            raise ValueError("No databases discovered")
        
        if db_index >= len(databases):
            raise ValueError(f"Invalid database index: {db_index}")
        
        selected_db = databases[db_index]
        db_type = selected_db.get("type")
        
        logger.info(f"Extracting schema from {db_type} database...")
        
        # Prepare connection parameters based on database type
        connection_params = {}
        
        if db_type == "sqlite":
            connection_params = {"path": selected_db.get("path")}
        elif db_type in ["postgresql", "mysql"]:
            # These would need to be provided by user or configuration
            # For now, return a message indicating manual configuration needed
            return {
                "error": f"Automatic schema extraction for {db_type} requires connection parameters",
                "database_type": db_type,
                "database_info": selected_db,
                "requires_manual_config": True
            }
        
        # Extract schema
        schema_content = extract_schema_from_database(db_type, connection_params)
        
        # Process the schema using existing pipeline
        result = initialize_schema_processing(schema_content)
        result["auto_generated"] = True
        result["source_database"] = selected_db
        
        return result
        
    except Exception as e:
        logger.error(f"Auto schema creation error: {str(e)}")
        raise


def generate_introduction(schema_result: Dict[str, Any], discovered_databases: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a welcoming introduction message for the chat session.
    
    Args:
        schema_result: Result from initialize_schema_processing
        discovered_databases: Discovered databases information
        
    Returns:
        Dictionary containing the introduction message and schema information
    """
    try:
        agents = SQLAgents()
        tasks = SQLTasks()
        
        # Prepare detailed database info summary
        db_count = len(discovered_databases.get("databases", []))
        db_types = {}
        databases_detail = []
        
        for db in discovered_databases.get("databases", []):
            db_type = db.get("type", "unknown")
            db_types[db_type] = db_types.get(db_type, 0) + 1
            
            # Build detailed info for each database
            if db_type == "sqlite":
                db_name = db.get("name", "Unknown")
                db_path = db.get("path", "")
                db_size = db.get("size_readable", "Unknown size")
                databases_detail.append(f"  • {db_name} (SQLite) - {db_size}")
                if db_path:
                    databases_detail.append(f"    Path: {db_path}")
            elif db_type == "mysql":
                db_name = db.get("database", "Unknown")
                db_host = db.get("host", "localhost")
                databases_detail.append(f"  • {db_name} (MySQL) at {db_host}")
            elif db_type == "postgresql":
                db_name = db.get("database", "Unknown")
                db_host = db.get("host", "localhost")
                databases_detail.append(f"  • {db_name} (PostgreSQL) at {db_host}")
        
        databases_info = f"""
Discovered {db_count} database(s):
{chr(10).join(databases_detail)}

Summary: {', '.join([f'{count} {dtype}' for dtype, count in db_types.items()])}
"""
        
        # Create introduction agent and task
        intro_agent = agents.sql_introduction_agent()
        intro_task = tasks.sql_introduction_task(
            intro_agent,
            schema_result.get('title', 'Database Schema'),
            schema_result.get('sql_content', ''),
            databases_info
        )
        
        crew = Crew(
            agents=[intro_agent],
            tasks=[intro_task],
            verbose=True
        )
        crew.kickoff()
        
        introduction_message = intro_task.output.raw
        
        # Add a note about schema compatibility
        note = "\n\n📝 **Note**: This schema was auto-loaded from a discovered database. I can generate SQL queries for you and provide insights about your data. Feel free to ask me anything about the schema or request specific queries!"
        
        return {
            **schema_result,
            'introduction': introduction_message + note,
            'auto_initialized': True,
            'discovered_databases': discovered_databases,
            'schema_source_type': discovered_databases.get("databases", [{}])[0].get("type", "unknown") if discovered_databases.get("databases") else "unknown"
        }
        
    except Exception as e:
        logger.error(f"Introduction generation error: {str(e)}")
        # Return with default introduction if AI generation fails
        return {
            **schema_result,
            'introduction': f"Welcome! I've automatically loaded the '{schema_result.get('title', 'database')}' schema. Feel free to ask me questions about the data!",
            'auto_initialized': True,
            'discovered_databases': discovered_databases,
            'schema_source_type': 'sqlite'
        }
