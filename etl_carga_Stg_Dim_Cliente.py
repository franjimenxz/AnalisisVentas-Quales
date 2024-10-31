import pandas as pd
import pyodbc

def cargar_stg_cliente():
    # Conexión a la base de datos
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=DESKTOP-6CVS8GM\\SQLExpress;'
                          'DATABASE=DW_DataShop;'
                          'Trusted_Connection=yes;')
    
    # Cargar datos desde el archivo CSV
    datos = pd.read_csv('clientes.csv')
    
    # Preparar los placeholders para la consulta
    placeholders = ', '.join(['?'] * len(datos.columns))
    query = f"INSERT INTO Stg_Dim_Cliente VALUES ({placeholders})"
    
    # Crear un cursor y ejecutar la consulta
    cursor = conn.cursor()
    cursor.executemany(query, datos.values.tolist())
    
    conn.commit()
    cursor.close()  # Asegúrate de cerrar el cursor
    conn.close()  # Cerrar la conexión
    print("Datos cargados en Stg_Dim_Cliente exitosamente.")

cargar_stg_cliente()
