import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="proyecto"
)

# Obtener los datos de la tabla y cargarlos en un DataFrame
df = pd.read_sql("SELECT marca, condicion FROM tabla_union", con=mydb)

# Obtener las 10 marcas más repetidas
top_10_marcas = df['marca'].value_counts().head(10).index

# Filtrar por las 10 marcas más repetidas
df = df[df['marca'].isin(top_10_marcas)]

# Agrupar por marca y condición y contar las filas
df = df.groupby(['marca', 'condicion']).size().reset_index(name='count')

# Crear un gráfico de barras apiladas
df.pivot(index='marca', columns='condicion', values='count').plot(kind='bar', stacked=True)
plt.title('Condición de las 10 marcas más con mas articulos')
plt.xlabel('Marca')
plt.ylabel('Cantidad')
plt.show()
