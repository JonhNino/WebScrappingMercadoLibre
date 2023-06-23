import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="proyecto"
)
# Crear tabla en la base de datos
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE computadores (id INT AUTO_INCREMENT PRIMARY KEY, name_product VARCHAR(255), price_product DECIMAL(10, 2), link_product VARCHAR(255), description_product VARCHAR(255), color_product VARCHAR(255), condicion VARCHAR(255), images VARCHAR(255))")

# Leer el archivo CSV y almacenar los datos en una variable
data = pd.read_csv("ComputadoresPortatil.csv")

# Iterar sobre los registros del archivo y agregarlos a la tabla de la base de datos
for index, row in data.iterrows():
    name_product = row["name_product"]
    price_product = row["price_product"]
    link_product = row["link_product"]
    description_product = row["description_product"]
    color_product = row["color_product"]
    condicion = row["condicion"]
    images = row["images"]

    sql = "INSERT INTO computadores (name_product, price_product, link_product, description_product, color_product, condicion, images) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name_product, price_product, link_product, description_product, color_product, condicion, images)
    mycursor.execute(sql, val)

    mydb.commit()

# Cerrar la conexión a la base de datos
mydb.close()
