import numpy as np
import matplotlib.pyplot as plt
import pull_data

var = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

var1 = "fg3"
var2 = "treb"

#fg3, treb

a = pull_data.get_graph(var1, var2)
"""
outcome_arr = []
for i in a:
    outcome_arr.append(i[0])
outcome_arr = np.array(outcome_arr)
print(outcome_arr)
"""

w_arr = []
l_arr = []
for i in a:
    if i[0] == "W":
        w_arr.append(i)
    else:
        l_arr.append(i)

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

plt.scatter(var1_w_arr,var2_w_arr) #blue
plt.scatter(var1_l_arr,var2_l_arr) #orange
plt.xlabel(var1)
plt.ylabel(var2)
plt.show()
