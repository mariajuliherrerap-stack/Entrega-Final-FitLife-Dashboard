import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from Backend.mercadeo import RegistroFidelizacion

class AppFitLife:
    def __init__(self, root):
        self.root = root
        self.root.title("FitLife - Sistema de Fidelización")
        self.root.geometry("400x550")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)
        self.construir_gui()

    def construir_gui(self):
        # 1. Logo
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(base_dir, "logo.png")
            img = Image.open(logo_path).convert("RGB").resize((120, 120), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo_img, bg="#f4f4f4").pack(pady=10)
        except Exception:
            tk.Label(self.root, text="⭐ FITLIFE LOYALTY", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=20)

        # 2. Formulario
        tk.Label(self.root, text="Registro de Compras y Bonos", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=5)

        tk.Label(self.root, text="Nombre del Cliente:", bg="#f4f4f4", font=("Arial", 10)).pack(pady=2)
        self.entry_cliente = tk.Entry(self.root, font=("Arial", 11), justify="center")
        self.entry_cliente.pack(pady=5)

        tk.Label(self.root, text="Categoría del Cliente:", bg="#f4f4f4", font=("Arial", 10)).pack(pady=2)
        self.cmb_categoria = ttk.Combobox(self.root, values=["Bronce", "Plata", "Oro"], state="readonly")
        self.cmb_categoria.pack(pady=5)

        tk.Label(self.root, text="Monto de la Compra ($):", bg="#f4f4f4", font=("Arial", 10)).pack(pady=2)
        self.entry_compras = tk.Entry(self.root, font=("Arial", 11), justify="center")
        self.entry_compras.pack(pady=5)

        # 3. Botones
        tk.Button(self.root, text="⭐ Calcular y Registrar Bono", bg="#2e7d32", fg="white", font=("Arial", 11, "bold"), cursor="hand2", command=self.registrar).pack(pady=15, fill="x", padx=50)
        tk.Button(self.root, text="🧹 Limpiar", bg="#d32f2f", fg="white", cursor="hand2", command=self.limpiar).pack(pady=5, fill="x", padx=120)

    def registrar(self):
        cliente = self.entry_cliente.get().strip()
        categoria = self.cmb_categoria.get()
        compras_str = self.entry_compras.get().strip()

        try:
            if not cliente or not categoria or not compras_str:
                raise ValueError("Debe completar todos los campos del formulario.")
            
            try:
                compras = float(compras_str)
            except ValueError:
                raise ValueError("El monto de compras debe ser numérico.")

            if compras <= 0:
                raise ValueError("El monto de la compra debe ser mayor a 0.")

            # Lógica de Negocio: Cálculo de bonos
            porcentajes = {"Bronce": 0.0, "Plata": 0.05, "Oro": 0.10}
            bono = compras * porcentajes[categoria]

            RegistroFidelizacion.guardar_registro(cliente, categoria, compras, bono)
            messagebox.showinfo("Éxito", f"Compra registrada.\nCliente: {cliente}\nCategoría: {categoria}\nBono Asignado: ${bono:,.2f}")
            self.limpiar()

        except ValueError as ve:
            messagebox.showwarning("Advertencia", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Fallo en el sistema:\n{e}")

    def limpiar(self):
        self.entry_cliente.delete(0, tk.END)
        self.cmb_categoria.set('')
        self.entry_compras.delete(0, tk.END)