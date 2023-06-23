import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos   
cnx  = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)          
cursor = cnx.cursor()  

# Consulta SQL para obtener los datos
query = "SELECT nombre, precio, existencias FROM producto" 
# Ejecutar la consulta y guardar los resultados en un DataFrame de Pandas
df = pd.read_sql(query, cnx)
df = df.head(5)


# Crear la figura y los ejes
fig, ax = plt.subplots()

# Configurar los límites del eje y
ax.set_ylim([0, len(df) + 1])

# Crear el gráfico de balas utilizando la función scatter
ax.scatter(df['precio'], df.index + 1, s=df['existencias'] * 10, color='blue')

# Etiquetar cada punto con el nombre del producto
for i, txt in enumerate(df['nombre']):
    ax.annotate(txt, (df['precio'][i], i + 1))

# Mostrar la gráfica
plt.show()

# Cerrar la conexión a la base de datos
cursor.close()
cnx.close()