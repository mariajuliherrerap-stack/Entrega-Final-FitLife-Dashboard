import sqlite3
from Backend.database import DB_NAME

class RegistroFidelizacion:
    @staticmethod
    def guardar_registro(cliente, categoria, compras, bono):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO lealtad (cliente, categoria, compras, bono)
                VALUES (?, ?, ?, ?)
            ''', (cliente, categoria, compras, bono))
            conn.commit()