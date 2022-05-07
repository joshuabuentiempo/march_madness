import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE my_db")