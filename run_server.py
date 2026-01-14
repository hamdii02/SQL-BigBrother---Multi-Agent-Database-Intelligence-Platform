#!/usr/bin/env python3
"""
SQL BigBrother FastAPI server startup script.

This script starts the FastAPI server integrated with Kedro pipelines and local Ollama AI models.
It automatically handles port conflicts by offering to kill existing processes or use alternative ports.

Features:
- Port conflict detection and resolution
- Ollama service health checking  
- Automatic model detection
- Interactive port conflict resolution
- Environment setup for local AI processing
"""

import os
import sys
import time
import socket
import subprocess
import requests
import uvicorn
import json
import re
from pathlib import Path
from sql_bigbrother.core.api.main import app

def check_ollama_service():
    """Check if Ollama service is running and has models available."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            if models:
                print(f"Ollama service is running with {len(models)} models available:")
                for model in models[:3]:  # Show first 3 models
                    print(f"   - {model['name']}")
                if len(models) > 3:
                    print(f"   ... and {len(models) - 3} more")
                return True
            else:
                print("⚠️  Ollama service is running but no models are installed.")
                print("   Install models with: ollama pull qwen2.5:7b")
                return False
    except requests.exceptions.RequestException:
        print("Ollama service is not running.")
        print("Start it with: ollama serve")
        return False

def is_port_in_use(port):
    """Check if a port is currently in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def get_processes_on_port(port):
    """Get list of processes using a specific port."""
    try:
        result = subprocess.run(['lsof', '-ti', f':{port}'], 
                              capture_output=True, text=True, check=False)
        if result.returncode == 0 and result.stdout.strip():
            return [pid.strip() for pid in result.stdout.strip().split('\n') if pid.strip()]
        return []
    except Exception:
        return []

def kill_processes_on_port(port):
    """Kill all processes using a specific port."""
    pids = get_processes_on_port(port)
    if pids:
        print(f"🔄 Found {len(pids)} process(es) using port {port}")
        for pid in pids:
            try:
                subprocess.run(['kill', '-9', pid], check=False)
                print(f"   ✅ Killed process {pid}")
            except Exception as e:
                print(f"   ❌ Failed to kill process {pid}: {e}")
        
        # Wait a moment for processes to terminate
        time.sleep(2)
        
        # Verify port is now free
        if is_port_in_use(port):
            print(f"   ⚠️  Port {port} still in use after killing processes")
            return False
        else:
            print(f"   ✅ Port {port} is now free")
            return True
    return True

def find_available_port(start_port, max_attempts=10):
    """Find an available port starting from start_port."""
    for port in range(start_port, start_port + max_attempts):
        if not is_port_in_use(port):
            return port
    return None

def handle_port_conflict(port, service_name):
    """Handle port conflicts by offering solutions."""
    print(f"⚠️  Port {port} is already in use ({service_name})")
    
    pids = get_processes_on_port(port)
    if pids:
        print(f"   Processes using port {port}: {', '.join(pids)}")
    
    print(f"\nOptions:")
    print(f"1. Kill existing processes on port {port} (recommended)")
    print(f"2. Use a different port")
    print(f"3. Exit and handle manually")
    
    while True:
        try:
            choice = input("Choose option (1/2/3): ").strip()
            
            if choice == '1':
                if kill_processes_on_port(port):
                    return port
                else:
                    print("Failed to free the port. Trying option 2...")
                    choice = '2'
            
            if choice == '2':
                alt_port = find_available_port(port + 1)
                if alt_port:
                    print(f"Using alternative port {alt_port}")
                    return alt_port
                else:
                    print("No available ports found")
                    return None
            
            if choice == '3':
                print("👋 Exiting. Please handle port conflicts manually.")
                return None
                
            print("Invalid choice. Please enter 1, 2, or 3.")
            
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            return None

