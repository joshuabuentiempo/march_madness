import numpy as np
import matplotlib.pyplot as plt
import pull_data

var = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]


def graph(var1):
    a = pull_data.difference(var1)
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

print(graph("pts"))

