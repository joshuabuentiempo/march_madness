import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()

def get_data(stat, year_start, year_end):
    sql_games = "SELECT * FROM games WHERE year > " + str(year_start) + "AND year < " + str(year_end)
    mycursor.execute(sql_games)
    result = mycursor.fetchall()

    list_a = []
    list_b = []

    for i in result:
        sql_stat = "SELECT " + stat + "FROM teams WHERE team = %s AND year = %s"
        val_a = (i[2], i[1])
        mycursor.execute(sql_stat, val_a)
        list_a.append(mycursor.fetchall()[0])

        sql_b = "SELECT " + stat + "FROM teams WHERE team = %s AND year = %s"
        val_b = (i[3], i[1])
        mycursor.execute(sql_b, val_b)
        list_b.append(mycursor.fetchall()[0])

    data = []
    for i in range(0, result):
        if result[i][6] == result[i][2]:
            data.append((round(list_a[i][0] - list_b[i][0], 2), 1))
        else:
            data.append((round(list_a[i][0] - list_b[i][0], 2), 0))

    return data