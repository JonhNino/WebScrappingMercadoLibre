import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos   
cnx  = mysql.connector.connect(
  host="localhost",
  user="root",                                                                                                                                                                                                                                                              
  password="",
  database="comercioelectronicoproyecto"   
)          

cursor = cnx.cursor()    

# Obtener los 10 colores más repetidos en la columna color_product
query = "SELECT color_product, COUNT(*) AS cantidad FROM tabla_union GROUP BY color_product ORDER BY cantidad DESC LIMIT 10"
cursor.execute(query)
result = cursor.fetchall()

# Crear un DataFrame con los resultados obtenidos
df = pd.DataFrame(result, columns=['color_product', 'cantidad'])

# Crear un gráfico de pastel con los resultados obtenidos
plt.pie(df['cantidad'], labels=df['color_product'], autopct='%1.1f%%')
plt.title('Los 10 colores más repetidos para los articulos Computador y Telefonos')
plt.show()

# Cerrar la conexión a la base de datos
cursor.close()
cnx.close()
