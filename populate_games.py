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

sql2 = "INSERT INTO games (year, team_a, team_b, score_a, score_b, winner) VALUES (%s,%s,%s,%s,%s,%s)"
games = scrape.get_games()      # get array of games
for i in games:
    if i[0][1] > i[1][1]:
        game_values = (i[2], i[0][0], i[1][0], i[0][1], i[1][1], i[0][0])
    else:
        game_values = (i[2], i[0][0], i[1][0], i[0][1], i[1][1], i[1][0])
    mycursor.execute(sql2, game_values)

mydb.commit()

print("Success")
