# 🏋️‍♀️ FitLife Fideliza - Ecosistema Integral & Business Intelligence

Este repositorio contiene la entrega final para la **Clase 12: Dashboard (Proyecto Final)**. Es una solución End-to-End diseñada para gestionar, asignar y analizar el retorno de inversión del programa de recompensas y categorías de FitLife.

## 🏗️ Arquitectura del Proyecto
El ecosistema se compone de las siguientes capas tecnológicas:

1. **Frontend (`app_fidelizacion.py`):** GUI desarrollada en Tkinter para el registro ágil de compras, con control de excepciones y UX optimizada.
2. **Backend (`mercadeo.py` & `database.py`):** Lógica que asigna automáticamente el porcentaje de bono según la categoría (Bronce, Plata, Oro).
3. **Base de Datos (`fitlife_fidelizacion.db`):** Repositorio SQLite que almacena el historial de transacciones y beneficios otorgados.
4. **Inteligencia de Negocios (`FitLife_MVP_Final.pbix`):** Panel gerencial en Power BI estructurado con un **Modelo Estrella**. Implementa Inteligencia de Tiempo y medidas DAX para evaluar métricas como el Porcentaje de Bono vs. Compra y el crecimiento mensual de retención.

## 👥 Integrantes del Grupo
* **Juliana** (Líder de Proyecto)
* **Mariana Carmona**

## 🚀 Instrucciones de Ejecución (Python)
1. Instalar dependencias necesarias: `pip install Pillow`
2. Ejecutar el orquestador principal: `python main.py`

## ⚠️ Nota Técnica para Evaluación (Power BI)
El ecosistema backend en Python (`main.py` y `database.py`) ya está configurado con rutas relativas (`os.path.dirname`) y funcionará automáticamente al clonar el repositorio. 

Sin embargo, dado que Power BI almacena rutas absolutas en Power Query, al abrir el archivo `.pbix` por primera vez es necesario actualizar la ruta del origen de datos para que las gráficas y medidas DAX se conecten:
1. Abrir Power BI Desktop.
2. Ir a **Inicio > Transformar datos > Configuración de origen de datos**.
3. Seleccionar la ruta actual y hacer clic en **Cambiar origen**.
4. Buscar y seleccionar el archivo `fitlife_fidelizacion.db` incluido en la carpeta de este repositorio.
5. Cerrar y presionar **Actualizar**.

---
*Desarrollado para el Tercer Corte - Universidad de La Sabana (2026).*
