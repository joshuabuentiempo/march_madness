import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE team_stats")