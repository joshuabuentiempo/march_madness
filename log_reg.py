import numpy as np
from scipy.special import expit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import graph_data

var = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

for i in var:
    print(i)
    x = graph_data.send_dif(i, 1)
    y = graph_data.send_outcome(i, 1)

    x = x[:, np.newaxis]

    clf = LogisticRegression().fit(x, y)


    print(clf.intercept_)
    print(clf.coef_)


    x_test = graph_data.send_dif(i, 0)
    y_true = graph_data.send_outcome(i, 0)

    x_test = x_test[:, np.newaxis]

    pred = clf.predict(x_test)

    #for i in range(0, len(pred)):
    #    print(pred[i], y_test[i])


    print(clf.score(x_test, y_true))
    print("###############################################")



"""
plt.clf()

plt.scatter(a.ravel(), b, color="black", zorder=20)
X_test = np.linspace(-8, 8)

loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color="red", linewidth=2)


plt.show()
"""






"""
a = graph_data.send_data("blk")
a = np.array(a)
x = a[0]
y = a[1]

b = graph_data.send_data_2("blk")
b = np.array(b)
x2 = b[0]
y2 = b[1]

x_r = x.reshape(-1,1)
x2_r = x2.reshape(-1,1)

model = LogisticRegression(solver = "liblinear", random_state = 0)
model.fit(x_r, y)

"""

#print(model.intercept_)
#print(model.coef_)
#print(model.predict_proba(x_r))
"""
print("Actual = " + str(y))
print("Predict = " + str(model.predict(x_r)))
print(model.score(x_r, y))
print("----------------------------------------------------------------------------")
print("Actual = " + str(y2))
print("Predict = " + str(model.predict(x2_r)))
print(model.score(x2_r, y2))
"""
#print(classification_report(y, model.predict(x_r)))

"""
games = scrape.games()

pred = model.predict(x2_r)

z1 = games[0]
z2 = games[1]
i = 0
while i < len(z1):
    if int(pred[i]) == 1:
        print(z1[i])
    else:
        print(z2[i])
    i += 1 

"""

"""
56% fg
53% fga
55% fg2_pct
55% ft_pct
58% oreb
61% ast
66% blk
53% tov
"""