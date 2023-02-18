import numpy as np
import matplotlib.pyplot as plt
import query

stat1 = ""
stat2 = ""

data = query.get_double_stat(stat1, stat2, 2014, 2014)

wins_x = []     #   stat1 differences for winning A teams
wins_y = []     #   stat2 differences for winning A teams
loss_x = []     #   stat1 differences for losing A teams
loss_y = []     #   stat2 differences for losing A teams

for i in data:
    if i[2] == 1:
        wins_x.append(i[0])
        wins_y.append(i[1])
    else:
        loss_x.append(i[0])
        loss_y.append(i[1])

x_values_wins = np.array(wins_x)
y_values_wins = np.array(wins_y)
x_values_loss = np.array(loss_x)
y_values_loss = np.array(loss_y)


#   Plotting graph
plt.plot(x_values_wins, y_values_wins, 'o')
plt.plot(x_values_loss, y_values_loss, 'o', mec = 'r')
plt.xlabel(stat1)
plt.ylabel(stat2)

plt.show()