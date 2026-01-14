"""SQL processing pipeline definition."""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import initialize_schema_processing, process_sql_query, discover_local_databases


def create_pipeline(**kwargs) -> Pipeline:
    """Create the SQL processing pipeline.
    
    Returns:
        A Kedro pipeline for SQL processing operations
    """
    return pipeline(
        [
            node(
                func=discover_local_databases,
                inputs=None,
                outputs="discovered_databases",
                name="discover_local_databases_node",
                tags=["initialization", "database_discovery", "ai_agents"]
            ),
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