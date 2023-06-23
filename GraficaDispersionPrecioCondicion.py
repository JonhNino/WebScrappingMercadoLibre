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

# Obtener los datos de la t     abla y cargarlos en un DataFrame
df = pd.read_sql("SELECT * FROM tabla_union LIMIT 10", con=mydb)

# Crear el gráfico de dispersión
plt.scatter(df['marca'], df['price_product'])
plt.xlabel('Marca')                     
plt.ylabel('Precio del producto [Mill]')
plt.title('Precio de los 10 primeros productos en función de su condición ')
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                      
