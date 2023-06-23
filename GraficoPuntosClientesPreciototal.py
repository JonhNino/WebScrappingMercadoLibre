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
# Ejecutar la consulta y obtener los resultados en un DataFrame
query = "SELECT c.nombre, cc.precio_total FROM cliente c INNER JOIN carro_compra cc ON c.id_cliente = cc.id_cliente WHERE cc.estado = 'activo' ORDER BY cc.precio_total DESC LIMIT 5;;"

df = pd.read_sql(query, con=mydb)

# Crear el gráfico de puntos
plt.scatter(df['nombre'], df['precio_total'])
plt.xlabel('Clientes')
plt.ylabel('Precio Total [Mill]')
plt.title('Top 5 clientes con precio total más alto')
plt.show()