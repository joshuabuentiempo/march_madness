import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16",
    database = "team_stats"
)

mycursor = mydb.cursor()
sql = "SELECT ft, pts FROM stats WHERE team = 'VCU' OR team = 'Duke'"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)