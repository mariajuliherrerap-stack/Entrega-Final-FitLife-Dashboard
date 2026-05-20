import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from Backend.database import inicializar_db
from Frontend.app_fidelizacion import AppFitLife

if __name__ == '__main__':
    inicializar_db()
    root = tk.Tk()
    app = AppFitLife(root)
    root.mainloop()