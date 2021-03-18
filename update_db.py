import scrape
import team_stats
import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16",
    database = "team_stats"
)

#mycursor = mydb.cursor()
#sql = "INSERT INTO stats (team , fg, fga, fg_pct, fg2, fg2a, fg2_pct, fg3, fg3a, fg3_pct, ft, fta, ft_pct, oreb, dreb, treb, ast, stl, blk, tov, pf, pts) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

a = scrape.get_teams()
for i in a:
    b = team_stats.get_stats(i, a[i])
    print(b)
    #mycursor.execute(sql, b)
