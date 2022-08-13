import numpy as np
import matplotlib.pyplot as plt
import pull_data

var = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]


def graph_log_reg(var1, train):
    a = pull_data.difference(var1, train)
    dif = []
    outcome = []

    for i in a:
        dif.append(i[0])
        outcome.append(i[1])
    
    n_dif = np.array(dif)
    n_outcome = np.array(outcome)

    print(n_dif)
    print(n_outcome)

    plt.scatter(n_dif, n_outcome)
    plt.xlabel(var1)
    plt.ylabel("win")
    plt.show()

#print(graph("pts"))

def send_dif(var1, train):
    a = pull_data.difference(var1, train)
    dif = []

    for i in a:
        dif.append(i[0])
    
    n_dif = np.array(dif)

    return n_dif

def send_outcome(var1, train):
    a = pull_data.difference(var1, train)
    outcome = []

    for i in a:
        outcome.append(i[1])
    
    n_outcome = np.array(outcome)

    return n_outcome

#########################################################################################################################

#def graph_lda(stat1, stat2, train):

stat1 = "pts"
stat2 = "treb"
train = 1

a = pull_data.get_stats(stat1, stat2, train)
diff1_w = []
diff2_w = []
diff1_l = []
diff2_l = []
outcome = []

for i in a:
    if i[2] == 0:
        diff1_l.append(i[0])
        diff2_l.append(i[1])
    else:
        diff1_w.append(i[0])
        diff2_w.append(i[1])

n_diff1_w = np.array(diff1_w)
n_diff2_w = np.array(diff2_w)
n_diff1_l = np.array(diff1_l)
n_diff2_l = np.array(diff2_l)

print(len(n_diff1_w))
print(len(n_diff2_w))
print(len(n_diff1_l))
print(len(n_diff2_l))

plt.scatter(n_diff1_w, n_diff2_w)
plt.scatter(n_diff1_l, n_diff2_l)
plt.xlabel(stat1)
plt.ylabel(stat2)
plt.show()