import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos   
mydb  = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)   

# Consulta SQL
query = "SELECT c.nombre, c.apellido, (SELECT COUNT(*) FROM pedido p WHERE p.id_cliente = c.id_cliente) AS num_pedidos FROM cliente c;"

# Lectura de datos utilizando Pandas
df = pd.read_sql(query, mydb)

# Gráfico de Puntos
plt.scatter(df.index, df['num_pedidos'], color='blue')
plt.xlabel('Cliente')
plt.ylabel('Cantidad de pedidos')
plt.title('Cantidad de pedidos por cliente')
plt.xticks(df.index, df['nombre'] + ' ' + df['apellido'], rotation=90)
plt.show()