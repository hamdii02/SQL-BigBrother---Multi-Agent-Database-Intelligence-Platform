import os 
from .configs import GROQ_API_BASE, GROQ_MODEL_NAME, GROQ_API_KEY, \
SPECIALIST_AGENT_ROLE, SPECIALIST_AGENT_GOAL, SPECIALIST_AGENT_BACKSTORY, \
EXPERT_AGENT_ROLE, EXPERT_AGENT_GOAL, EXPERT_AGENT_BACKSTORY, \
TITLE_AGENT_ROLE, TITLE_AGENT_GOAL, TITLE_AGENT_BACKSTORY, \
RECOMMEND_AGENT_ROLE, RECOMMEND_AGENT_GOAL, RECOMMEND_AGENT_BACKSTORY, \
INTRO_AGENT_ROLE, INTRO_AGENT_GOAL, INTRO_AGENT_BACKSTORY, \
COORDINATOR_AGENT_ROLE, COORDINATOR_AGENT_GOAL, COORDINATOR_AGENT_BACKSTORY

# Set up API keys if available, otherwise use dummy for Ollama fallback
if GROQ_API_KEY:
    os.environ["OPENAI_API_KEY"] = GROQ_API_KEY
    if GROQ_API_BASE:
        os.environ["OPENAI_API_BASE"] = GROQ_API_BASE
    if GROQ_MODEL_NAME:
        os.environ["OPENAI_MODEL_NAME"] = GROQ_MODEL_NAME
elif not os.getenv("OPENAI_API_KEY"):
    # Set dummy key for Ollama usage - CrewAI requires this even when using local models
    os.environ["OPENAI_API_KEY"] = "sk-dummy-key-for-ollama-usage"
    
# Force Ollama configuration for CrewAI
os.environ["CREWAI_LLM_PROVIDER"] = "ollama"
os.environ["OLLAMA_BASE_URL"] = "http://localhost:11434"

from textwrap import dedent
from crewai import Agent
import requests

class SQLAgents():
    def __init__(self):
        self.default_model = self._get_best_available_model()
        
    def _get_best_available_model(self):
        """Get the best available Ollama model, fallback to a reasonable default."""
        try:
            response = requests.get("http://localhost:11434/api/tags", timeout=2)
            if response.status_code == 200:
                models = response.json().get("models", [])
                model_names = [model["name"] for model in models]
                
                # Prefer smaller, faster models for title/recommendation tasks
                preferred_order = ["qwen2.5:7b", "qwen2.5:14b", "qwen3:14b", "qwen3:30b", "gpt-oss:20b", "gemma2:9b", "llama3:8b"]
                
                for preferred in preferred_order:
                    if preferred in model_names:
                        return preferred
                        
                # If none of the preferred models, use the first available
                if model_names:
                    return model_names[0]
                    
        except Exception:
            pass
            
        # Default fallback
        return "qwen2.5:7b"
    def sql_specialist_agent(self, model=None):
        model = model or self.default_model
        return Agent(
            role=SPECIALIST_AGENT_ROLE,
            goal=SPECIALIST_AGENT_GOAL,
            backstory=dedent(SPECIALIST_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=f"ollama/{model}"
        )
        
    def sql_expert_agent(self, model=None):
        model = model or self.default_model
        return Agent(
            role=EXPERT_AGENT_ROLE,
            goal=EXPERT_AGENT_GOAL,
            backstory=dedent(EXPERT_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=f"ollama/{model}"
        )

    def sql_title_agent(self, model=None):
        model = model or self.default_model
        return Agent(
            role=TITLE_AGENT_ROLE,
            goal=TITLE_AGENT_GOAL,
            backstory=dedent(TITLE_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=f"ollama/{model}"
        )
        
    def sql_recommended_agent(self, model=None):
        model = model or self.default_model
        return Agent(
            role=RECOMMEND_AGENT_ROLE,
            goal=RECOMMEND_AGENT_GOAL,
            backstory=dedent(RECOMMEND_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=f"ollama/{model}"
        )
    
    def sql_introduction_agent(self, model=None):
        model = model or self.default_model
        return Agent(
            role=INTRO_AGENT_ROLE,
            goal=INTRO_AGENT_GOAL,
            backstory=dedent(INTRO_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=f"ollama/{model}"
        )
    
    def conversation_coordinator_agent(self, model=None):
        model = model or self.default_model
        return Agent(
            role=COORDINATOR_AGENT_ROLE,
            goal=COORDINATOR_AGENT_GOAL,
            backstory=dedent(COORDINATOR_AGENT_BACKSTORY),
            allow_delegation=True,  # Can delegate to SQL agents
            verbose=True,
            llm=f"ollama/{model}"
        )
