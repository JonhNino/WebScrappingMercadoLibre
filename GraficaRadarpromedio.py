import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

# Conectar a la base de datos   
conexion  = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)   
# Consulta SQL
consulta = """
SELECT nombre, descripcion
FROM producto
WHERE precio < (
  SELECT AVG(precio)
  FROM producto
);
"""

# Ejecución de la consulta y obtención de los resultados
cursor = conexion.cursor()
cursor.execute(consulta)
resultados = cursor.fetchall()

# Creación de un dataframe con los resultados
df = pd.DataFrame(resultados, columns=["Nombre", "Descripcion"])

# Creación de una lista con las columnas del dataframe
columnas = list(df.columns[1:])

# Creación de una lista con los valores del primer registro del dataframe
valores = list(df.iloc[0, 1:])

# Añadir el primer valor al final de la lista para cerrar la gráfica
valores += valores[:1]

# Creación de una lista con los ángulos de la gráfica
angulos = [n / float(len(columnas)) * 2 * pi for n in range(len(columnas))]
angulos += angulos[:1]

# Creación de la figura
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Creación de la gráfica de radar
ax.plot(angulos, valores, linewidth=2, linestyle='solid', label=df.iloc[0, 0])
ax.fill(angulos, valores, 'b', alpha=0.1)

# Añadir leyenda y título
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title('Descripción de productos con precio menor al promedio')

# Mostrar la gráfica
plt.show()

# Cierre de la conexión a la base de datos
conexion.close()