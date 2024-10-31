import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-6CVS8GM\\SQLEXPRESS;'
    'DATABASE=DW_DataShop;'
    'Trusted_Connection=yes;'
)

def cargar_stg_producto():
    datos = pd.read_csv('productos.csv')
    placeholders = ', '.join(['?'] * len(datos.columns))
    query = f"INSERT INTO Stg_Dim_Producto VALUES ({placeholders})"
    
    cursor = conn.cursor()  # Crear un cursor
    cursor.executemany(query, datos.values.tolist())
    conn.commit()
    cursor.close()  # Cerrar el cursor
    print("Datos cargados en Stg_Dim_Producto exitosamente.")
    conn.close()

cargar_stg_producto()
