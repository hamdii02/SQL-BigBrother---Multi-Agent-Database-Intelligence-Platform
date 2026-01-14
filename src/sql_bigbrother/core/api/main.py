"""FastAPI integration with Kedro pipelines."""

from fastapi import FastAPI, Form, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project
import logging
from pathlib import Path
import json
from typing import Dict, Any, Optional
from datetime import datetime

# Configure Kedro project
project_path = Path(__file__).parent.parent.parent.parent.parent
configure_project("sql_bigbrother")

logger = logging.getLogger(__name__)

# Global state for discovered databases
discovered_databases: Optional[Dict[str, Any]] = None
initial_chat_state: Optional[Dict[str, Any]] = None
chat_sessions: Dict[str, Dict[str, Any]] = {}  # Store chat sessions by session_id

app = FastAPI(title="SQL BigBrother API", version="1.0.0")

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",  # New frontend port
    "http://localhost:5176", 
    "http://localhost:3000",
    "http://192.168.1.96:5173",  # Network access
    "http://192.168.1.96:5175",  # Network access for new port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class KedroSessionManager:
    """Manage Kedro sessions for API endpoints."""
    
    @staticmethod
    def run_pipeline_node(node_name: str, inputs: Dict[str, Any] = None) -> Dict[str, Any]:
        """Run a specific Kedro node with given inputs."""
        if inputs is None:
            inputs = {}
            
        with KedroSession.create(project_path=project_path) as session:
            try:
                # Run the pipeline
                if node_name == "discover_local_databases_node":
                    from sql_bigbrother.pipelines.sql_processing.nodes import discover_local_databases
                    result = discover_local_databases(inputs.get("database_config"))
                elif node_name == "initialize_schema_processing_node":
                    from sql_bigbrother.pipelines.sql_processing.nodes import initialize_schema_processing
                    result = initialize_schema_processing(inputs.get("schema_content"))
                elif node_name == "process_sql_query_node":
                    from sql_bigbrother.pipelines.sql_processing.nodes import process_sql_query
                    result = process_sql_query(
                        requirement=inputs.get("requirement"),
                        schema=inputs.get("schema"), 
                        model=inputs.get("model"),
                        is_explain=inputs.get("is_explain", False),
                        chat_history=inputs.get("chat_history", []),
                        execute_query=inputs.get("execute_query", False)
                    )
                elif node_name == "auto_create_schema_node":
                    from sql_bigbrother.pipelines.sql_processing.nodes import auto_create_schema
                    result = auto_create_schema(
                        discovered_databases=inputs.get("discovered_databases"),
                        db_index=inputs.get("db_index", 0)
                    )
                else:
                    raise ValueError(f"Unknown node: {node_name}")
                    
                return result
                
            except Exception as e:
                logger.error(f"Error running Kedro node {node_name}: {str(e)}")
                raise HTTPException(status_code=500, detail=str(e))


