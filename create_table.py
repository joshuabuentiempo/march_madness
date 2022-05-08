import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE teams (Teamid INT NOT NULL AUTO_INCREMENT, team VARCHAR(255), year INT(3), fg FLOAT(3), fga FLOAT(3), fg_pct FLOAT(3), fg2 FLOAT(3), fg2a FLOAT(3), fg2_pct FLOAT(3), fg3 FLOAT(3), fg3a FLOAT(3), fg3_pct FLOAT(3), ft FLOAT(3), fta FLOAT(3), ft_pct FLOAT(3), oreb FLOAT(3), dreb FLOAT(3), treb FLOAT(3), ast FLOAT(3), stl FLOAT(3), blk FLOAT(3), tov FLOAT(3), pf FLOAT(3), pts FLOAT(3), PRIMARY KEY (Teamid))")

mycursor.execute("CREATE TABLE games (Gameid INT NOT NULL AUTO_INCREMENT, year INT(3), team_a VARCHAR(255), team_b VARCHAR(255), score_a INT(3), score_b INT(3), winner VARCHAR(255), PRIMARY KEY (Gameid))")
