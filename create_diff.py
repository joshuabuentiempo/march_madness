import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16",
    database = "team_stats"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE diff (outcome VARCHAR(255), fg FLOAT(3), fga FLOAT(3), fg_pct FLOAT(3), fg2 FLOAT(3), fg2a FLOAT(3), fg2_pct FLOAT(3), fg3 FLOAT(3), fg3a FLOAT(3), fg3_pct FLOAT(3), ft FLOAT(3), fta FLOAT(3), ft_pct FLOAT(3), oreb FLOAT(3), dreb FLOAT(3), treb FLOAT(3), ast FLOAT(3), stl FLOAT(3), blk FLOAT(3), tov FLOAT(3), pf FLOAT(3), pts FLOAT(3))")
