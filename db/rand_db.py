import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16",
    database = "team_stats"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM diff2018"
#sql = "SHOW TABLES"
#sql = "DROP TABLE diff"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)