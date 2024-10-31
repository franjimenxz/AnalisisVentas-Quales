
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-6CVS8GM\\SQLEXPRESS;'
    'DATABASE=DW_DataShop;'
    'Trusted_Connection=yes;'
)

def ejecutar_sp():
    try:
        conn.execute("EXEC sp_carga_Dim_Tienda")
        conn.commit()
        print("Stored Procedure sp_carga_Dim_Tienda ejecutado correctamente.")
    except pyodbc.Error as e:
        print(f"Error ejecutando sp_carga_Dim_Tienda: {e}")
    finally:
        conn.close()

ejecutar_sp()
