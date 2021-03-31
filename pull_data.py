import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "CarletonU16",
    database = "team_stats"
)

"""
mycursor = mydb.cursor()
sql = "SELECT ft, pts FROM stats WHERE team = 'VCU' OR team = 'Duke'"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)
"""
mycursor = mydb.cursor()

def get_data(a, b):
    sql = "SELECT * FROM stats2018 WHERE team = %s OR team = %s"
    val = (a, b)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result

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