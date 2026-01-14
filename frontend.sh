#!/bin/bash

# Frontend Management Script for SQL BigBrother

FRONTEND_DIR="src/sql_bigbrother/core/frontend"

case "$1" in
    "install")
        echo "📦 Installing frontend dependencies..."
        cd "$FRONTEND_DIR" && npm install
        ;;
    "dev"|"start")
        echo "🚀 Starting React frontend development server..."
        cd "$FRONTEND_DIR" && npm run dev
        ;;
    "build")
        echo "🏗️  Building frontend for production..."
        cd "$FRONTEND_DIR" && npm run build
        ;;
    "preview")
        echo "👀 Starting production preview server..."
        cd "$FRONTEND_DIR" && npm run preview
        ;;
    *)
        echo "SQL BigBrother Frontend Manager"
        echo ""
        echo "Usage: $0 [command]"
        echo ""
        echo "Commands:"
        echo "  install  - Install frontend dependencies"
        echo "  dev      - Start development server"
        echo "  start    - Start development server (alias for dev)"
        echo "  build    - Build for production"
        echo "  preview  - Preview production build"
        echo ""
        echo "Examples:"
        echo "  $0 install    # Install dependencies"
        echo "  $0 dev        # Start development at http://localhost:5173"
        ;;
esac