import sqlite3
from sqlite3 import Error

DB_FILE = "./db/inventary.db"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        
        print(f"Conectado a la base de datos: {DB_FILE}")
        return conn
    except Error as e:
        print(e)

    return conn