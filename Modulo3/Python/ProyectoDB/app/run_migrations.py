import sqlite3
from sqlite3 import Error
import sys
import os

DB_FILE = "./db/inventary.db"

def run_migrations(migration_name):
    migration_path = os.path.join("./migrations", migration_name)
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        with open(migration_path) as f:
            cursor.executescript(f.read())
        print(f"Migración '{migration_name}' aplicada.")
        conn.close()
    except Error as e:
        print(f"Error al ejecutar migraciones: {e}")
    except FileNotFoundError:
        print(f"No se encontró el archivo de migración: {migration_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python run_migrations.py <nombre_migracion.sql>")
    else:
        migration_name = sys.argv[1]
        run_migrations(migration_name)
