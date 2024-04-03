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
            f"UID={os.getenv('DB_USERNAME')};"
            f"PWD={os.getenv('DB_PASSWORD')}"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None