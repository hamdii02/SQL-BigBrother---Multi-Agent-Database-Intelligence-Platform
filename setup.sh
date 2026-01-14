#!/bin/bash

# SQL BigBrother Kedro Project Setup Script
echo "🚀 Setting up SQL BigBrother Kedro Project..."
echo "This script will install dependencies, configure services, and set up the environment."
echo ""

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Please run this script from the sql-bigbrother directory"
    exit 1
fi

# Detect OS
OS=$(uname -s)
echo "🔍 Detected OS: $OS"

# Check for required tools
echo "🔧 Checking for required tools..."

# Check for uv
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install it first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install it first:"
    if [ "$OS" = "Darwin" ]; then
        echo "   brew install node"
    elif [ "$OS" = "Linux" ]; then
        echo "   sudo apt update && sudo apt install nodejs npm"
    fi
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies with uv..."
uv sync

# Check for Ollama
echo "🤖 Checking for Ollama..."
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed. Installing Ollama..."
    if [ "$OS" = "Darwin" ]; then
        # macOS - download and install Ollama
        if command -v brew &> /dev/null; then
            echo "   Installing Ollama via Homebrew..."
            brew install ollama
        else
            echo "   Please install Ollama manually from https://ollama.ai"
            echo "   Or install Homebrew first: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        fi
    elif [ "$OS" = "Linux" ]; then
        echo "   Installing Ollama..."
        curl -fsSL https://ollama.ai/install.sh | sh
    fi
else
    echo "✅ Ollama is already installed"
fi

# Start Ollama service
echo "🚀 Starting Ollama service..."
if [ "$OS" = "Darwin" ]; then
    brew services start ollama 2>/dev/null || ollama serve &
elif [ "$OS" = "Linux" ]; then
    ollama serve &
fi

# Wait for Ollama to start
echo "⏳ Waiting for Ollama to start..."
sleep 5

# Install AI models
echo "🧠 Installing AI models..."
echo "   This may take several minutes depending on your internet connection..."

# Check if any models are already installed
if ollama list | grep -q "qwen2.5:7b"; then
    echo "✅ qwen2.5:7b is already installed"
else
    echo "   Installing qwen2.5:7b (recommended, ~4.7GB)..."
    ollama pull qwen2.5:7b
fi

# Check for MySQL
echo "🗄️  Checking for MySQL..."
if ! command -v mysql &> /dev/null; then
    echo "⚠️  MySQL is not installed. Installing MySQL..."
    if [ "$OS" = "Darwin" ]; then
        if command -v brew &> /dev/null; then
            echo "   Installing MySQL via Homebrew..."
            brew install mysql
            echo "   Starting MySQL service..."
            brew services start mysql
        else
            echo "   Please install Homebrew first, then run: brew install mysql"
        fi
    elif [ "$OS" = "Linux" ]; then
        echo "   Installing MySQL..."
        sudo apt update && sudo apt install mysql-server -y
        echo "   Starting MySQL service..."
        sudo systemctl start mysql
        sudo systemctl enable mysql
    fi
else
    echo "✅ MySQL is already installed"
    # Start MySQL if not running
    if [ "$OS" = "Darwin" ]; then
        brew services start mysql 2>/dev/null || echo "   MySQL may already be running"
    elif [ "$OS" = "Linux" ]; then
        sudo systemctl start mysql 2>/dev/null || echo "   MySQL may already be running"
    fi
fi

# Create database
echo "🏗️  Setting up database..."
if mysql -u root -e "CREATE DATABASE IF NOT EXISTS sql_bigbrother;" 2>/dev/null; then
    echo "✅ Database 'sql_bigbrother' created successfully"
    mysql -u root -e "USE sql_bigbrother; SELECT 'Database setup complete' as status;" 2>/dev/null
else
    echo "⚠️  Could not create database automatically. You may need to:"
    echo "   1. Set a MySQL root password: mysql_secure_installation"
    echo "   2. Create database manually: mysql -u root -p -e 'CREATE DATABASE sql_bigbrother;'"
fi

# Set up environment variables
echo "⚙️  Creating .env file..."
if [ ! -f ".env" ]; then
    cat > .env << EOF
# Database Configuration (MySQL)
DB_USER=root
DB_PASSWORD=
DB_NAME_SETUP=sql_bigbrother
DB_NAME_USE=sql_bigbrother

# Groq AI Configuration (Optional - for external AI APIs)
GROQ_API_BASE=https://api.groq.com/openai/v1
GROQ_MODEL_NAME=gemma2-9b-it
GROQ_API_KEY=your_groq_api_key_here

