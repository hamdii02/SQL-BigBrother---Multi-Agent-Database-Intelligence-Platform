import os 
from prompts.configs import GROQ_API_BASE, GROQ_MODEL_NAME, GROQ_API_KEY, \
SPECIALIST_AGENT_ROLE, SPECIALIST_AGENT_GOAL, SPECIALIST_AGENT_BACKSTORY, \
EXPERT_AGENT_ROLE, EXPERT_AGENT_GOAL, EXPERT_AGENT_BACKSTORY, \
TITLE_AGENT_ROLE, TITLE_AGENT_GOAL, TITLE_AGENT_BACKSTORY, \
RECOMMEND_AGENT_ROLE, RECOMMEND_AGENT_GOAL, RECOMMEND_AGENT_BACKSTORY

from textwrap import dedent
from crewai import Agent
from langchain_ollama import OllamaLLM

class SQLAgents():
    def sql_specialist_agent(self, model="qwen2.5:14b"):
        return Agent(
            role=SPECIALIST_AGENT_ROLE,
            goal=SPECIALIST_AGENT_GOAL,
            backstory=dedent(SPECIALIST_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=OllamaLLM(
                model=model, 
                base_url="http://localhost:11434",
                temperature=0.1,
                format=""
            )
        )
        
    def sql_expert_agent(self, model="qwen2.5:14b"):
        return Agent(
            role=EXPERT_AGENT_ROLE,
            goal=EXPERT_AGENT_GOAL,
            backstory=dedent(EXPERT_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=OllamaLLM(model=model, base_url="http://localhost:11434")
        )

    def sql_title_agent(self, model="qwen2.5:14b"):
        return Agent(
            role=TITLE_AGENT_ROLE,
            goal=TITLE_AGENT_GOAL,
            backstory=dedent(TITLE_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=OllamaLLM(model=model, base_url="http://localhost:11434")
        )
        
    def sql_recommended_agent(self, model="qwen2.5:14b"):
        return Agent(
            role=RECOMMEND_AGENT_ROLE,
            goal=RECOMMEND_AGENT_GOAL,
            backstory=dedent(RECOMMEND_AGENT_BACKSTORY),
            allow_delegation=False,
            verbose=True,
            llm=OllamaLLM(model=model, base_url="http://localhost:11434")
        )
        