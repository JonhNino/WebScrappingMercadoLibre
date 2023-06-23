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

# Crea un cursor para ejecutar las consultas SQL
mycursor = mydb.cursor()

# Ejecuta la consulta SQL para obtener los datos de las marcas
mycursor.execute("SELECT marca, COUNT(*) AS cantidad FROM tabla_union GROUP BY marca ORDER BY cantidad DESC LIMIT 10")

# Obtiene los resultados de la consulta SQL
results = mycursor.fetchall()
# Convierte los resultados en un DataFrame de Pandas
df = pd.DataFrame(results, columns=["marca", "cantidad"])

# Creación del gráfico de barras
plt.bar(df["marca"], df["cantidad"])
plt.xticks(rotation=90) # Rotación de la leyenda en 90 grados


# Agrega las etiquetas de los ejes y el título del gráfico
plt.xlabel("Marca")
plt.ylabel("Cantidad de productos")
plt.title("Top 10 marcas con más productos")

# Muestra el gráfico
plt.show()
