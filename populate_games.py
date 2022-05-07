import scrape
import team_stats
import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()

sql2 = "INSERT INTO games () VALUES ()"
games = scrape.get_games()      # get array of games
for i in games:
    game_values = ()
    mycursor.execute(sql2, game_values)

mydb.commit()

print("Success")
