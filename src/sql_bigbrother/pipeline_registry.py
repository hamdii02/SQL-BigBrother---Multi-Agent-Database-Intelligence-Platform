"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from sql_bigbrother.pipelines.sql_processing import create_pipeline as create_sql_processing_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    
    # Add our custom SQL processing pipeline
    pipelines["sql_processing"] = create_sql_processing_pipeline()
    
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
