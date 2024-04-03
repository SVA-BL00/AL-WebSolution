import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER=ODBC Driver 18 for SQL Server;"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    

def add_user(name, lastname, email, password, department):
    conn = get_db_connection()
    if conn:
        try:
            # Retrieve the next available ID from the database
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(id) FROM users")
            result = cursor.fetchone()
            next_id = result[0] + 1 if result[0] is not None else 1

            # Insert the user with the next available ID
            cursor.execute(
                "INSERT INTO Usuarios (EmployeeID, FirstName, LastName, Department, Email, PassW) VALUES (?, ?, ?, ?, ?)",
                (next_id, name, lastname, department, email, password)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
        finally:
            conn.close()
    else:
        return False
