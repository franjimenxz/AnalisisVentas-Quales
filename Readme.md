# Proyecto de Data Warehouse y Visualización de Ventas

Este proyecto consiste en la creación de un sistema de análisis de ventas utilizando un enfoque de Data Warehouse. El objetivo es almacenar, transformar y analizar datos de ventas para obtener información útil a partir de visualizaciones interactivas en Power BI. El proyecto abarca la configuración de un Data Warehouse en SQL Server, la carga de datos desde archivos CSV mediante Python, y la creación de reportes en Power BI.

## Índice

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instrucciones](#instrucciones)
  - [1. SQL Server](#1-sql-server)
  - [2. Python para Carga de Datos](#2-python-para-carga-de-datos)
  - [3. Power BI para Visualización](#3-power-bi-para-visualización)
- [Guía de Uso](#guía-de-uso)
- [Conclusión](#conclusión)

---

## Descripción

Este proyecto utiliza un enfoque de Data Warehouse para organizar y analizar los datos de ventas de una tienda. Se desarrollaron diversas tareas para construir este sistema de análisis, incluyendo:

1. **Diseño del Esquema de Data Warehouse**: Se definieron y crearon tablas de dimensiones y una tabla de hechos para almacenar la información de ventas, permitiendo el análisis multidimensional.
2. **Transformación y Carga de Datos**: Se emplearon scripts en Python para cargar datos desde archivos CSV y llenar las tablas en SQL Server.
3. **Visualización en Power BI**: Se crearon reportes y visualizaciones interactivas en Power BI para analizar el rendimiento de ventas desde diferentes perspectivas, como tienda, producto, cliente y tiempo.

## Requisitos

- **SQL Server** (versión 2017 o superior)
- **SQL Server Management Studio (SSMS)**
- **Python 3.x** con las librerías `pandas` y `pyodbc`
- **Power BI Desktop**

## Estructura del Proyecto

El proyecto está organizado en las siguientes etapas:

1. **Esquema de Data Warehouse en SQL Server**:
   - **Dimensiones**: Tablas que contienen información descriptiva sobre los productos, clientes, tiendas y fechas (producto, cliente, tienda y tiempo).
   - **Tabla de Hechos**: Una tabla que registra las transacciones de ventas, permitiendo el análisis de las ventas realizadas.

2. **Scripts en Python**:
   - Se desarrollaron scripts en Python para cargar los datos desde archivos CSV a las tablas de SQL Server. Los scripts permiten transformar y limpiar los datos antes de su carga en las tablas correspondientes del Data Warehouse.

3. **Reportes en Power BI**:
   - Se diseñaron y crearon visualizaciones en Power BI, incluyendo KPIs y gráficos interactivos que permiten explorar el rendimiento de ventas por tienda, producto, cliente y período.

---

## Instrucciones

### 1. SQL Server

- **Creación del Data Warehouse**: Se creó una base de datos en SQL Server llamada `DW_DataShop`, en la que se definieron tablas de dimensiones (`Dim_Producto`, `Dim_Cliente`, `Dim_Tienda`, `Dim_Tiempo`) y una tabla de hechos (`Fact_Ventas`) para almacenar las transacciones de ventas.
- **Procedimientos Almacenados para Transformaciones**: Se implementaron procedimientos almacenados para automatizar la generación de datos de fechas en la tabla de tiempo y calcular el importe de ventas en la tabla de hechos.

### 2. Python para Carga de Datos

- **Carga de Datos desde CSV**: Se desarrollaron scripts en Python que utilizan `pandas` y `pyodbc` para cargar datos desde archivos CSV a las tablas de SQL Server. Los scripts permiten leer los archivos, limpiar los datos y cargarlos en las tablas del Data Warehouse.
- **Automatización**: Los scripts de Python cargan datos de las tablas de dimensiones y de la tabla de hechos, facilitando la actualización y el mantenimiento del Data Warehouse.

### 3. Power BI para Visualización

- **Conexión a SQL Server**: En Power BI, se configuró una conexión a SQL Server para extraer los datos desde el Data Warehouse `DW_DataShop`.
- **Creación de Visualizaciones**: Se construyeron diversas visualizaciones, tales como:
  - **KPIs**: Importe Total de Ventas, Cantidad de Ventas Realizadas, Precio Promedio por Producto y Cliente.
  - **Gráficos de Anillo**: Cantidad de productos vendidos por categoría y cantidad de clientes por tienda.
  - **Gráficos de Barras Apilados**: Ventas por producto, año y mes.
  - **Tabla Detalle de Ventas**: Tabla que muestra detalles de cada venta, incluyendo fecha, cliente, tienda, producto, cantidad, importe, precio de costo y precio de venta sugerido.
  - **Matriz Comparativa de Ventas por Tienda**: Tabla comparativa con columnas de año y mes, filas de tienda y producto, y valores de importe de ventas y porcentaje de variación mes a mes.
- **Formato Condicional**: Se aplicaron reglas de formato condicional en Power BI para resaltar las variaciones en las ventas mes a mes con colores (rojo, naranja, amarillo, verde), lo que facilita la interpretación de tendencias.

---

## Guía de Uso

1. **Ejecuta los Scripts de SQL** en SQL Server para crear la base de datos `DW_DataShop`, las tablas de dimensiones y la tabla de hechos.
2. **Ejecuta el Script de Python** para cargar los datos desde los archivos CSV a las tablas en SQL Server.
3. **Configura Power BI** para conectarse a SQL Server y carga las tablas de dimensiones y la tabla de hechos.
4. **Crea las Visualizaciones en Power BI**:
   - Sigue las instrucciones de diseño en Power BI para crear los KPIs, gráficos de anillo, gráficos de barras, tabla de detalle y matriz comparativa de ventas.

---

## Conclusión

Este proyecto proporciona un enfoque integral para la creación de un sistema de análisis de ventas utilizando un Data Warehouse, transformaciones de datos y visualizaciones interactivas en Power BI. Este sistema permite a los usuarios analizar las ventas por diferentes dimensiones (tienda, producto, cliente y tiempo) y obtener información clave para la toma de decisiones.