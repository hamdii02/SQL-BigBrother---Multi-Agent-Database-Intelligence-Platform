"""Nodes for SQL processing pipeline."""

import logging
from typing import Dict, Any, List
import json
from crewai import Agent, Task, Crew, Process
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


def process_sql_query(requirement: str, schema: str, model: str, is_explain: bool = False) -> Dict[str, Any]:
    """Process SQL query request using AI agents.
    
    Args:
        requirement: User's query requirement
        schema: SQL schema
        model: AI model to use
        is_explain: Whether to include explanation
        
    Returns:
        Dictionary containing query, explanation, rows, and columns
    """
    try:
        agents = SQLAgents()
        tasks = SQLTasks()
        database = DatabaseManager("mysql")
        
        filtered_schema = filterSchema_v2(schema)
        query_output = ""
        explain_output = ""
        
        if is_explain:
            specialist = agents.sql_specialist_agent(model)
            expert = agents.sql_expert_agent(model)
            agent_list = [specialist, expert]

            design_task = tasks.sql_design_task(specialist, requirement, filtered_schema)  
            analyze_task = tasks.sql_expert_task(expert, design_task)
            task_list = [design_task, analyze_task]

            crew = Crew(agents=agent_list, tasks=task_list, verbose=True, process=Process.sequential)       
            crew.kickoff()
            
            query_output = extractMarkdown(design_task.output.raw) 
            explain_output = analyze_task.output.raw
        else:
            specialist = agents.sql_specialist_agent(model)
            agent_list = [specialist]

            design_task = tasks.sql_design_task(specialist, requirement, filtered_schema)  
            task_list = [design_task]
        
            crew = Crew(agents=agent_list, tasks=task_list, verbose=True)       
            crew.kickoff()
        
            query_output = extractMarkdown(design_task.output.raw) 
      
        # Setup database and execute query
        setup_success = database.setup(schema)
        if not setup_success:
            raise Exception('SQL setup failed')

        metadata = database.execute(query_output)
        query = markdownSQL(query_output)
            
        return {
            'query': query, 
            'explain': explain_output, 
            'rows': process_data(metadata['rows']), 
            'columns': metadata['columns']
        }
    except Exception as e:
        logger.error(f"SQL query processing error: {str(e)}")
        raise
