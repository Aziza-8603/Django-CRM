import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="aziza",
    password="mypassword",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS website")

print("All Done!")

