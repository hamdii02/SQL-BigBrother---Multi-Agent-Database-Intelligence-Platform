"""SQL processing pipeline definition."""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import initialize_schema_processing, process_sql_query


def create_pipeline(**kwargs) -> Pipeline:
    """Create the SQL processing pipeline.
    
    Returns:
        A Kedro pipeline for SQL processing operations
    """
    return pipeline(
        [
            node(
                func=initialize_schema_processing,
                inputs="schema_content",
                outputs="schema_processing_result",
                name="initialize_schema_processing_node",
                tags=["initialization", "schema_processing"]
            ),
            node(
                func=process_sql_query,
                inputs=["requirement", "schema", "model", "is_explain"],
                outputs="sql_query_result",
                name="process_sql_query_node", 
                tags=["query_processing", "ai_agents"]
            ),
        ]
    )