@app.on_event("startup")
async def startup_event():
    """Run database discovery on startup and auto-initialize chat."""
    global discovered_databases, initial_chat_state
    try:
        logger.info("Starting database discovery...")
        discovered_databases = KedroSessionManager.run_pipeline_node(
            "discover_local_databases_node",
            {}
        )
        logger.info(f"Database discovery completed: {discovered_databases.get('summary')}")
        
        # Auto-initialize chat with first discovered database
        # Prioritize: MySQL > PostgreSQL > SQLite
        databases = discovered_databases.get("databases", [])
        mysql_dbs = [db for db in databases if db.get("type") == "mysql"]
        postgres_dbs = [db for db in databases if db.get("type") == "postgresql"]
        sqlite_dbs = [db for db in databases if db.get("type") == "sqlite"]
        
        target_db = None
        if mysql_dbs:
            target_db = (mysql_dbs[0], "mysql")
            logger.info(f"Found MySQL database, prioritizing for auto-initialization")
        elif postgres_dbs:
            target_db = (postgres_dbs[0], "postgresql")
            logger.info(f"Found PostgreSQL database, prioritizing for auto-initialization")
        elif sqlite_dbs:
            target_db = (sqlite_dbs[0], "sqlite")
            logger.info(f"Found SQLite database for auto-initialization")
        
        if target_db:
            logger.info("Auto-initializing chat with discovered database...")
            try:
                from sql_bigbrother.pipelines.sql_processing.nodes import extract_schema_from_database, initialize_schema_processing, generate_introduction
                
                first_db, db_type = target_db
                
                # Extract schema based on database type
                if db_type == "mysql":
                    # For MySQL, use default connection to ecommerce_db
                    connection_params = {
                        "host": "localhost",
                        "user": "root",
                        "password": "",
                        "database": "ecommerce_db"
                    }
                elif db_type == "sqlite":
                    connection_params = {"path": first_db.get("path")}
                else:
                    connection_params = {}
                
                schema_content = extract_schema_from_database(db_type, connection_params)
                
                # Process schema
                schema_result = initialize_schema_processing(schema_content)
                
                # Generate introduction
                initial_chat_state = generate_introduction(schema_result, discovered_databases)
                
                logger.info(f"Chat auto-initialized with {db_type} database")
            except Exception as e:
                logger.warning(f"Could not auto-initialize chat: {str(e)}")
                initial_chat_state = {
                    "title": "SQL BigBrother",
                    "introduction": "Welcome! I've discovered several databases on your system. You can upload a schema or ask me to analyze a discovered database.",
                    "discovered_databases": discovered_databases
                }
        else:
            logger.info("No SQLite databases found for auto-initialization")
            initial_chat_state = {
                "title": "SQL BigBrother",
                "introduction": f"Welcome! I've discovered {len(databases)} database(s) on your system. Upload a schema file to get started, or provide connection details for PostgreSQL/MySQL databases.",
                "discovered_databases": discovered_databases
            }
            
    except Exception as e:
        logger.error(f"Database discovery failed: {str(e)}")
        discovered_databases = {
            "databases": [],
            "error": str(e),
            "summary": "Discovery failed"
        }
        initial_chat_state = {
            "title": "SQL BigBrother",
            "introduction": "Welcome! Please upload a SQL schema file to get started.",
            "error": str(e)
        }


@app.get('/')
async def root() -> Dict[str, str]:
    """Root endpoint."""
    return {
        "data": 'SQL BigBrother FastAPI with Kedro',
        "databases_discovered": len(discovered_databases.get("databases", [])) if discovered_databases else 0,
        "chat_initialized": initial_chat_state is not None
    }


@app.get('/chat/init')
async def get_initial_chat_state() -> Dict[str, Any]:
    """Get the initial chat state with auto-generated introduction.
    
    Returns:
        Dictionary containing the introduction, schema, and discovered databases
    """
    if initial_chat_state is None:
        raise HTTPException(status_code=503, detail="Chat initialization not yet completed")
    
    return initial_chat_state


@app.get('/databases')
async def get_discovered_databases() -> Dict[str, Any]:
    """Get list of discovered local databases."""
    if discovered_databases is None:
        raise HTTPException(status_code=503, detail="Database discovery not yet completed")
    return discovered_databases


