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

# Consulta SQL para obtener los datos
query = "SELECT marca, existencias FROM producto"

# Carga los datos en un dataframe de pandas
df = pd.read_sql_query(query, cnx)

# Agrupa los datos por marca y suma las existencias
df_grouped = df.groupby('marca').sum().sort_values(by='existencias', ascending=False)

# Selecciona las 3 marcas con más existencias
top_3 = df_grouped.head(3)

# Crea el gráfico de barras
plt.bar(top_3.index, top_3['existencias'])

# Configura el título y las etiquetas de los ejes
plt.title('Marcas con más existencias')
plt.xlabel('Marca')
plt.ylabel('Existencias')

# Muestra el gráfico
plt.show()
