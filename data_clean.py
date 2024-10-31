import pandas as pd

# Cargar los datos desde el CSV
df_clientes = pd.read_csv('clientes.csv')
df_productos = pd.read_csv('productos.csv')
df_tiendas = pd.read_csv('tiendas.csv')
df_ventas = pd.read_csv('ventas.csv')

# Limpieza de datos de clientes
df_clientes.dropna(subset=['Nombre_Cliente', 'Edad', 'Genero'], inplace=True)  # Eliminar filas con valores nulos en campos clave
df_clientes['Edad'] = df_clientes['Edad'].fillna(df_clientes['Edad'].median())  # Rellenar edades nulas con la mediana
df_clientes['Genero'] = df_clientes['Genero'].str.capitalize()  # Normalizar género (Ej. "femenino" a "Femenino")

# Limpieza de datos de productos
df_productos.dropna(subset=['Nombre_Producto', 'Categoria', 'Marca'], inplace=True)
df_productos['Precio_Costo'] = df_productos['Precio_Costo'].fillna(df_productos['Precio_Costo'].mean())  # Rellenar precios nulos con la media

# Limpieza de datos de ventas
df_ventas.dropna(subset=['Fecha_Venta', 'ID_Tienda', 'ID_Producto', 'Cantidad'], inplace=True)
df_ventas['Cantidad'] = df_ventas['Cantidad'].astype(int)  # Asegurar que "Cantidad" es entero
df_ventas['Importe_Venta'] = df_ventas['Cantidad'] * df_ventas['Importe_Venta']  # Calcular importe si no está disponible

# Verificar datos
print(df_clientes.info())
print(df_productos.info())
print(df_ventas.info())

# Guardar los datos limpios en archivos CSV para cargarlos a SQL Server
df_clientes.to_csv('Clean_Dim_Cliente.csv', index=False)
df_productos.to_csv('Clean_Dim_Producto.csv', index=False)
df_tiendas.to_csv('Clean_Dim_Tienda.csv', index=False)
df_ventas.to_csv('Clean_Fact_Ventas.csv', index=False)
