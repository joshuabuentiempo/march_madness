import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)


mycursor = mydb.cursor()

def difference(stat):
    sql = "SELECT * FROM games"
    #sql = "SELECT Teamid, team, year, ft, pts FROM teams WHERE team = 'VCU' OR team = 'Duke'"
    mycursor.execute(sql)

    result = mycursor.fetchall()
    result_a = []
    result_b = []

    for i in result:
        sql_a = "SELECT " + stat +  " FROM teams WHERE team = %s AND year = %s"
        val_a = (i[2], i[1])
        mycursor.execute(sql_a, val_a)
        result_a.append(mycursor.fetchall()[0][0])

        sql_b = "SELECT " + stat +  " FROM teams WHERE team = %s AND year = %s"
        val_b = (i[3], i[1])
        mycursor.execute(sql_b, val_b)
        result_b.append(mycursor.fetchall()[0][0])


    t = 0
    diff = []
    win = []
    while t < len(result_a):
        diff.append(result_a[t] - result_b[t])
        if result[t][6] == result[t][2]:
            win.append(1)
        else:
            win.append(0)
        t += 1

    final = []
    t2 = 0
    while t2 < len(win):
        final.append((diff[t2], win[t2]))
        t2 += 1

    return final


"""
mycursor = mydb.cursor()
sql = "SELECT * FROM games"
#sql = "SELECT Teamid, team, year, ft, pts FROM teams WHERE team = 'VCU' OR team = 'Duke'"
mycursor.execute(sql)

result = mycursor.fetchall()

print(result[0])



mycursor = mydb.cursor()

def get_data_a(year, team_a, stat):
    sql = "SELECT " + stat +  " FROM teams WHERE team = %s AND year = %s"
    val = (team_a, year)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result

def get_data_b(year, team_b, stat):
    sql = "SELECT " + stat +  " FROM teams WHERE team = %s AND year = %s"
    val = (team_b, year)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result
"""




def get_graph_data(c):
    sql = "SELECT outcome, " + c + " FROM diff"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

def get_graph_data_2(c):
    sql = "SELECT outcome, " + c + " FROM diff2018"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result



"""
def get_graph_data(c, d):
    sql = "SELECT outcome, " + c + ", " + d + " FROM diff"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result
"""