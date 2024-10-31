import pandas as pd
import random

# Datos iniciales
data = {
    'ID_Cliente': [1, 2, 3, 4, 5],
    'Nombre_Cliente': ['Alice', 'Bob', 'Charlie', 'Daniela', 'Elena'],
    'Edad': [30, 25, 35, 28, 40],
    'Genero': ['F', 'M', 'M', 'F', 'F'],
    'Ciudad': ['Buenos Aires', 'Córdoba', 'Mendoza', 'Rosario', 'Salta']
}

# Crear DataFrame
df = pd.DataFrame(data)

# Generar datos adicionales
nuevos_datos = []

for i in range(6, 106):  # Generar 1000 datos adicionales
    nombre = random.choice(['Ana', 'Juan', 'Carlos', 'María', 'Luis', 'Sofía', 'José', 'Laura'])
    edad = random.randint(18, 65)
    genero = random.choice(['M', 'F'])
    ciudad = random.choice(['Buenos Aires', 'Córdoba', 'Mendoza', 'Rosario', 'Salta', 'La Plata', 'Mar del Plata'])
    nuevos_datos.append([i, nombre, edad, genero, ciudad])

# Crear DataFrame de nuevos datos y concatenar con el original
df_nuevos = pd.DataFrame(nuevos_datos, columns=['ID_Cliente', 'Nombre_Cliente', 'Edad', 'Genero', 'Ciudad'])
df_completo = pd.concat([df, df_nuevos], ignore_index=True)

# Guardar en un archivo CSV
df_completo.to_csv('datos_ampliados.csv', index=False)

print("Datos generados y guardados en 'datos_ampliados.csv'")
