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
# Realizar la consulta y obtener los resultados en un DataFrame de Pandas
consulta = "SELECT porcentaje_descuento, COUNT(*) AS num_cupones FROM cupon_descuento GROUP BY porcentaje_descuento"
df = pd.read_sql(consulta, con=conexion)

# Crear el gráfico de tarta
plt.pie(df['num_cupones'], labels=df['porcentaje_descuento'], autopct='%1.1f%%')
plt.title('Porcentaje de la cantidad de descuentos')

# Mostrar el gráfico
plt.show()

# Cerrar la conexión a la base de datos
conexion.close()