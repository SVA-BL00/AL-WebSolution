import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;"
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
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuarios (name, lastname, email, password, department) VALUES (?, ?, ?, ?, ?)",
            (name, lastname, email, password, department)
        )
        conn.commit()
        conn.close()
        return True
    else:
        return False
