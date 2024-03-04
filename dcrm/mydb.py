import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user='root',
    password='Vikas@123'
)
# Prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE sketch")
print("all set!")