import numpy as np
import matplotlib.pyplot as plt
import pull_data

var = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

#var1 = "blk"

#fg, fga, fg2_pct, ft_pct, oreb, ast, blk, tov

def graph(var1):
    a = pull_data.get_graph_data(var1)

    var_arr = []
    for i in a:
        b = list(i)
        if i[0] == "W":
            b[0] = 1
            var_arr.append(b)
        else:
            b[0] = 0
            var_arr.append(b)
    #print(var_arr)
    y_arr = []
    for i in var_arr:
        y_arr.append(i[0])
    y_arr = np.array(y_arr)
    
    x_arr = []
    for i in var_arr:
        x_arr.append(i[1])
    x_arr = np.array(x_arr)

    plt.scatter(x_arr, y_arr)
    plt.xlabel(var1)
    plt.ylabel("win")
    plt.show()


def send_data(x):
    a = pull_data.get_graph_data(x)

    var_arr = []
    for i in a:
        b = list(i)
        if i[0] == "W":
            b[0] = 1
            var_arr.append(b)
        else:
            b[0] = 0
            var_arr.append(b)

    y_arr = []
    for i in var_arr:
        y_arr.append(i[0])
    y_arr = np.array(y_arr)
    
    x_arr = []
    for i in var_arr:
        x_arr.append(i[1])
    x_arr = np.array(x_arr)

    return x_arr, y_arr

def send_data_2(x):
    a = pull_data.get_graph_data_2(x)

    var_arr = []
    for i in a:
        b = list(i)
        if i[0] == "W":
            b[0] = 1
            var_arr.append(b)
        else:
            b[0] = 0
            var_arr.append(b)

    y_arr = []
    for i in var_arr:
        y_arr.append(i[0])
    y_arr = np.array(y_arr)
    
    x_arr = []
    for i in var_arr:
        x_arr.append(i[1])
    x_arr = np.array(x_arr)

    return x_arr, y_arr


"""
fg3, treb
blk, pts
oreb, tov
ft_pct, treb

w_arr = []
l_arr = []
for i in a:
    if i[0] == "W":
        w_arr.append(i)
    else:
        l_arr.append(i)

print(w_arr)
print(l_arr)


# Seperate variables of winning array
var1_w_arr = []
for i in w_arr:
    var1_w_arr.append(i[1])
var1_w_arr = np.array(var1_w_arr)
print(var1_w_arr)

var2_w_arr = []
for i in w_arr:
    var2_w_arr.append(i[2])
var2_w_arr = np.array(var2_w_arr)
print(var2_w_arr)

# Seperate variables of losing array
var1_l_arr = []
for i in l_arr:
    var1_l_arr.append(i[1])
var1_l_arr = np.array(var1_l_arr)
print(var1_l_arr)

var2_l_arr = []
for i in l_arr:
    var2_l_arr.append(i[2])
var2_l_arr = np.array(var2_l_arr)
print(var2_l_arr)
"""