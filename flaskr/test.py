import pyodbc

# Replace with your connection details
server = 'augmented-labs.database.windows.net'
database = 'Augmented Labs'
username = 'adminALsql'
password = 'cherryCola19'

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print("Successfully connected to the database.")
    print("Server version:", row[0])
except Exception as e:
    print("Failed to connect to the database:", e)

