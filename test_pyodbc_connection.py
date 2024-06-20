import pyodbc
import urllib.parse
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read environment variables
server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USER')
password = os.getenv('SQL_PASSWORD')
driver = os.getenv('SQL_DRIVER', 'ODBC Driver 18 for SQL Server')
encrypt = os.getenv('SQL_ENCRYPT', 'yes')
trust_cert = os.getenv('SQL_TRUST_SERVER_CERTIFICATE', 'no')
timeout = os.getenv('SQL_CONNECTION_TIMEOUT', '30')

# Construct the connection string
connection_string = (
    f"DRIVER={driver};"
    f"SERVER={server},1433;"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt={encrypt};"
    f"TrustServerCertificate={trust_cert};"
    f"Connection Timeout={timeout};"
)

try:
    # Connect to the database
    print("Attempting to connect to the database using pyodbc...")
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
    conn.close()
except pyodbc.Error as ex:
    print(f"Connection failed: {ex}")
