import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import graph_data
import scrape

#fg, fga, fg2_pct, ft_pct, oreb, ast, blk, tov

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
56% fg
53% fga
55% fg2_pct
55% ft_pct
58% oreb
61% ast
66% blk
53% tov
"""