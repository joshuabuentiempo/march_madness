import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report#, confusion_matrix
import graph_data

#fg, fga, fg2_pct, ft_pct, oreb, ast, blk, tov

a = graph_data.send_data("ast")
a = np.array(a)
x = a[0]
y = a[1]

x_r = x.reshape(-1,1)

model = LogisticRegression(solver = "liblinear", random_state = 0)
model.fit(x_r, y)

#print(model.intercept_)
#print(model.coef_)

print(model.predict_proba(x_r))

print("Actual = " + str(y))
print("Predict = " + str(model.predict(x_r)))

print(model.score(x_r, y))

print(classification_report(y, model.predict(x_r)))

plt.scatter(x_r, y)
plt.show()


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