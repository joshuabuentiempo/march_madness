import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)


mycursor = mydb.cursor()

def difference(stat, train):
    if train == 1:
        sql = "SELECT year, team_a, team_b, score_a-score_b FROM games WHERE year < 2020"
    else:
        sql = "SELECT year, team_a, team_b, score_a-score_b FROM games WHERE year > 2020"
    mycursor.execute(sql)

    result = mycursor.fetchall()
    result_a = []
    result_b = []

    for i in result:
        sql_a = "SELECT " + stat +  " FROM teams WHERE team = %s AND year = %s"
        val_a = (i[1], i[0])
        mycursor.execute(sql_a, val_a)
        result_a.append(mycursor.fetchall()[0][0])

        sql_b = "SELECT " + stat +  " FROM teams WHERE team = %s AND year = %s"
        val_b = (i[2], i[0])
        mycursor.execute(sql_b, val_b)
        result_b.append(mycursor.fetchall()[0][0])

    final = []
    for i in range(0, len(result)):
        if result[i][3] > 0:
            final.append((round(result_a[i] - result_b[i], 2), 1))
        else:
            final.append((round(result_a[i] - result_b[i], 2), 0))

    return final

