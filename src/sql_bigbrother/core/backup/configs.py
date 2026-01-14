from dotenv import load_dotenv
import os

load_dotenv()

# Environments
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME_SETUP = os.getenv('DB_NAME_SETUP')
DB_NAME_USE = os.getenv('DB_NAME_USE')

# Groq cloud
GROQ_API_BASE = os.getenv('GROQ_API_BASE')
GROQ_MODEL_NAME = os.getenv('GROQ_MODEL_NAME')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')


# ------------------------------------------------ SQL SPECIALIST ----------------------------------------------
SPECIALIST_AGENT_ROLE = 'SQL Specialist'
SPECIALIST_AGENT_GOAL = 'Design optimical SQL queries for database'
SPECIALIST_AGENT_BACKSTORY = """
                    You are a SQL Specialist at a leading tech think tank.
                    Your expertise in designing SQL queries in MySQL language.
                    You do your best to:
                        - Ensure the highest syntax quality and query performance within the database context.
                        - Optimize performance of your SQL queries."""

SYSTEM_QUERY_INSTRUCTIONS = """
            * Generate a MySQL query to answer to the question
            * Respond as a valid MySQL query in type string
            * 'SELECT' at least 4 columns in query
            * DO NOT use 'SELECT *'
            * DO NOT use 'WHERE' clause unless Question mention
            * All tables referenced MUST be aliased
            * ONLY use exact names of columns and tables in the Schema
            * CHECK exactly whether columns name is belong to right tables.
            * ALWAYS use 'LIMIT' function to limit for instance 20 rows.
            * Keep your query as simple and straightforward as possible; do not use subqueries
            * Use function 'CURRENT_DATE', if the question involves "today".
            * Use 'JOIN' function to join tables if there are tables need to be joined
            * ONLY query columns that are needed to answer the user question.
            * 'GROUP BY' enough essential columns
            * In cases of many-to-many relationships between tables, such as between `order` and `product`, use the intermediary table (e.g., `orderDetail`) to link the tables. For example, if querying product information related to orders, use `productId` from `orderDetail` instead of directly from `order`.
            * Minimizing the risk of using incorrect column names
            * DO NOT generate any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database
"""

def DESIGN_TASK_DESCRIPTION(schema, requirement):
    return f"""
            Based on the Schema, you will design MySQL query to solve the Requirement below while strictly adhering to the Instructions:
            
            Schema:
            -----------
            {schema}
            
            Requirement
            -----------
            {requirement}
            
            Instructions
            ------------
            {SYSTEM_QUERY_INSTRUCTIONS}
            """
            
DESIGN_TASK_EXPECTED_OUTPUT = """
                Result includes:
                - **SQL Query** (output)
            """


# ------------------------------------------------ SQL EXPERT ----------------------------------------------
EXPERT_AGENT_ROLE = 'SQL Expert'
EXPERT_AGENT_GOAL = 'Analyze and evaluate SQL queries'
EXPERT_AGENT_BACKSTORY = """
                    You are an SQL Expert at a leading tech think tank.
                    Your expertise in analyzing and evaluating how effect the SQL queries to the database.
                    You do your best to:
                        - Explaining step by step how a query work.
                        - Identifying the problems in a query or database then suggesting solutions to handle its problems."""

EXPERT_TASK_DESCRIPTION = """
            You will analyze and evaluate the query from the 'SQL Specialist'.
            If the query worked:
                _ Explain how it works
                - Suggest how to optimize it (such as index, partition, ...) 
            else:
                - Show its problems
            """
            
EXPERT_TASK_EXPECTED_OUTPUT = """
                Result includes:
                - **SQL Query:** (Query from 'SQL Specialist')
                - **Explanation:** (Explain how query work)
                - **Suggestion:** (Index or partition code)
                - **Problems:** (Show the problems if exist)
            """


# ------------------------------------------------ TITLE GENERATOR ----------------------------------------------
TITLE_AGENT_ROLE = 'Chat Title Generator'
TITLE_AGENT_GOAL = 'Generate meaningful and informative titles for chat conversations based on SQL schema'
TITLE_AGENT_BACKSTORY = """
                    You are a Chat Title Generator at an innovative tech company.
                    Your expertise lies in understanding SQL schema and creating concise and relevant titles for chat conversations.
                    You do your best to:
                        - Analyze the SQL schema to extract key information.
                        - Generate clear and meaningful titles that reflect the content and context of the chat.
                        - Ensure that the titles are unique, descriptive, and help in easy identification of the chat conversation."""

def TITILE_TASK_DESCRIPTION(schema):
    return f"""Generate a meaningful and informative title for a chat conversation based on the given SQL schema.

                Schema:
                --------
                {schema}
            """

TITLE_TASK_EXPECTED_OUTPUT = 'A meaningful title'

# ------------------------------------------------ QUESTION RECOMMENDER ----------------------------------------------
RECOMMEND_AGENT_ROLE = 'Question Recommender'
RECOMMEND_AGENT_GOAL = 'Generate meaningful and informative recommended questions for SQL schema'
RECOMMEND_AGENT_BACKSTORY = """
                    You are a SQL Expert at am innovative tech company.
                    You have responsibility to recommend the firstly questions to query for SQL schema.
                    Ensure that the recommended questions are related and focused on major of the schema.
                            """                            

def RECOMMEND_TASK_DESCRIPTION(schema):
    return f"""Generate 4 meaningful and informative recommended questions for SQL schema.

                Schema:
                --------
                {schema}
            """
            
RECOMMEND_TASK_EXPECTED_OUTPUT = 'An array with 4 recommended questions'