# OpenAI Configuration (Optional - for external AI APIs)
OPENAI_API_KEY=your_openai_api_key_here

# CrewAI Configuration (Required for local Ollama)
CREWAI_LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434

# FastAPI Configuration
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
FASTAPI_RELOAD=true

# Frontend Configuration
FRONTEND_URL=http://localhost:5176
AUTH_PORT=2405
EOF
    echo "✅ .env file created with default configuration"
else
    echo "✅ .env file already exists"
fi

# Install Node.js dependencies for auth service
echo "📦 Installing Node.js dependencies for auth service..."
cd src/sql_bigbrother/core/auth
npm install
cd ../../../..

# Install Node.js dependencies for frontend
echo "📦 Installing Node.js dependencies for frontend..."
cd src/sql_bigbrother/core/frontend
npm install

# Create frontend environment file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️  Creating frontend .env file..."
    cat > .env << EOF
# Environment variables for React frontend
VITE_BACKEND_URL=http://localhost:2405/api/v1
VITE_CREWAI_URL=http://localhost:8000
EOF
    echo "✅ Frontend .env file created"
else
    echo "✅ Frontend .env file already exists"
fi

cd ../../../..

# Final verification
echo ""
echo "🔍 Running final verification..."

# Test Ollama
if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
    echo "✅ Ollama service is running"
    MODELS=$(ollama list | grep -c "qwen")
    echo "✅ $MODELS Ollama models installed"
else
    echo "⚠️  Ollama service may not be running. Start it with: ollama serve"
fi

# Test MySQL
if mysql -u root -e "SELECT 1;" >/dev/null 2>&1; then
    echo "✅ MySQL is accessible"
    if mysql -u root -e "USE sql_bigbrother; SELECT 1;" >/dev/null 2>&1; then
        echo "✅ Database 'sql_bigbrother' is ready"
    else
        echo "⚠️  Database 'sql_bigbrother' needs to be created manually"
    fi
else
    echo "⚠️  MySQL connection failed. Check MySQL installation and service status"
fi

# Check Node.js dependencies
if [ -f "src/sql_bigbrother/core/auth/node_modules/package.json" ]; then
    echo "✅ Auth service dependencies installed"
else
    echo "⚠️  Auth service dependencies may not be installed correctly"
fi

if [ -f "src/sql_bigbrother/core/frontend/node_modules/package.json" ]; then
    echo "✅ Frontend dependencies installed"
else
    echo "⚠️  Frontend dependencies may not be installed correctly"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "🚀 To start SQL BigBrother:"
echo ""
echo "1. Start all services:"
echo "   ./start_all.sh"
echo ""
echo "2. Or start services manually:"
echo "   # Terminal 1: Start Ollama (if not running)"
echo "   ollama serve"
echo ""
echo "   # Terminal 2: Start FastAPI server"
echo "   OPENAI_API_KEY=\"sk-dummy-key-for-ollama-usage\" \\"
echo "   CREWAI_LLM_PROVIDER=\"ollama\" \\"
echo "   OLLAMA_BASE_URL=\"http://localhost:11434\" \\"
echo "   uv run python run_server.py"
echo ""
echo "   # Terminal 3: Start auth service"
echo "   cd src/sql_bigbrother/core/auth && node server.js"
echo ""
echo "   # Terminal 4: Start frontend"
echo "   cd src/sql_bigbrother/core/frontend && npm run dev"
echo ""
echo "📚 Access points:"
echo "   • Frontend:     http://localhost:5176"
echo "   • API:          http://localhost:8000"
echo "   • API Docs:     http://localhost:8000/docs"
echo "   • Auth Service: http://localhost:2405"
echo ""
echo "🧪 Test the API:"
echo "   curl -X 'POST' \\"
echo "     'http://localhost:8000/ask-chat' \\"
echo "     -H 'accept: application/json' \\"
echo "     -H 'Content-Type: application/x-www-form-urlencoded' \\"
echo "     -d 'question=Get all users&schema=CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));&model=qwen2.5:7b'"
echo ""
echo "🔧 Useful commands:"
echo "   kedro registry list              - List available pipelines"  
echo "   kedro viz                        - Visualize pipelines"
echo "   ollama list                      - Show installed models"
echo "   brew services list | grep mysql  - Check MySQL status (macOS)"
echo "   docker-compose up --build       - Run with Docker (alternative)"
echo ""
echo "📖 Check README.md for detailed troubleshooting and configuration options."