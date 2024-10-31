import pyodbc

# Conexión a SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-6CVS8GM\\SQLEXPRESS;'
    'DATABASE=DW_DataShop;'
    'Trusted_Connection=yes;'
)

# Ejecutar el procedimiento para llenar Dim_Tiempo
conn.execute("EXEC sp_Genera_Dim_Tiempo @anio = 2023;")  # Cambia 2023 por el año deseado
print("Stored Procedure sp_Genera_Dim_Tiempo ejecutado correctamente.")

# Lista de Stored Procedures a ejecutar
procedimientos = [
    "sp_carga_Int_Dim_Producto",
    "sp_carga_Int_Dim_Cliente",
    "sp_carga_Int_Dim_Tienda",
    "sp_carga_Int_Fact_Ventas",
    "sp_carga_Dim_Producto",
    "sp_carga_Dim_Cliente",
    "sp_carga_Dim_Tienda",
    "sp_carga_Fact_Ventas"
]

# Ejecutar los Stored Procedures
for sp in procedimientos:
    try:
        conn.execute(f"EXEC {sp}")
        print(f"Stored Procedure {sp} ejecutado correctamente.")
    except Exception as e:
        print(f"Error al ejecutar {sp}: {e}")

conn.commit()
conn.close()
