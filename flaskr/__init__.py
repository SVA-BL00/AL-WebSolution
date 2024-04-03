from flask import Flask
import pyodbc
from dotenv import load_dotenv
import os
import secrets 

def create_app():
    app = Flask(__name__)
    app._static_folder = 'static'
    load_dotenv()

    app.config['SECRET_KEY'] = secrets.token_hex(16)

    # Database config
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

    @app.route('/')
    def index():
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Employees")
            count = cursor.fetchone()[0]
            conn.close()
            return f"Total records in database: {count}"
        else:
            return "Failed to connect to database."

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
