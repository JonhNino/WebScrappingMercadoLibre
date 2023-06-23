import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos   
conexion  = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)          
cursor = conexion.cursor()  
# Realizar la consulta y obtener los resultados en un DataFrame de Pandas
consulta = "SELECT c.nombre, c.apellido, COUNT(*) AS num_pedidos FROM cliente c JOIN pedido p ON c.id_cliente = p.id_cliente GROUP BY c.id_cliente ORDER BY num_pedidos DESC LIMIT 10;"
df = pd.read_sql(consulta, con=conexion)

# Crear el gráfico de puntos
plt.scatter(df["num_pedidos"], df.index)
plt.xlabel("Número de pedidos")
plt.ylabel("Clientes")
plt.title("Número de pedidos realizados por cada cliente")
plt.yticks(df.index, df["nombre"] + " " + df["apellido"])
plt.show()

# Cerrar la conexión a la base de datos
conexion.close()