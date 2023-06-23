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
df = pd.read_sql("SELECT price_product FROM tabla_union", con=mydb)

# Crear el diagrama de caja
plt.boxplot(df['price_product'])
plt.title('Rango de precios')
plt.ylabel('Precio')
plt.show()
