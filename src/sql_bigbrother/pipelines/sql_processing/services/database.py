import mysql.connector
from mysql.connector import Error
import os
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Database manager for MySQL operations with Kedro integration."""
    
    def __init__(self, db_type: str = "mysql", **config):
        self.type = db_type
        # Set default values for missing environment variables
        self.config = config or {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', '3306')),
            'user': os.getenv('DB_USER', 'root'),  # Default to 'root'
            'password': os.getenv('DB_PASSWORD', ''),  # Default to empty password
            'setup_database': os.getenv('DB_NAME_SETUP', 'sys'),
            'use_database': os.getenv('DB_NAME_USE', 'sql_bigbrother_temp')  # Default database name
        }
        
        # Validate required configuration
        if not self.config['user']:
            logger.warning("DB_USER not set, using default: root")
            self.config['user'] = 'root'
        if self.config['password'] is None:
            logger.warning("DB_PASSWORD not set, using empty password")
            self.config['password'] = ''
        if not self.config['use_database']:
            self.config['use_database'] = 'sql_bigbrother_temp'

    def execute(self, ssql: str) -> Dict[str, Any]:
        """Execute SQL query and return results."""
        connection = None
        try:
            logger.info(f"Connecting to database: {self.config['use_database']} on {self.config['host']}:{self.config['port']}")
            connection = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['use_database'],
                port=self.config['port']
            )

            if connection.is_connected():
                cursor = connection.cursor()
                logger.info(f"Executing query: {ssql[:100]}...")
                cursor.execute(ssql)
                
                rows = cursor.fetchall()
                columns = [i[0] for i in cursor.description] if cursor.description else []
                
                logger.info(f"Query executed successfully, returned {len(rows)} rows")
                return {"rows": rows, "columns": columns}
                
        except mysql.connector.Error as e:
            logger.error(f"MySQL Error: {e}")
            print(f"MySQL Error: {e}")
            return {"rows": [], "columns": []}
        except Exception as e:
            logger.error(f"Execution Error: {e}")
            print(f"Execution Error: {e}")
            return {"rows": [], "columns": []}
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    def setup(self, schema: str) -> bool:
        """Setup database with provided schema."""
        connection = None
        try:
            logger.info(f"Setting up database: {self.config['use_database']}")
            connection = mysql.connector.connect(
                host=self.config['host'],
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['setup_database'],
                autocommit=False,
                port=self.config['port']
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
               
                # Create the database
                cursor.execute(f"DROP DATABASE IF EXISTS {self.config['use_database']};")
                cursor.execute(f"CREATE DATABASE {self.config['use_database']};")
                cursor.execute(f"USE {self.config['use_database']};")
                
                # Execute schema creation
                lines = schema.split(");")
                for i in range(0, len(lines) - 1):
                    table_sql = lines[i].strip() + ");"
                    if table_sql.strip():  # Skip empty lines
                        try:
                            cursor.execute(table_sql)
                            logger.info(f"Created table {i+1}")
                        except mysql.connector.Error as table_error:
                            logger.error(f"Error creating table {i+1}: {table_error}")
                            logger.error(f"SQL: {table_sql}")
                            return False
                    
                connection.commit()
                logger.info("Database setup completed successfully")
                print("Setup Database successfully")
                return True

        except mysql.connector.Error as e:
            logger.error(f"MySQL Setup Error: {e}")
            print(f"MySQL Setup Error: {e}")
            return False
        except Exception as e:
            logger.error(f"Setup Error: {e}")
            print(f"Setup Error: {e}")
            return False
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    



