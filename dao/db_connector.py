import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

conn = psycopg2.connect(database = DB_NAME,
                        host = DB_HOST,
                        port = DB_PORT,
                        user = DB_USER,
                        password = DB_PASSWORD)

cursor = conn.cursor()

def get_db_status():
    cursor.execute("SELECT * FROM status WHERE id=1")
    return cursor.fetchone()

def execute_query(query):
    cursor.execute(query)
    conn.commit()