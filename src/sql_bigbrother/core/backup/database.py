import mysql.connector
from mysql.connector import Error
from configs import DB_NAME_SETUP, DB_NAME_USE, DB_PASSWORD, DB_USER

class DatabaseManager:
    type = "mysql"

    def __init__(self, type):
        self.type = type

    def query(self, ssql):
        actions = {
            'mysql': queryMySQL_v2(ssql)
        }
        return actions.get(self.type)
    
    def setup(self, schema):
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
                    print(str(i) + ". " + lines[i].strip() + ");")
                    cursor.execute(lines[i].strip() + ");")
                    i = i + 1
                    
                print("Setup Database successfully")

        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                connection.commit()
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

def queryMySQL_v2(ssql):
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
            result = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            error = None
            print("Query successfully")

            return result, columns, error

    except Error as e:
        print(f"Error: {e}")
        error = str(e)
        return None, None, error 
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