def find_frontend_ports():
    """Find all ports where frontend (Vite/Node) processes are running."""
    frontend_ports = []
    try:
        # Look for Vite processes
        result = subprocess.run(['pgrep', '-f', 'vite'], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid.strip():
                    # Get port information for each Vite process
                    try:
                        lsof_result = subprocess.run(['lsof', '-Pan', '-p', pid.strip()], 
                                                   capture_output=True, text=True, check=False)
                        if lsof_result.returncode == 0:
                            # Extract port numbers from lsof output
                            port_matches = re.findall(r':(\d{4,5})->.*LISTEN', lsof_result.stdout)
                            for port in port_matches:
                                if 5000 <= int(port) <= 6000:  # Typical Vite port range
                                    frontend_ports.append(int(port))
                    except Exception:
                        continue
        
        # Also check common frontend ports directly
        common_frontend_ports = [5173, 5174, 5175, 5176, 3000, 3001]
        for port in common_frontend_ports:
            if is_port_in_use(port):
                # Check if it's actually a frontend service
                try:
                    response = requests.get(f'http://localhost:{port}/', timeout=2)
                    if response.status_code == 200 and ('vite' in response.text.lower() or 
                                                       'react' in response.text.lower() or
                                                       'vue' in response.text.lower()):
                        if port not in frontend_ports:
                            frontend_ports.append(port)
                except:
                    pass
    
    except Exception as e:
        print(f"Error detecting frontend ports: {e}")
    
    return sorted(set(frontend_ports))

def start_frontend_server():
    """Start the frontend development server."""
    frontend_dir = Path(__file__).parent / "src" / "sql_bigbrother" / "core" / "frontend"
    
    if not frontend_dir.exists():
        print(f"❌ Frontend directory not found: {frontend_dir}")
        return None
    
    try:
        print("🔄 Starting frontend server...")
        process = subprocess.Popen(
            ['npm', 'run', 'dev'],
            cwd=str(frontend_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a moment and check if process started successfully
        time.sleep(3)
        if process.poll() is None:  # Process is still running
            print("✅ Frontend server started successfully")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Frontend server failed to start: {stderr}")
            return None
    except Exception as e:
        print(f"❌ Error starting frontend server: {e}")
        return None

def start_auth_server():
    """Start the Node.js auth server."""
    auth_dir = Path(__file__).parent / "src" / "sql_bigbrother" / "core" / "auth"
    
    if not auth_dir.exists():
        print(f"❌ Auth directory not found: {auth_dir}")
        return None
    
    try:
        print("🔄 Starting auth server...")
        process = subprocess.Popen(
            ['node', 'server.js'],
            cwd=str(auth_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a moment and check if process started successfully
        time.sleep(2)
        if process.poll() is None:  # Process is still running
            print("✅ Auth server started successfully")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Auth server failed to start: {stderr}")
            return None
    except Exception as e:
        print(f"❌ Error starting auth server: {e}")
        return None

def check_service_health(port, service_name, endpoint="/"):
    """Check if a service is healthy and responding."""
    try:
        response = requests.get(f"http://localhost:{port}{endpoint}", timeout=3)
        return response.status_code == 200
    except:
        return False

def kill_all_server_processes():
    """Kill all SQL BigBrother related processes."""
    processes_killed = []
    
    # Kill FastAPI/uvicorn processes
    try:
        result = subprocess.run(['pgrep', '-f', 'uvicorn|run_server'], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            pids = [pid.strip() for pid in result.stdout.strip().split('\n') if pid.strip()]
            for pid in pids:
                try:
                    subprocess.run(['kill', '-9', pid], check=False)
                    processes_killed.append(f"FastAPI (PID: {pid})")
                except Exception:
                    pass
    except Exception:
        pass
    
    # Kill Vite processes
    try:
        result = subprocess.run(['pgrep', '-f', 'vite'], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            pids = [pid.strip() for pid in result.stdout.strip().split('\n') if pid.strip()]
            for pid in pids:
                try:
                    subprocess.run(['kill', '-9', pid], check=False)
                    processes_killed.append(f"Vite (PID: {pid})")
                except Exception:
                    pass
    except Exception:
        pass
    
    # Kill Node.js auth service
    try:
        result = subprocess.run(['pgrep', '-f', 'node.*server.js'], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            pids = [pid.strip() for pid in result.stdout.strip().split('\n') if pid.strip()]
            for pid in pids:
                try:
                    subprocess.run(['kill', '-9', pid], check=False)
                    processes_killed.append(f"Auth Service (PID: {pid})")
                except Exception:
                    pass
    except Exception:
        pass
    
    if processes_killed:
        print(f"🔄 Killed previous processes: {', '.join(processes_killed)}")
        time.sleep(2)  # Wait for processes to terminate
    
    return len(processes_killed)

def setup_environment():
    """Set up environment variables for local AI processing."""
    # Set dummy OpenAI key for CrewAI compatibility when using Ollama
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("GROQ_API_KEY"):
        os.environ["OPENAI_API_KEY"] = "ollama-local-dummy-key"
        print("🔧 Using local Ollama models (no external API keys required)")

if __name__ == "__main__":
    print("🚀 Starting SQL BigBrother Complete System...")
    
    # Store process references
    frontend_process = None
    auth_process = None
    
    # Check for existing processes and offer to clean up
    frontend_ports = find_frontend_ports()
    if frontend_ports:
        print(f"🔍 Found frontend running on ports: {', '.join(map(str, frontend_ports))}")
    
    # Check for existing server processes
    existing_processes = []
    for port in [8000, 8001, 2405] + frontend_ports:
        if is_port_in_use(port):
            pids = get_processes_on_port(port)
            if pids:
                existing_processes.extend(pids)
    
    if existing_processes:
        print(f"\n⚠️  Found {len(set(existing_processes))} existing server processes")
        print("Options:")
        print("1. Kill all existing processes and restart fresh (recommended)")
        print("2. Continue with existing services")
        print("3. Exit")
        
        try:
            choice = input("Choose option (1/2/3): ").strip()
            if choice == '1':
                killed_count = kill_all_server_processes()
                print(f"✅ Cleaned up {killed_count} processes")
            elif choice == '3':
                print("👋 Exiting...")
                sys.exit(0)
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            sys.exit(0)
    
    # Check prerequisites
    setup_environment()
    
    # Start supporting services
    print("\n🔄 Starting supporting services...")
    
    # Start auth service if not running
    if not is_port_in_use(2405):
        auth_process = start_auth_server()
        time.sleep(2)  # Wait for auth service to initialize
    else:
        print("✅ Auth service already running on port 2405")
    
    # Start frontend if not running  
    frontend_running = False
    for port in [5173, 5174, 5175, 5176]:
        if is_port_in_use(port) and check_service_health(port, "Frontend"):
            print(f"✅ Frontend already running on port {port}")
            frontend_running = True
            break
    
    if not frontend_running:
        frontend_process = start_frontend_server()
        time.sleep(3)  # Wait for frontend to initialize
    
    # Check and handle port conflicts
    target_port = 8000
    
    if is_port_in_use(target_port):
        result_port = handle_port_conflict(target_port, "FastAPI Server")
        if result_port is None:
            sys.exit(1)
        target_port = result_port
    else:
        print(f"✅ Port {target_port} is available")
    
    if not check_ollama_service():
        print("\n💡 To use external APIs instead of local Ollama, set environment variables:")
        print("   export GROQ_API_KEY='your_groq_api_key'")
        print("   export OPENAI_API_KEY='your_openai_api_key'")
        
        try:
            response = input("\nContinue anyway? (y/N): ")
            if response.lower() != 'y':
                sys.exit(1)
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            sys.exit(1)
    
    # Show frontend information if available
    current_frontend_ports = find_frontend_ports()
    
    print(f"\n📊 SQL BigBrother Services:")
    print(f"   • FastAPI Backend: http://localhost:{target_port}")
    print(f"   • API Docs: http://localhost:{target_port}/docs")
    print(f"   • Health Check: http://localhost:{target_port}/health")
    
    if current_frontend_ports:
        print(f"   • Frontend: http://localhost:{current_frontend_ports[0]}")
        if len(current_frontend_ports) > 1:
            print(f"   • Additional Frontend Ports: {', '.join(map(str, current_frontend_ports[1:]))}")
    else:
        print(f"   • Frontend: Not detected (start with 'npm run dev' in frontend directory)")
    
    auth_port = 2405
    if is_port_in_use(auth_port):
        print(f"   • Auth Service: http://localhost:{auth_port}")
    else:
        print(f"   • Auth Service: Not running (start with 'node server.js' in auth directory)")
    
    print("\n🔄 Starting FastAPI server with auto-reload enabled...\n")
    
    try:
        # Final health check before starting FastAPI
        print("🔍 Final service health check...")
        
        if check_service_health(2405, "Auth Service", "/api/v1/health"):
            print("   ✅ Auth service is healthy")
        elif is_port_in_use(2405):
            print("   ⚠️  Auth service is running but may not be ready")
        else:
            print("   ❌ Auth service is not running")
        
        # Check frontend
        frontend_healthy = False
        for port in [5173, 5174, 5175, 5176]:
            if is_port_in_use(port):
                if check_service_health(port, "Frontend"):
                    print(f"   ✅ Frontend is healthy on port {port}")
                    frontend_healthy = True
                    break
                else:
                    print(f"   ⚠️  Frontend on port {port} may not be ready")
        
        if not frontend_healthy:
            print("   ❌ Frontend is not running or not healthy")
        
        print("   ✅ Starting FastAPI backend...")
        
        uvicorn.run(
            "sql_bigbrother.core.api.main:app", 
            host="0.0.0.0", 
            port=target_port, 
            reload=True,
            reload_dirs=["src"],
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Shutting down all services...")
        
        # Clean shutdown of started processes
        if frontend_process and frontend_process.poll() is None:
            print("   🔄 Stopping frontend server...")
            frontend_process.terminate()
            try:
                frontend_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                frontend_process.kill()
        
        if auth_process and auth_process.poll() is None:
            print("   🔄 Stopping auth server...")
            auth_process.terminate()
            try:
                auth_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                auth_process.kill()
        
        print("   ✅ All services stopped")
        
    except Exception as e:
        if "Address already in use" in str(e):
            print(f"\n❌ Port {target_port} became unavailable during startup")
            print("   This can happen if another process started using the port")
            print("   Please try running the server again")
        else:
            print(f"\n❌ Server failed to start: {e}")
        
        # Clean up on error
        if frontend_process and frontend_process.poll() is None:
            frontend_process.terminate()
        if auth_process and auth_process.poll() is None:
            auth_process.terminate()
            
        sys.exit(1)