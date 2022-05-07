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

sql = "INSERT INTO teams (team, year, fg, fga, fg_pct, fg2, fg2a, fg2_pct, fg3, fg3a, fg3_pct, ft, fta, ft_pct, oreb, dreb, treb, ast, stl, blk, tov, pf, pts) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
teams = scrape.get_teams()      # get array of teams
for i in teams:
    b = team_stats.get_stats(i[2])
    team_values = (i[0], i[1], b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10], b[11], b[12], b[13], b[14], b[15], b[16], b[17], b[18], b[19], b[20])       # team_name, year, stats ... 
    mycursor.execute(sql, team_values)

mydb.commit()

print("Success")