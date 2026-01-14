#!/bin/bash

# SQL BigBrother Full Stack Startup Script
echo "🚀 Starting SQL BigBrother Full Stack..."

# Function to check if a port is available
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null ; then
        echo "⚠️  Port $port is already in use"
        return 1
    fi
    return 0
}

# Check required ports
check_port 8000 || exit 1  # Kedro API
check_port 2405 || exit 1  # Auth service
check_port 5173 || exit 1  # Frontend

# Start Kedro API server in background
echo "🐍 Starting Kedro API server on port 8000..."
uv run python run_server.py &
API_PID=$!

# Wait a moment for API to start
sleep 3

# Start Auth service in background
echo "🔐 Starting Authentication service on port 2405..."
cd src/sql_bigbrother/core/auth
npm run dev &
AUTH_PID=$!
cd ../../../..

# Wait a moment for Auth to start  
sleep 3

# Start Frontend in background
echo "⚛️  Starting React Frontend on port 5173..."
cd src/sql_bigbrother/core/frontend
npm run dev &
FRONTEND_PID=$!
cd ../../../..

echo ""
echo "✅ All services started!"
echo "📚 API Documentation: http://localhost:8000/docs"
echo "🌐 Frontend Application: http://localhost:5173"
echo "🔐 Authentication Service: http://localhost:2405"
echo ""
echo "Press Ctrl+C to stop all services..."

# Function to cleanup processes on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $API_PID 2>/dev/null
    kill $AUTH_PID 2>/dev/null  
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script termination
trap cleanup SIGINT SIGTERM

# Wait for user to stop
wait