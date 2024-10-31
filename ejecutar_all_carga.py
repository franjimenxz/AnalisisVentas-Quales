import pandas as pd
import pyodbc

# Conexión a SQL Server
conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-6CVS8GM\\SQLEXPRESS;'
        'DATABASE=DW_DataShop;'
        'Trusted_Connection=yes;'
    )


# Función para cargar datos en tablas Stage
def cargar_csv_en_stage(archivo_csv, tabla_sql):
    datos = pd.read_csv(archivo_csv)
    for _, row in datos.iterrows():
        placeholders = ', '.join(['?'] * len(row))
        query = f"INSERT INTO {tabla_sql} VALUES ({placeholders})"
        conn.execute(query, tuple(row))
    conn.commit()
    print(f"Datos cargados en {tabla_sql} exitosamente.")

# Cargar datos desde CSV
cargar_csv_en_stage('productos.csv', 'Stg_Dim_Producto')
cargar_csv_en_stage('clientes.csv', 'Stg_Dim_Cliente')
cargar_csv_en_stage('tiendas.csv', 'Stg_Dim_Tienda')
cargar_csv_en_stage('ventas.csv', 'Stg_Fact_Ventas')
