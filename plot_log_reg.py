import numpy as np
import matplotlib.pyplot as plt
import query

stat = "fg_pct"

data = query.get_single_stat(stat, 2012, 2019)

x = []
y = []

for i in data:
    x.append(i[0])
    y.append(i[1])

x_values = np.array(x)
y_values = np.array(y)


#   Calculating means for Team A wins and losses
win_temp = []
lose_temp = []
for i in data:
    if i[1] == 1:
        win_temp.append(i[0])
    else:
        lose_temp.append(i[0])

win_mean = sum(win_temp)/len(win_temp)
print(win_mean)
lose_mean = sum(lose_temp)/len(lose_temp)
print(lose_mean)
print(abs(win_mean - lose_mean))

a = [win_mean, lose_mean]
b = [1, 0]


#   Plotting graph
plt.plot(x_values, y_values, 'o')
plt.plot(a, b, 'o', mec = 'r')
plt.title(stat)
plt.xlabel('Stat Difference')
plt.ylabel('Win')

plt.show()