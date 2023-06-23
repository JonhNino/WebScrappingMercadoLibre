import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Conectar a la base de datos   
conexion   = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)          

# Consulta SQL
consulta = """
SELECT c.nombre, AVG(p.precio) AS precio_promedio
FROM categoria c
JOIN producto p ON c.codigo_categoria = p.categoria
GROUP BY c.codigo_categoria;
"""

# Ejecución de la consulta y obtención de los resultados
cursor = conexion.cursor()
cursor.execute(consulta)
resultados = cursor.fetchall()

# Creación de un dataframe con los resultados
df = pd.DataFrame(resultados, columns=["Categoria", "Precio Promedio"])
df['Precio Promedio'] = df['Precio Promedio'].astype(float)

# Gráfico de tabla
tabla = pd.pivot_table(df, values='Precio Promedio', index='Categoria', aggfunc=np.sum)
tabla.plot(kind='bar')
plt.xlabel('Categoria')
plt.ylabel('Precio Promedio')
plt.title('Promedio de precios de productos por categoria')
plt.show()

# Cierre de la conexión a la base de datos
conexion.close()