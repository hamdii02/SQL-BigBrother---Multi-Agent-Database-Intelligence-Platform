import mysql.connector
from mysql.connector import Error
from prompts.configs import DB_NAME_SETUP, DB_NAME_USE, DB_PASSWORD, DB_USER

class DatabaseManager:
    type = "mysql"

    def __init__(self, type):
        self.type = type

    async def execute(self, ssql):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user= DB_USER,
                password= DB_PASSWORD,
                database= DB_NAME_USE,
                port=3306
            )

            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(ssql)
                
                rows = cursor.fetchall()
                columns = [i[0] for i in cursor.description]
                
                for row in rows:
                    for value in row:
                        print(type(value))
                        print(str(value))
                
                print("Query successfully")
                return {"rows": rows, "columns": columns}
        except Exception as e:
            print(f"Error: {e}")
            return {"rows": [], "columns": []}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    
    async def setup(self, schema):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user= DB_USER,
                password= DB_PASSWORD,
                database= DB_NAME_SETUP,
                autocommit= False,
                port=3306
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
               
                cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME_USE};")
                cursor.execute(f"CREATE DATABASE {DB_NAME_USE};")
                cursor.execute(f"USE {DB_NAME_USE};")
                
                lines = schema.split(");")
                # print(lines)
                for i in range(0, len(lines) - 1):
                    # print(str(i) + ". " + lines[i].strip() + ");")
                    cursor.execute(lines[i].strip() + ");")
                    i = i + 1
                    
                print("Setup Database successfully")
                return True

        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            if connection.is_connected():
                connection.commit()
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    