@app.post('/databases/rediscover')
async def rediscover_databases() -> Dict[str, Any]:
    """Manually trigger database rediscovery."""
    global discovered_databases
    try:
        logger.info("Manual database rediscovery triggered...")
        discovered_databases = KedroSessionManager.run_pipeline_node(
            "discover_local_databases_node",
            {}
        )
        return discovered_databases
    except Exception as e:
        logger.error(f"Database rediscovery failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/ask-chat')
async def ask_chat(
    question: str = Form(...), 
    schema: str = Form(""), 
    model: str = Form("qwen2.5:7b"),
    session_id: str = Form(None)
) -> Dict[str, Any]:
    """Process SQL query using Kedro pipeline with session management."""
    try:
        logger.info(f"Received request - question: {question[:50]}..., schema length: {len(schema)}, model: {model}, session_id: {session_id}")
        
        # Generate session_id if not provided
        if not session_id:
            import uuid
            session_id = str(uuid.uuid4())
            logger.info(f"Generated new session_id: {session_id}")
        
        # Initialize session if doesn't exist
        if session_id not in chat_sessions:
            # If no schema provided and we have initial_chat_state, use that schema
            if not schema and initial_chat_state and initial_chat_state.get('sql_content'):
                schema = initial_chat_state.get('sql_content')
                logger.info(f"Using initial chat state schema ({len(schema)} chars)")
            
            chat_sessions[session_id] = {
                "schema": schema,
                "history": [],
                "created_at": datetime.now().isoformat()
            }
            logger.info(f"Created new chat session: {session_id}")
        else:
            # If schema is empty but session has schema, use session's schema
            if not schema and chat_sessions[session_id].get("schema"):
                schema = chat_sessions[session_id]["schema"]
                logger.info(f"Using session schema ({len(schema)} chars)")
            # Update session schema if a new one is provided
            elif schema and len(schema) > len(chat_sessions[session_id].get("schema", "")):
                chat_sessions[session_id]["schema"] = schema
                logger.info(f"Updated session schema ({len(schema)} chars)")
        
        # Add question to history
        chat_sessions[session_id]["history"].append({
            "type": "question",
            "content": question,
            "timestamp": datetime.now().isoformat()
        })
        
        # Build chat history for context (convert to simpler format)
        chat_history = []
        for item in chat_sessions[session_id]["history"][-10:]:  # Last 5 exchanges (10 messages)
            if item["type"] == "question":
                chat_history.append({"role": "user", "content": item["content"]})
            elif item["type"] == "response":
                # Extract the explanation or query as assistant response
                content = item["content"]
                if isinstance(content, dict):
                    response_text = content.get("explain", "") or content.get("query", "")
                else:
                    response_text = str(content)
                chat_history.append({"role": "assistant", "content": response_text})
        
        # Always execute queries by default
        should_execute = True
        
        # Warn if schema is empty
        if not schema or len(schema.strip()) == 0:
            logger.warning("Schema is empty for query processing - query quality may be poor")
        
        inputs = {
            "requirement": question,
            "schema": schema,
            "model": model,
            "is_explain": False,
            "chat_history": chat_history[:-1],  # Exclude current question
            "execute_query": should_execute
        }
        
        result = KedroSessionManager.run_pipeline_node("process_sql_query_node", inputs)
        
        # Add result to history
        chat_sessions[session_id]["history"].append({
            "type": "response",
            "content": result,
            "timestamp": datetime.now().isoformat()
        })
        
        # Include session info and discovered databases in the response
        result["session_id"] = session_id
        result["history_length"] = len(chat_sessions[session_id]["history"])
        if discovered_databases:
            result["available_databases"] = discovered_databases.get("databases", [])
        
        return result
        
    except Exception as e:
        logger.error(f"Error in ask_chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/chat/{session_id}/history')
async def get_chat_history(session_id: str) -> Dict[str, Any]:
    """Get chat history for a specific session.
    
    Args:
        session_id: The chat session ID
        
    Returns:
        Dictionary containing chat history
    """
    global chat_sessions
    
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {
        "session_id": session_id,
        "history": chat_sessions[session_id]["history"],
        "created_at": chat_sessions[session_id]["created_at"],
        "message_count": len(chat_sessions[session_id]["history"])
    }


@app.delete('/chat/{session_id}')
async def clear_chat_session(session_id: str) -> Dict[str, str]:
    """Clear a chat session.
    
    Args:
        session_id: The chat session ID to clear
        
    Returns:
        Success message
    """
    global chat_sessions
    
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    
    return {"message": f"Session {session_id} cleared successfully"}



@app.post('/init-chat')
async def initialize_chat(file: UploadFile = File(...)) -> Dict[str, Any]:
    """Initialize chat by processing SQL schema file using Kedro pipeline."""
    try:
        if file is None:
            raise HTTPException(status_code=404, detail="File not found")
            
        contents = await file.read()
        schema_content = contents.decode('utf-8')
        
        inputs = {"schema_content": schema_content}
        result = KedroSessionManager.run_pipeline_node("initialize_schema_processing_node", inputs)
        
        # Include discovered databases in the response
        if discovered_databases:
            result["discovered_databases"] = {
                "count": len(discovered_databases.get("databases", [])),
                "databases": discovered_databases.get("databases", []),
                "summary": discovered_databases.get("summary", "")
            }
        
        return result
        
    except Exception as e:
        logger.error(f"Error in initialize_chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/auto-schema')
async def auto_create_schema_endpoint(db_index: int = Form(0)) -> Dict[str, Any]:
    """Automatically create schema from a discovered database.
    
    Args:
        db_index: Index of the database to extract schema from (default: 0)
    """
    try:
        if discovered_databases is None:
            raise HTTPException(status_code=503, detail="Database discovery not yet completed")
        
        databases = discovered_databases.get("databases", [])
        if not databases:
            raise HTTPException(status_code=404, detail="No databases discovered")
        
        if db_index >= len(databases):
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid database index. Found {len(databases)} databases."
            )
        
        inputs = {
            "discovered_databases": discovered_databases,
            "db_index": db_index
        }
        
        result = KedroSessionManager.run_pipeline_node("auto_create_schema_node", inputs)
        
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in auto_create_schema: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/extract-schema')
async def extract_schema_endpoint(
    db_type: str = Form(...),
    host: str = Form("localhost"),
    port: int = Form(None),
    database: str = Form(...),
    username: str = Form(None),
    password: str = Form(None),
    path: str = Form(None)
) -> Dict[str, Any]:
    """Extract schema from a specific database with connection parameters.
    
    Args:
        db_type: Type of database (postgresql, mysql, sqlite)
        host: Database host (for PostgreSQL/MySQL)
        port: Database port (for PostgreSQL/MySQL)
        database: Database name or path
        username: Database username (for PostgreSQL/MySQL)
        password: Database password (for PostgreSQL/MySQL)
        path: Database file path (for SQLite)
    """
    try:
        from sql_bigbrother.pipelines.sql_processing.nodes import extract_schema_from_database, initialize_schema_processing
        
        # Prepare connection parameters
        connection_params = {}
        
        if db_type == "sqlite":
            if not path:
                raise HTTPException(status_code=400, detail="SQLite requires 'path' parameter")
            connection_params = {"path": path}
        elif db_type == "postgresql":
            connection_params = {
                "host": host,
                "port": port or 5432,
                "database": database,
                "user": username,
                "password": password
            }
        elif db_type == "mysql":
            connection_params = {
                "host": host,
                "port": port or 3306,
                "database": database,
                "user": username,
                "password": password
            }
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported database type: {db_type}")
        
        # Extract schema
        schema_content = extract_schema_from_database(db_type, connection_params)
        
        # Process the schema
        result = initialize_schema_processing(schema_content)
        result["auto_generated"] = True
        result["database_type"] = db_type
        
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in extract_schema: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/sessions')
async def get_sessions() -> Dict[str, Any]:
    """Get all active chat sessions."""
    sessions_summary = {}
    for session_id, session_data in chat_sessions.items():
        sessions_summary[session_id] = {
            "created_at": session_data.get("created_at"),
            "message_count": len(session_data.get("history", [])),
            "has_schema": bool(session_data.get("schema"))
        }
    return {"sessions": sessions_summary, "total": len(sessions_summary)}


@app.get('/sessions/{session_id}')
async def get_session(session_id: str) -> Dict[str, Any]:
    """Get specific chat session details."""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return chat_sessions[session_id]


@app.delete('/sessions/{session_id}')
async def delete_session(session_id: str) -> Dict[str, str]:
    """Delete a chat session."""
    if session_id not in chat_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    del chat_sessions[session_id]
    return {"message": f"Session {session_id} deleted successfully"}


    return {"status": "healthy", "service": "SQL BigBrother"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sql_bigbrother.core.api.main:app", host="0.0.0.0", port=8000, reload=True)
    
