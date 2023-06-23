import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos   
mydb = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="proyecto"   
)                                                                                                   

# Obtener los datos de la tabla y cargarlos en un DataFrame
df = pd.read_sql("SELECT condicion, COUNT(*) as cantidad FROM tabla_union GROUP BY condicion", con=mydb)

# Crear el gráfico de tarta
plt.pie(df['cantidad'], labels=df['condicion'], autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Cantidad de artículos según su condición')
plt.show()
