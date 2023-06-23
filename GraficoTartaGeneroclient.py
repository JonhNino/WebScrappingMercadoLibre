import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos   
db_connection  = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)   

# Ejecutar la consulta SQL para obtener la cantidad de clientes por género
query = "SELECT genero, COUNT(*) AS cantidad FROM cliente GROUP BY genero"
df = pd.read_sql(query, con=db_connection)

# Crear el gráfico de tarta
fig, ax = plt.subplots()
ax.pie(df['cantidad'], labels=df['genero'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
ax.set_title('Porcentaje de clientes según género')

# Mostrar el gráfico
plt.show()
