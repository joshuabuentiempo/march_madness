import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM diff2018"
sql = "SHOW TABLES"
#sql = "DROP TABLE diff"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)