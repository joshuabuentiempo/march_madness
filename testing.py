"""

import scrape
import team_stats


a = scrape.get_teams()
b = []


x = scrape.get_games()

for i in x:
    print(i[2], i[0][0], i[1][0], i[0][1], i[1][1])





for i in a:
    print(i[0], i[1], team_stats.get_stats(i[2]))


x = 0
while x <= len(b):
    print(a[x], b[x])
    x += 1
"""

########################################################################################################################################## Check databases


import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM games"
#sql = "SHOW TABLES"
#sql = "DROP TABLE games"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)
