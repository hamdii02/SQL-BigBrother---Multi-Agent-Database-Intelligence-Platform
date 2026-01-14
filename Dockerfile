# Dockerfile for SQL BigBrother Kedro Project
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml requirements.txt ./
COPY src/ src/
COPY conf/ conf/
COPY data/ data/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e .

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app/src
ENV KEDRO_PROJECT_PATH=/app

# Run the FastAPI server
CMD ["python", "-m", "uvicorn", "sql_bigbrother.core.api.main:app", "--host", "0.0.0.0", "--port", "8000"]