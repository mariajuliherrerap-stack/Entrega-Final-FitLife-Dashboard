import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "fitlife_fidelizacion.db")

def inicializar_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lealtad (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT,
                categoria TEXT,
                compras REAL,
                bono REAL
            )
        ''')
        conn.commit()