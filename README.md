# SQL BigBrother - Multi-Agent Database Intelligence Platform

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## 🛠️ Technologies Stack

### Multi-Agent AI Framework
- **[CrewAI](https://github.com/joaomdmoura/crewai)** (v1.6.1+) - Orchestrates specialized AI agents for SQL generation, query optimization, schema analysis, and database interaction
- **[LangGraph](https://github.com/langchain-ai/langgraph)** (v1.0.6+) - State machine framework for building agentic workflows, used for database discovery and multi-step reasoning
- **[LangChain Community](https://github.com/langchain-ai/langchain)** (v0.4.1+) - LLM integration and prompt management
- **[LangChain Ollama](https://github.com/langchain-ai/langchain)** (v1.0.0+) - Local LLM integration with Ollama

### Local AI/LLM
- **[Ollama](https://ollama.ai)** - Local LLM inference engine (supports Qwen 2.5, Llama, GPT-OSS, and more)
- **Supported Models**:
  - `qwen2.5:7b` - Fast & efficient (4.7GB)
  - `qwen2.5:14b` - Balanced performance (9.0GB)
  - `gpt-oss:20b` - Most capable (13GB)

### Backend Framework
- **[Kedro](https://kedro.org)** (v1.1.1) - Data pipeline framework for orchestrating ML workflows
- **[FastAPI](https://fastapi.tiangolo.com/)** (v0.123.4+) - High-performance Python API framework
- **[Uvicorn](https://www.uvicorn.org/)** (v0.38.0+) - ASGI server for FastAPI
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** (v1.2.1+) - Environment configuration
- **[Python-multipart](https://github.com/andrew-d/python-multipart)** (v0.0.20+) - File upload support

### Database Connectors & Libraries
- **[PyMySQL](https://github.com/PyMySQL/PyMySQL)** (v1.1.2+) - Pure Python MySQL client
- **[mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)** (v9.5.0+) - Official MySQL connector
- **[psycopg2](https://github.com/psycopg/psycopg2)** - PostgreSQL adapter (optional)
- **[sqlite3](https://docs.python.org/3/library/sqlite3.html)** - Built-in SQLite support

### Authentication Service (Node.js)
- **[Express.js](https://expressjs.com/)** (v4.19.2+) - Web application framework
- **[Mongoose](https://mongoosejs.com/)** (v8.3.2+) - MongoDB object modeling
- **[bcrypt](https://github.com/kelektiv/node.bcrypt.js)** (v5.1.1+) - Password hashing
- **[jsonwebtoken](https://github.com/auth0/node-jsonwebtoken)** (v9.0.2+) - JWT authentication
- **[express-session](https://github.com/expressjs/session)** (v1.18.0+) - Session management
- **[cors](https://github.com/expressjs/cors)** (v2.8.5+) - CORS middleware
- **[helmet](https://helmetjs.github.io/)** (v7.1.0+) - Security headers
- **[morgan](https://github.com/expressjs/morgan)** (v1.10.0+) - HTTP request logger

### Frontend Framework & UI
- **[React](https://react.dev/)** (v18.2.0) - UI framework
- **[Vite](https://vitejs.dev/)** (v5.3.1+) - Build tool and dev server
- **[React Router DOM](https://reactrouter.com/)** (v6.23.1+) - Client-side routing
- **[Axios](https://axios-http.com/)** (v1.7.2+) - HTTP client
- **[TailwindCSS](https://tailwindcss.com/)** (v3.4.4+) - Utility-first CSS framework
- **[DaisyUI](https://daisyui.com/)** (v4.12.2+) - Tailwind component library
- **[React Icons](https://react-icons.github.io/react-icons/)** (v5.2.1+) - Icon library
- **[React Markdown](https://remarkjs.github.io/react-markdown/)** (v9.0.1+) - Markdown rendering
- **[React Syntax Highlighter](https://github.com/react-syntax-highlighter/react-syntax-highlighter)** (v15.5.0+) - Code syntax highlighting
- **[Prism.js](https://prismjs.com/)** (v1.29.0+) - Syntax highlighting theme
- **[Nivo](https://nivo.rocks/)** (v0.87.0+) - Data visualization library
- **[D3.js](https://d3js.org/)** (v7.9.0+) - Data-driven visualizations
- **[Moment.js](https://momentjs.com/)** (v2.30.1+) - Date manipulation
- **[Socket.io Client](https://socket.io/)** (v4.7.5+) - Real-time bidirectional communication

### Data Science & Visualization
- **[scikit-learn](https://scikit-learn.org/)** (v1.5.1+) - Machine learning library
- **[seaborn](https://seaborn.pydata.org/)** (v0.12.1+) - Statistical data visualization
- **[Jupyter Lab](https://jupyter.org/)** (v3.0+) - Interactive development environment
- **[Kedro-viz](https://github.com/kedro-org/kedro-viz)** (v6.7.0+) - Pipeline visualization

### Development & Utilities
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer
- **[nodemon](https://nodemon.io/)** (v3.1.2+) - Node.js auto-restart utility
- **[ESLint](https://eslint.org/)** (v8.57.0+) - JavaScript linter
- **[Autoprefixer](https://github.com/postcss/autoprefixer)** (v10.4.19+) - CSS vendor prefixing
- **[PostCSS](https://postcss.org/)** (v8.4.38+) - CSS transformation tool

## Overview

SQL BigBrother is a multi-agent AI-powered SQL optimization system built with Kedro 1.1.1. This system uses **CrewAI agents** orchestrating specialized roles for SQL query generation, optimization, and analysis, combined with **LangGraph** for stateful agentic workflows like database discovery. The platform leverages **local Ollama models** to provide enterprise-grade database intelligence entirely offline, without requiring external API keys or cloud dependencies.

## Features

- 🤖 **Local AI Processing**: Uses Ollama for local LLM inference (no external API keys required)
- � **Database Discovery Agent**: Automatic detection of PostgreSQL, MySQL, and SQLite databases using LangGraph agents
- �📊 **Schema Upload & Analysis**: Upload SQL schema files and get AI-generated insights
- 💬 **Interactive Chat Interface**: Ask questions about your database schema
- 🔍 **SQL Query Generation**: Generate optimized SQL queries based on natural language requests
- 📈 **Query Analysis**: Get explanations and optimizations for existing SQL queries
- 🔐 **Authentication System**: Secure user authentication and chat history

## Project Structure

```
sql-bigbrother/
├── src/sql_bigbrother/
│   ├── core/                    # Core application components  
│   │   ├── api/                 # FastAPI backend services
│   │   ├── auth/                # Node.js authentication service
│   │   ├── backup/              # Backup utilities
│   │   ├── frontend/            # React frontend application  
│   │   └── https/               # HTTP test files
│   ├── pipelines/
│   │   └── sql_processing/      # Kedro SQL processing pipeline
│   └── api/                     # FastAPI integration (symlink to core/api)
├── conf/                        # Kedro configuration files
├── data/                        # Data storage
└── run_server.py               # FastAPI server startup script
```

## 🎥 Demo

### Video Demo

[📹 Watch Demo Video](./media/demo_sql_agents.m4v)

### Screenshots

#### Interface Overview
![Interface Overview](./media/Capture%20d'écran%202026-01-27%20à%2017.14.23.png)

#### Chat Interface & SQL Query Generation
![Chat Interface](./media/Capture%20d'écran%202026-01-27%20à%2017.14.43.png)

#### Query Results & Data Visualization
![Query Results](./media/Capture%20d'écran%202026-01-27%20à%2017.15.09.png)

#### Schema Analysis
![Schema Analysis](./media/Capture%20d'écran%202026-01-27%20à%2017.15.17.png)

#### Query Explanation & Optimization
![Query Explanation](./media/Capture%20d'écran%202026-01-27%20à%2017.15.57.png)

## Prerequisites

1. **Install Ollama**: Download and install [Ollama](https://ollama.ai)
2. **Pull AI Models**: Install required models
   ```bash
   # Install recommended models (choose based on your system resources)
   ollama pull qwen2.5:7b      # Fastest, 4.7GB
   ollama pull qwen2.5:14b     # Balanced, 9.0GB  
   ollama pull gpt-oss:20b     # Most capable, 13GB
   ```
3. **Start Ollama Service**:
   ```bash
   ollama serve
   ```

## Quick Start

1. **Setup Environment**: Run the setup script to install dependencies:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Start Required Services**:
   ```bash
   # Start Ollama service (required for AI)
   ollama serve &
   
   # Start MySQL service (required for database functionality)  
   brew services start mysql  # macOS
   # sudo systemctl start mysql  # Linux
   
   # Option 1: Use the startup script
   chmod +x start_all.sh
   ./start_all.sh
   
   # Option 2: Start services manually
   # Terminal 1: FastAPI Server with proper environment
   OPENAI_API_KEY="sk-dummy-key-for-ollama-usage" \
   CREWAI_LLM_PROVIDER="ollama" \
   OLLAMA_BASE_URL="http://localhost:11434" \
   uv run python run_server.py
   
   # Terminal 2: Authentication Server  
   cd src/sql_bigbrother/core/auth && node server.js
   
   # Terminal 3: Frontend
   cd src/sql_bigbrother/core/frontend && npm run dev
   ```

3. **Access the application**:
   - Frontend: http://localhost:5176 (or check terminal for actual port)
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Auth Service: http://localhost:2405

## Usage

### Chat Mode with Automatic Database Discovery & Schema Initialization

When the server starts, it automatically:
1. **Discovers all local databases**: PostgreSQL, MySQL, and SQLite installations
2. **Auto-initializes chat**: If SQLite databases are found, automatically extracts and loads the first one's schema
3. **Generates welcome introduction**: An AI agent creates a personalized welcome message explaining the loaded database

The discovered databases and schema are immediately available for querying—no manual upload required!

### API Endpoints

#### 1. Health Check
```bash
curl http://localhost:8000/health
# Response: 
{
  "status": "healthy",
  "service": "SQL BigBrother",
  "databases_discovered": 3,
  "chat_initialized": true
}
```

#### 2. Get Initial Chat State (NEW)
```bash
# Get the auto-generated welcome message and loaded schema
curl http://localhost:8000/chat/init

# Expected Response:
{
  "title": "Cinema Database",
  "introduction": "Welcome! 👋 I've automatically loaded the Cinema Database schema for you...",
  "recommends": ["Question 1", "Question 2", "Question 3", "Question 4"],
  "sql_content": "CREATE TABLE...",
  "auto_initialized": true,
  "discovered_databases": {
    "databases": [...],
    "summary": "..."
  }
}
```

#### 3. Get Discovered Databases
```bash
curl http://localhost:8000/databases

# Expected Response:
{
  "databases": [
    {
      "type": "postgresql",
      "status": "available",
      "output": "psql (PostgreSQL) 15.3"
    },
    {
      "type": "mysql",
      "status": "available",
      "output": "mysql Ver 8.0.33"
    }
  ],
  "os_type": "darwin",
  "commands_executed": ["psql --version: SUCCESS", ...],
  "summary": "{'total_found': 2, 'databases_by_type': {'postgresql': 1, 'mysql': 1}}",
  "discovery_timestamp": "2026-01-14T10:30:00"
}
```

#### 3. Rediscover Databases (NEW)
```bash
curl -X POST http://localhost:8000/databases/rediscover

# Triggers a fresh database discovery scan
```

#### 4. Ask Chat (SQL Query Generation)
```bash
curl -X 'POST' \
  'http://localhost:8000/ask-chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'question=Get all users with their email addresses&schema=CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255));&model=qwen2.5:7b'

# Expected Response:
{
  "query": "SELECT id, name, email FROM users;",
  "explain": "",
  "rows": [...],
  "columns": [...],
  "available_databases": [...]  # Includes discovered databases
}
```

#### 5. Initialize Chat (Schema Upload)
```bash
curl -X 'POST' \
  'http://localhost:8000/init-chat' \
  -H 'accept: application/json' \
  -F 'file=@path/to/schema.sql'

# Expected Response:
{
  "title": "Generated Schema Title",
  "recommends": ["Recommended question 1", "Recommended question 2"],
  "sql_content": "Original schema content",
  "discovered_databases": {
    "count": 3,
    "databases": [...],
    "summary": "Database discovery summary"
  }
}
```

#### 6. Auto-Create Schema from Discovered Database (NEW)
```bash
# Automatically extract and process schema from a discovered database
curl -X 'POST' \
  'http://localhost:8000/auto-schema' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'db_index=0'

# Expected Response:
{
  "title": "Auto-Generated Schema Title",
  "recommends": ["Recommended question 1", "Recommended question 2"],
  "sql_content": "Extracted schema content",
  "auto_generated": true,
  "source_database": {
    "type": "sqlite",
    "path": "/path/to/database.db"
  }
}
```

#### 7. Extract Schema with Connection Parameters (NEW)
```bash
# For SQLite
curl -X 'POST' \
  'http://localhost:8000/extract-schema' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'db_type=sqlite&path=/path/to/database.db'

# For PostgreSQL
curl -X 'POST' \
  'http://localhost:8000/extract-schema' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'db_type=postgresql&host=localhost&port=5432&database=mydb&username=user&password=pass'

# For MySQL
curl -X 'POST' \
  'http://localhost:8000/extract-schema' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'db_type=mysql&host=localhost&port=3306&database=mydb&username=user&password=pass'
```

### Frontend Usage

#### 1. Automatic Schema Creation (NEW)
- Navigate to the frontend application at http://localhost:5176
- Go to the Chat page
- Click "Discover Databases" to see all locally discovered databases
- Select a database and click "Auto-Generate Schema" 
- The system will automatically extract and process the schema

#### 2. Upload Schema (Traditional Method)
- Navigate to the frontend application at http://localhost:5176
- Go to the Chat page and click the Schema tab
- Click "Click here to upload schema" 
- Upload a SQL schema file (samples available in `data/01_raw/sample_schemas/`)

#### 3. Ask Questions
- Once schema is uploaded or auto-generated, you'll get AI-generated title and recommended questions
- Ask natural language questions about your database
- Request SQL queries based on your requirements

#### 4. Analyze Results  
- Get optimized SQL queries with explanations
- View query execution details and performance insights
- Save chat conversations for future reference

### Available Models

The system automatically detects available models. Check what's installed:
```bash
ollama list
```

Supported model formats:
- `qwen2.5:7b` (recommended for development)
- `qwen2.5:14b` (balanced performance/quality)
- `qwen3:14b` (newer version)
- `qwen3:30b` (high quality, resource intensive)
- `gpt-oss:20b` (alternative high-quality model)

## Configuration

### Firebase Configuration (Required)

Before running the application, you need to configure Firebase for authentication and data storage:

1. **Create a Firebase project** at [Firebase Console](https://console.firebase.google.com/)

2. **Copy the example configuration file**:
   ```bash
   cd src/sql_bigbrother/core/frontend/src/firebase
   cp config.example.js config.js
   ```

3. **Update Firebase configuration** in:
   ```
   src/sql_bigbrother/core/frontend/src/firebase/config.js
   ```
   
   Replace the configuration with your Firebase project credentials:
   ```javascript
   const firebaseConfig = {
     apiKey: "YOUR_API_KEY",
     authDomain: "YOUR_AUTH_DOMAIN",
     projectId: "YOUR_PROJECT_ID",
     storageBucket: "YOUR_STORAGE_BUCKET",
     messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
     appId: "YOUR_APP_ID"
   };
   ```

4. **Update environment variables** (optional - if using `.env` file):
   ```bash
   # Create .env file in frontend directory
   cd src/sql_bigbrother/core/frontend
   
   # Add Firebase configuration
   VITE_FIREBASE_API_KEY=your_api_key
   VITE_FIREBASE_AUTH_DOMAIN=your_auth_domain
   VITE_FIREBASE_PROJECT_ID=your_project_id
   VITE_FIREBASE_STORAGE_BUCKET=your_storage_bucket
   VITE_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
   VITE_FIREBASE_APP_ID=your_app_id
   ```

> **Note**: The `config.js` file is gitignored to prevent accidental credential commits. Always use `config.example.js` as a template.

### AI Models
The system automatically detects available Ollama models and uses the best one available:
- **qwen2.5:7b**: Fast, suitable for most tasks
- **qwen2.5:14b**: Better quality, more resource intensive  
- **gpt-oss:20b**: Highest quality, requires significant resources

### External APIs (Optional)
If you prefer using external AI services, you can set environment variables:
```bash
export GROQ_API_KEY="your_groq_api_key"
export OPENAI_API_KEY="your_openai_api_key"  
```

## Development Guidelines

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## Architecture

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         Frontend (React)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │Dashboard │  │ Queries  │  │ Agents   │  │ Connections  │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘   │
└───────┼─────────────┼─────────────┼────────────────┼───────────┘
        │             │             │                │
        └─────────────┴─────────────┴────────────────┘
                            │
                ┌───────────▼────────────┐
                │   FastAPI Backend      │
                │  (Python Endpoints)    │
                └───────────┬────────────┘
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
┌───────▼────────┐  ┌───────▼────────┐  ┌───────▼────────┐
│  LLM Service   │  │ Agent Manager  │  │ DB Connections │
│ (Ollama/Local) │  │   (CrewAI)     │  │   Service      │
└───────┬────────┘  └───────┬────────┘  └───────┬────────┘
        │                   │                    │
        │           ┌───────▼────────┐           │
        │           │ Agent Executor │           │
        │           └───────┬────────┘           │
        │                   │                    │
        └───────────────────┼────────────────────┘
                            │
                ┌───────────▼────────────┐
                │   Database Layer       │
                │  (PostgreSQL/MySQL)    │
                └────────────────────────┘
```

### Backend Services
- **FastAPI Server** (port 8000): Main API server with Kedro pipeline integration
- **Authentication Service** (port 2405): Node.js server handling user auth and chat history
- **Ollama Service** (port 11434): Local AI model inference

### Frontend
- **React Application**: Modern web interface built with Vite and Tailwind CSS
- **Real-time Chat**: Interactive chat interface for SQL queries and schema analysis

### AI Pipeline
- **CrewAI Agents**: Specialized AI agents for different tasks (SQL generation, analysis, recommendations)
- **Local Processing**: All AI processing happens locally via Ollama
- **Schema Analysis**: Automatic schema parsing and intelligent question generation

### Agent Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Agent System                            │
│                                                             │
│  ┌────────────────────────────────────────────────────┐   │
│  │            Agent Executor (Core)                   │   │
│  │  • Manages agent lifecycle                         │   │
│  │  • Routes queries to appropriate agents            │   │
│  │  • Handles agent communication                     │   │
│  └─────────────────┬──────────────────────────────────┘   │
│                    │                                       │
│       ┌────────────┼────────────┬────────────┐            │
│       │            │            │            │            │
│  ┌────▼─────┐ ┌───▼──────┐ ┌──▼───────┐ ┌─▼─────────┐   │
│  │ SQL      │ │ Analysis │ │ Security │ │ Database  │   │
│  │ Agent    │ │ Agent    │ │ Agent    │ │ Discovery │   │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └─┬─────────┘   │
│       │            │            │          │             │
│       └────────────┼────────────┴──────────┘             │
│                    │                                       │
│       ┌────────────▼────────────┐                         │
│       │    LLM Integration      │                         │
│       │  (Ollama - Local)       │                         │
│       └─────────────────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

### Agent Responsibilities

#### 1. Agent Executor (Core Orchestrator)
Located in: `src/sql_bigbrother/core/api/`

**Responsibilities:**
- **Agent Lifecycle Management**: Creates, initializes, and manages agent instances
- **Query Routing**: Determines which agent should handle specific queries
- **Context Management**: Maintains conversation history and context
- **Tool Integration**: Provides access to database tools and utilities
- **Error Handling**: Manages failures and fallbacks between agents

**Key Capabilities:**
- `execute_query()` - Main entry point for processing queries
- `route_to_agent()` - Intelligent routing based on query type
- `maintain_history()` - Keeps track of conversation context

#### 2. Database Discovery Agent (NEW)
Located in: `src/sql_bigbrother/pipelines/sql_processing/nodes.py`

**Responsibilities:**
- **Automatic Database Detection**: Discovers PostgreSQL, MySQL, and SQLite installations
- **System Command Execution**: Runs OS-specific commands to identify database services
- **Database File Scanning**: Locates SQLite database files on the local filesystem
- **Connection Validation**: Tests database availability and accessibility
- **Multi-OS Support**: Works across macOS, Linux, and Windows platforms

**Key Capabilities:**
- `check_os()` - Detects operating system type
- `discover_postgres()` - Finds PostgreSQL installations and running instances
- `discover_mysql()` - Identifies MySQL/MariaDB services
- `discover_sqlite()` - Locates SQLite database files
- `summarize_discovery()` - Provides comprehensive discovery report

**LangGraph Workflow:**
```
Start → Check OS → Discover PostgreSQL → Discover MySQL 
     → Discover SQLite → Summarize → End
```

#### 3. SQL Agent
Located in: `src/sql_bigbrother/core/api/prompts/`

**Responsibilities:**
- **Query Generation**: Converts natural language to SQL queries
- **Query Validation**: Ensures SQL syntax is correct
- **Query Optimization**: Suggests improvements for performance
- **Schema Understanding**: Analyzes database schema to generate accurate queries
- **Multi-Database Support**: Handles different SQL dialects (PostgreSQL, MySQL, etc.)

**Key Capabilities:**
- `generate_sql()` - Creates SQL from natural language
- `validate_query()` - Checks SQL correctness
- `explain_query()` - Provides query explanations

#### 4. Analysis Agent
Located in: `src/sql_bigbrother/core/api/prompts/`

**Responsibilities:**
- **Data Interpretation**: Analyzes query results and provides insights
- **Trend Detection**: Identifies patterns and anomalies in data
- **Visualization Suggestions**: Recommends appropriate charts/graphs
- **Report Generation**: Creates summaries and reports from data
- **Business Intelligence**: Translates data into actionable insights

**Key Capabilities:**
- `analyze_results()` - Interprets query output
- `generate_insights()` - Provides business insights
- `suggest_visualizations()` - Recommends data viz approaches

#### 5. Security Agent
Located in: `src/sql_bigbrother/core/api/services/`

**Responsibilities:**
- **SQL Injection Prevention**: Detects and blocks malicious queries
- **Access Control**: Enforces user permissions and roles
- **Audit Logging**: Tracks all query executions and modifications
- **Query Sanitization**: Cleans and validates input queries
- **Compliance Checking**: Ensures queries meet security standards

**Key Capabilities:**
- `validate_security()` - Checks for security threats
- `enforce_permissions()` - Validates user access rights
- `audit_query()` - Logs query execution for compliance

### Data Flow

```
User Query
    │
    ▼
Frontend (React)
    │
    ▼
API Endpoint (/api/query)
    │
    ▼
Agent Executor
    │
    ├─► Security Agent (Validates query safety)
    │        │
    │        ▼
    ├─► SQL Agent (Generates SQL)
    │        │
    │        ▼
    ├─► Database Execution
    │        │
    │        ▼
    └─► Analysis Agent (Interprets results)
         │
         ▼
    Response to User
```

### Key Technologies

- **Backend**: FastAPI (Python)
- **Frontend**: React + Vite
- **AI/LLM**: Ollama (Local), OpenAI GPT / Claude (optional)
- **Database**: PostgreSQL (primary), MySQL, SQLite (supported)
- **Agent Framework**: CrewAI with custom implementations

## Installation & Dependencies

### System Requirements

- **Python 3.11+** with `uv` package manager
- **Node.js 18+** with `npm`
- **Ollama** installed and running
- **8GB+ RAM** for basic models (16GB+ recommended)

### Complete Installation Steps

1. **Install System Dependencies**:
   ```bash
   # Install uv (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Install Node.js (if not already installed)
   # macOS: brew install node
   # Ubuntu: sudo apt install nodejs npm
   
   # Install Ollama
   # Visit https://ollama.ai for installation instructions
   ```

2. **Install Project Dependencies**:
   ```bash
   # Install Python dependencies
   uv sync
   
   # Install Node.js dependencies for auth service
   cd src/sql_bigbrother/core/auth && npm install
   
   # Install Node.js dependencies for frontend  
   cd src/sql_bigbrother/core/frontend && npm install
   
   # Return to project root
   cd ../../../..
   ```

3. **Install AI Models**:
   ```bash
   # Start Ollama service
   ollama serve &
   
   # Install models (choose based on your system)
   ollama pull qwen2.5:7b      # 4.7GB - Fast, recommended for development
   ollama pull qwen2.5:14b     # 9.0GB - Better quality
   ollama pull gpt-oss:20b     # 13GB - Highest quality (optional)
   ```

4. **Verify Installation**:
   ```bash
   # Test Ollama
   curl http://localhost:11434/api/tags
   
   # Test model
   ollama run qwen2.5:7b "Hello, how are you?"
   
   # Test Python environment
   uv run python -c "import crewai; print('CrewAI installed successfully')"
   ```

### Missing Dependencies Resolution

#### ❌ **Problem**: `uv: command not found`
```bash
# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # or restart terminal
```

#### ❌ **Problem**: `node: command not found`
```bash
# macOS
brew install node

# Ubuntu/Debian
sudo apt update && sudo apt install nodejs npm

# Verify installation
node --version && npm --version
```

#### ❌ **Problem**: `ollama: command not found`
```bash
# Install Ollama - visit https://ollama.ai
# Or use curl (Linux/macOS):
curl -fsSL https://ollama.ai/install.sh | sh

# Verify installation
ollama --version
```

#### ❌ **Problem**: Python module import errors
```bash
# Ensure you're in the right environment
uv sync --dev

# Install specific missing packages
uv add crewai langchain-ollama fastapi uvicorn

# For LiteLLM support (if needed)
uv add litellm
```

#### ❌ **Problem**: Node.js dependency issues
```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# For permission issues (Linux/macOS)
sudo npm install -g npm
```

### Environment Variables

Create a `.env` file in the project root (optional but recommended):
```bash
# Database Configuration (for MySQL integration)
DB_USER=root
DB_PASSWORD=
DB_NAME_SETUP=sql_bigbrother
DB_NAME_USE=sql_bigbrother

# Optional: External AI APIs (if you don't want to use Ollama)
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GROQ_API_BASE=your_groq_base_url
GROQ_MODEL_NAME=your_groq_model

# Server configuration (optional)
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
AUTH_PORT=2405
FRONTEND_PORT=5176

# CrewAI Configuration (for local Ollama)
CREWAI_LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
```

### Docker Setup (Alternative)

If you prefer Docker:
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access services
# Frontend: http://localhost:5176
# API: http://localhost:8000
# Auth: http://localhost:2405
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the files `tests/test_run.py` and `tests/pipelines/data_science/test_pipeline.py` for instructions on how to write your tests. Run the tests as follows:

```
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.

## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Troubleshooting

### API Request Issues

#### ❌ **Problem**: `curl` request returns "Model qwen2_5_7b not found: 404 page not found"
**Root Cause**: Model name format mismatch and CrewAI configuration issues.

**Solutions**:
1. **Fix Model Name Format**:
   ```bash
   # ❌ Wrong format
   model=qwen2_5_7b
   
   # ✅ Correct format  
   model=qwen2.5:7b
   ```

2. **Use Valid SQL Schema**:
   ```bash
   # ❌ Invalid schema
   schema=string
   
   # ✅ Valid schema
   schema=CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));
   ```

3. **Correct curl Command**:
   ```bash
   curl -X 'POST' \
     'http://localhost:8000/ask-chat' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     -d 'question=Hello, write a SQL query to get all users&schema=CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));&model=qwen2.5:7b'
   ```

#### ❌ **Problem**: "OpenAI API call failed" or "OPENAI_API_KEY is required"
**Root Cause**: CrewAI defaulting to OpenAI instead of using Ollama.

**Solution**: Ensure proper environment variables are set when starting the server:
```bash
# Set environment variables for Ollama
export OPENAI_API_KEY="sk-dummy-key-for-ollama-usage"
export CREWAI_LLM_PROVIDER="ollama"  
export OLLAMA_BASE_URL="http://localhost:11434"

# Start server with environment
uv run python run_server.py
```

#### ❌ **Problem**: "'TaskOutput' object has no attribute 'raw_output'"
**Root Cause**: CrewAI version compatibility issue with TaskOutput structure.

**Solution**: This is automatically fixed in the current codebase. If you encounter this:
- Update to the latest version of the code
- The fix changes `task.output.raw_output` to `task.output.raw`

#### ❌ **Problem**: "cannot access local variable 'connection' where it is not associated with a value"
**Root Cause**: Database connection failure (MySQL not running).

**Solutions**:
1. **Install and Start MySQL** (if you need database execution):
   ```bash
   # macOS with Homebrew
   brew install mysql
   brew services start mysql
   
   # Ubuntu/Debian
   sudo apt install mysql-server
   sudo systemctl start mysql
   ```

2. **Use SQLite** (recommended for development):
   - Modify database configuration to use SQLite instead
   - No separate database server required

3. **Skip Database Execution** (for query generation only):
   - The API will still generate SQL queries
   - Database execution errors don't prevent query generation

### Common Issues

1. **"Ollama service not running"**
   ```bash
   # Check if Ollama is running
   curl http://localhost:11434/api/tags
   
   # Start Ollama service
   ollama serve
   ```

2. **"No models available"**
   ```bash
   # List installed models
   ollama list
   
   # Install required models
   ollama pull qwen2.5:7b
   ollama pull qwen2.5:14b  # Optional, better quality
   ```

3. **"Port already in use"**
   The `run_server.py` script automatically detects and handles port conflicts:
   - **Option 1**: Automatically kill existing processes (recommended)
   - **Option 2**: Use an alternative port (8001, 8002, etc.)
   - **Option 3**: Exit and handle manually
   
   Manual port cleanup:
   ```bash
   # Kill processes on specific ports
   lsof -ti:8000 | xargs kill -9  # FastAPI
   lsof -ti:2405 | xargs kill -9  # Auth service
   lsof -ti:5176 | xargs kill -9  # Frontend
   lsof -ti:11434 | xargs kill -9 # Ollama
   ```

4. **"Schema upload not working"**
   - Ensure Ollama service is running: `ollama serve`
   - Check models are installed: `ollama list`
   - Verify FastAPI server is running: `curl http://localhost:8000/health`
   - Check server logs for detailed errors

5. **"Frontend not accessible"**
   - Check the actual port in terminal output (may be 5176 instead of 5173)
   - Ensure Node.js dependencies are installed: `cd frontend && npm install`
   - Clear browser cache and try again

6. **"CrewAI agents not responding"**
   - Verify Ollama models are working: `curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{"model": "qwen2.5:7b", "prompt": "Hello", "stream": false}'`
   - Check environment variables are set correctly
   - Restart services in correct order: Ollama → FastAPI → Frontend

7. **"Database connection errors"**
   - **MySQL not running**: `brew services start mysql` (macOS) or `sudo systemctl start mysql` (Linux)
   - **Database doesn't exist**: `mysql -u root -e "CREATE DATABASE sql_bigbrother;"`
   - **Connection denied**: Check DB_USER and DB_PASSWORD in `.env` file
   - **Port conflicts**: Default MySQL port is 3306, ensure it's not blocked

### Performance Tips

- **Memory Requirements**:
  - `qwen2.5:7b`: ~8GB RAM minimum (recommended for development)
  - `qwen2.5:14b`: ~16GB RAM minimum
  - `gpt-oss:20b`: ~24GB RAM minimum

- **Model Selection**:
  - **Fast responses**: Use `qwen2.5:7b`
  - **Balanced**: Use `qwen2.5:14b`  
  - **Best quality**: Use `gpt-oss:20b` or `qwen3:14b`

- **System Resources**:
  - Monitor CPU usage during model loading
  - SSD recommended for faster model loading
  - Close other resource-intensive applications

### Debugging Steps

1. **Check Service Status**:
   ```bash
   # Ollama
   curl http://localhost:11434/api/tags
   
   # FastAPI
   curl http://localhost:8000/health
   
   # Frontend (if running)
   curl http://localhost:5176
   ```

2. **Test Individual Components**:
   ```bash
   # Test Ollama directly
   ollama run qwen2.5:7b "Hello"
   
   # Test API endpoint
   curl -X GET http://localhost:8000/health
   
   # Test with simple query
   curl -X POST http://localhost:8000/ask-chat \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "question=Get all users&schema=CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));&model=qwen2.5:7b"
   
   # Test database connection
   mysql -u root -e "USE sql_bigbrother; SHOW TABLES;"
   ```

3. **Check Logs**:
   - **FastAPI logs**: Terminal running `run_server.py`
   - **Ollama logs**: Terminal running `ollama serve`
   - **System logs**: `tail -f /var/log/system.log` (macOS) or `journalctl -f` (Linux)

### Getting Help

If you encounter issues not covered here:

1. **Check Dependencies**:
   ```bash
   # Python environment
   uv run python --version
   uv run pip list | grep -E "(crewai|langchain|fastapi)"
   
   # Node.js environment  
   node --version
   npm --version
   ```

2. **Enable Verbose Logging**:
   - Add `verbose=True` to Crew configurations
   - Set `DEBUG=True` in FastAPI settings
   - Check browser developer console for frontend issues

3. **Reset Environment**:
   ```bash
   # Clean restart
   pkill -f "ollama\|uvicorn\|node"
   
   # Restart services
   ollama serve &
   sleep 5
   uv run python run_server.py
   ```

### Database Configuration

#### MySQL Setup (Recommended for Full Functionality)

**macOS Installation:**
```bash
# Install MySQL using Homebrew
brew install mysql

# Start MySQL service
brew services start mysql

# Create database for SQL BigBrother
mysql -u root -e "CREATE DATABASE IF NOT EXISTS sql_bigbrother;"

# Test connection
mysql -u root -e "USE sql_bigbrother; SELECT 'MySQL setup complete' as status;"
```

**Ubuntu/Linux Installation:**
```bash
# Install MySQL
sudo apt update && sudo apt install mysql-server

# Start MySQL service
sudo systemctl start mysql
sudo systemctl enable mysql

# Secure installation (set root password)
sudo mysql_secure_installation

# Create database
sudo mysql -u root -p -e "CREATE DATABASE sql_bigbrother;"
```

**Configuration:**
After installation, update your `.env` file:
```bash
DB_USER=root
DB_PASSWORD=          # Leave empty for default macOS setup
DB_NAME_SETUP=sql_bigbrother
DB_NAME_USE=sql_bigbrother
```

**MySQL Service Management:**
```bash
# Start/Stop MySQL (macOS)
brew services start mysql
brew services stop mysql

# Start/Stop MySQL (Linux)
sudo systemctl start mysql
sudo systemctl stop mysql

# Check status
brew services list | grep mysql  # macOS
sudo systemctl status mysql      # Linux
```

#### SQLite Setup (Recommended for Development)
SQLite requires no setup - it creates database files automatically. Update your configuration to use SQLite for easier development.

## Known Limitations & Solutions

### Current Limitations

1. **Database Connection Setup Required**
   - **Issue**: Full functionality requires MySQL or SQLite configuration
   - **Impact**: Without database, only SQL query generation works (no query execution or results)
   - **Solution**: Install and configure MySQL (see installation section above)
   - **Alternative**: Use the system for SQL generation only, execute queries manually in your preferred database tool

2. **Memory Usage with Large Models**
   - **Issue**: Models like `gpt-oss:20b` require significant RAM (20GB+)
   - **Impact**: System may become unresponsive on lower-end machines
   - **Workaround**: Use smaller models (`qwen2.5:7b` requires only ~8GB RAM)
   - **Future Fix**: Model optimization and memory management improvements

3. **CrewAI Version Compatibility**
   - **Issue**: Some CrewAI versions don't properly handle custom LLM providers
   - **Impact**: May default to OpenAI API instead of Ollama
   - **Solution**: Current codebase uses CrewAI 1.6.1 with proper Ollama configuration
   - **Future Fix**: Regular updates to track CrewAI improvements

### Complete Setup Verification

After installation, verify everything is working:

```bash
# 1. Check all services are running
curl http://localhost:11434/api/tags          # Ollama
curl http://localhost:8000/health             # FastAPI
mysql -u root -e "SELECT 1;"                 # MySQL

# 2. Test complete workflow
curl -X 'POST' \
  'http://localhost:8000/ask-chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'question=Get all users with their details&schema=CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);&model=qwen2.5:7b'

# Expected response should include generated SQL query and execution results
```

### Planned Improvements

- **Enhanced Database Support**: SQLite integration for zero-config setup
- **Query Optimization**: Advanced SQL query analysis and optimization suggestions  
- **Model Management**: Automatic model downloading and management
- **Performance Monitoring**: Real-time performance metrics and optimization tips
- **Multi-Database Support**: Support for PostgreSQL, SQL Server, Oracle
- **Export Features**: Export chat history and generated queries
- **Query Execution History**: Track and analyze query performance over time

### Contributing

This project is open for contributions. Common areas that need help:

1. **Database Integrations**: Adding support for more database types
2. **Performance Optimization**: Improving response times and memory usage
3. **UI/UX Improvements**: Enhancing the frontend experience
4. **Testing**: Adding comprehensive test coverage
5. **Documentation**: Improving setup guides and troubleshooting

### Version History

- **v0.1.0**: Initial release with OpenAI/Groq integration
- **v0.2.0**: Migration to local Ollama models for privacy and offline operation
- **v0.2.1**: CrewAI compatibility fixes and improved error handling
- **Current**: Enhanced troubleshooting and documentation

## Support

For issues not covered in this documentation:

1. **Check the Issues**: Look at existing GitHub issues for similar problems
2. **Enable Debug Mode**: Add verbose logging to get more detailed error information
3. **System Information**: Include your OS, Python version, and model information when reporting issues
4. **Minimal Reproduction**: Provide the minimal steps to reproduce the issue

### Community Resources

- **Sample Schemas**: Use files in `data/01_raw/sample_schemas/` for testing
- **Example Queries**: Check the frontend for recommended questions after schema upload
- **API Documentation**: Visit `http://localhost:8000/docs` when server is running

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)
