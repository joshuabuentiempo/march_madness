import scrape
import pull_data
import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16",
    database = "team_stats"
)

mycursor = mydb.cursor()

a = scrape.games()
ref = a[0]
otr = a[1]

#print(str(ref[0][0]), type(str(ref[0][0])), int(otr[0][1]), type(int(otr[0][1])))

i = 0
while i < len(ref):
    if int(ref[i][1]) > int(otr[i][1]) :
        o = "W"
    else:
        o = "L"
    dat = pull_data.get_data(str(ref[i][0]), str(otr[i][0]))
    d1 = dat[0]
    d2 = dat[1]
    d1_stat = d1[1:len(d1)]
    d2_stat = d2[1:len(d2)]
    x = 0
    diff = []
    sql = "INSERT INTO diff2018 (outcome, fg, fga, fg_pct, fg2, fg2a, fg2_pct, fg3, fg3a, fg3_pct, ft, fta, ft_pct, oreb, dreb, treb, ast, stl, blk, tov, pf, pts) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    while x < len(d1_stat):
        diff.append(round(d1_stat[x] - d2_stat[x], 3))
        x += 1
    val = (o, diff[0], diff[1], diff[2], diff[3], diff[4], diff[5], diff[6], diff[7], diff[8], diff[9], diff[10], diff[11], diff[12], diff[13], diff[14], diff[15], diff[16], diff[17], diff[18], diff[19], diff[20])
    mycursor.execute(sql, val)
    i += 1

mydb.commit()

print("Success")
