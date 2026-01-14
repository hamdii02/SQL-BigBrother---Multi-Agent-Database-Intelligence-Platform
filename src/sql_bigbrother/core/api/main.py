"""FastAPI integration with Kedro pipelines."""

from fastapi import FastAPI, Form, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from kedro.framework.session import KedroSession
from kedro.framework.project import configure_project
import logging
from pathlib import Path
import json
from typing import Dict, Any

# Configure Kedro project
project_path = Path(__file__).parent.parent.parent.parent.parent
configure_project("sql_bigbrother")

logger = logging.getLogger(__name__)

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
    def run_pipeline_node(node_name: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Run a specific Kedro node with given inputs."""
        with KedroSession.create(project_path=project_path) as session:
            try:
                # Run the pipeline
                if node_name == "initialize_schema_processing_node":
                    from sql_bigbrother.pipelines.sql_processing.nodes import initialize_schema_processing
                    result = initialize_schema_processing(inputs.get("schema_content"))
                elif node_name == "process_sql_query_node":
                    from sql_bigbrother.pipelines.sql_processing.nodes import process_sql_query
                    result = process_sql_query(
                        requirement=inputs.get("requirement"),
                        schema=inputs.get("schema"), 
                        model=inputs.get("model"),
                        is_explain=inputs.get("is_explain", False)
                    )
                else:
                    raise ValueError(f"Unknown node: {node_name}")
                    
                return result
                
            except Exception as e:
                logger.error(f"Error running Kedro node {node_name}: {str(e)}")
                raise HTTPException(status_code=500, detail=str(e))


@app.get('/')
async def root() -> Dict[str, str]:
    """Root endpoint."""
    return {"data": 'SQL BigBrother FastAPI with Kedro'}


@app.post('/ask-chat')
async def ask_chat(
    question: str = Form(...), 
    schema: str = Form(...), 
    model: str = Form(...)
) -> Dict[str, Any]:
    """Process SQL query using Kedro pipeline."""
    try:
        inputs = {
            "requirement": question,
            "schema": schema,
            "model": model,
            "is_explain": False
        }
        
        result = KedroSessionManager.run_pipeline_node("process_sql_query_node", inputs)
        return result
        
    except Exception as e:
        logger.error(f"Error in ask_chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


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
        
        return result
        
    except Exception as e:
        logger.error(f"Error in initialize_chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/health')
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "service": "SQL BigBrother"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("sql_bigbrother.core.api.main:app", host="0.0.0.0", port=8000, reload=True)
    
