import pandas as pd
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="proyecto"       
)

# Create cursor
mycursor = mydb.cursor()

# Check if table already exists
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()
if ('celulares',) not in tables:
  # Create table
  mycursor.execute("CREATE TABLE celulares (id INT AUTO_INCREMENT PRIMARY KEY, name_product VARCHAR(255), price_product DECIMAL(10, 2), link_product VARCHAR(255), marca VARCHAR(255), description_product VARCHAR(255), color_product VARCHAR(255), condicion VARCHAR(255), images VARCHAR(255))")

# Read CSV file
data = pd.read_csv("Celulares.csv")

# Insert data into table
for index, row in data.iterrows():
    # Get values from row
    name_product = row["name_product"]
    price_product = row["price_product"]
    link_product = row["link_product"]
    marca = row["marca"]
    description_product = row["description_product"]
    color_product = row["color_product"]
    condicion = row["condicion"]
    images = row["images"]    

    # Insert row into table
    sql = "INSERT INTO celulares (name_product, price_product, link_product, marca, description_product, color_product, condicion, images) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name_product, price_product, link_product, marca, description_product, color_product, condicion, images)
    mycursor.execute(sql, val)

    # Commit changes
    mydb.commit()

# Close database connection
mydb.close()
