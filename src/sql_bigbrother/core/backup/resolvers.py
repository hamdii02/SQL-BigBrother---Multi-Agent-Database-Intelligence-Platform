from crewai import Agent, Task, Crew, Process
from database import DatabaseManager
from utils import filterSchema, filterSchema_v2, markdownSQL, extractMarkdown
from agents import SQLAgents
from tasks import SQLTasks
import re

agents = SQLAgents()
tasks = SQLTasks()

class Resolvers():
    def initialize_chat(self, schema):              
        title_agent = agents.sql_title_agent()
        recommended_agent = agents.sql_recommended_agent();
        title_task = tasks.sql_title_task(title_agent, filterSchema_v2(schema))
        recommended_task = tasks.sql_recommended_task(recommended_agent, filterSchema_v2(schema))
        
        crew = Crew(
                agents=[title_agent, recommended_agent],
                tasks=[title_task, recommended_task],
                verbose=True,
            )
        
        crew.kickoff()
        title = title_task.output.raw_output
        recommends = recommended_task.output.raw_output
        return title, recommends

    def setup_sql(self, schema):
        try:
            DB = DatabaseManager("mysql")
            DB.setup(schema)       
            return True
        except Exception as e:
            print("Error: " + str(e))
            return False
    
    def generate_sql(self, requirement, schema, model, is_explain=False):
        filter = filterSchema_v2(schema)
        
        # Specialist
        specialist = agents.sql_specialist_agent_groq() if model == 'groq' else agents.sql_specialist_agent(model)
        design_task = tasks.sql_design_task(specialist, requirement, filter)

        crew = None
        query_output = None 
        explain_output = None
        
        if is_explain == True:
            # Expert
            expert = agents.sql_expert_agent_groq() if model == 'groq' else agents.sql_expert_agent(model)
            analyze_task = tasks.sql_expert_task(expert, design_task)
            
            crew = Crew(
                agents=[specialist, expert],
                tasks=[design_task, analyze_task],
                verbose=True,
                process=Process.sequential
            )
            
            crew.kickoff()
            explain_output = analyze_task.output.raw_output
        else:
            crew = Crew(
                agents=[specialist],
                tasks=[design_task],
                verbose=True,
            )
            
            crew.kickoff()
            
        query_output = extractMarkdown(design_task.output.raw_output)      
        print(query_output)      
        
        try:
            DB = DatabaseManager("mysql")
            DB.setup(schema)     
            result, columns, error = DB.query(query_output)
        
            # Return test result
            output = markdownSQL(query_output) if explain_output == None else explain_output
            execute = result
            return output, execute, columns

        except Exception as e:
            return "Error: " + str(e), 500
    