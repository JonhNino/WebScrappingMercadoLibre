import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"  
)


# Realizar la consulta y obtener los resultados en un DataFrame de Pandas
consulta = "SELECT nombre, YEAR(CURDATE()) - YEAR(fecha_nacimiento) AS edad FROM cliente WHERE id_cliente IN (SELECT DISTINCT id_cliente FROM cliente_cupon)"
df = pd.read_sql(consulta, con=mydb)

# Crear el gráfico de barras verticales
plt.bar(df["nombre"], df["edad"])
plt.xticks(rotation=90)
plt.xlabel("Nombre del cliente")
plt.ylabel("Edad del cliente")
plt.title("Edades de clientes que han utilizado al menos un cupón de descuento")
plt.show()

# Cerrar la conexión a la base de datos
mydb.close()