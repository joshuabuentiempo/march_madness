import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()

def get_stats(stat1, stat2, train):
    if train == 1:
        sql = "SELECT * FROM games WHERE year < 2020"
    else:
        sql = "SELECT * FROM games WHERE year > 2020"

    mycursor.execute(sql)

    result = mycursor.fetchall()
    result_a = []
    result_b = []


    for i in result:
        sql_a = "SELECT " + stat1 + "," + stat2 + ",Teamid FROM teams WHERE team = %s AND year = %s"
        val_a = (i[2], i[1])
        mycursor.execute(sql_a, val_a)
        result_a.append(mycursor.fetchall()[0])

        sql_b = "SELECT " + stat1 + "," + stat2 +  ",Teamid FROM teams WHERE team = %s AND year = %s"
        val_b = (i[3], i[1])
        mycursor.execute(sql_b, val_b)
        result_b.append(mycursor.fetchall()[0])

    diff1 = []
    diff2 = []
    win = []
    for i in range(len(result_a)):
        diff1.append(round(result_a[i][0] - result_b[i][0], 2))
        diff2.append(round(result_a[i][1] - result_b[i][1], 2))
        if result[i][6] == result[i][2]:
            win.append(1)
        else:
            win.append(0)

    final = []
    t2 = 0
    while t2 < len(win):
        final.append((diff1[t2], diff2[t2], win[t2]))
        t2 += 1

    return final

