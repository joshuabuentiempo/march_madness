import numpy as np
from scipy.special import expit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import query

stat = "pf"

train_data = query.get_single_stat(stat, 2012, 2017)
test_data = query.get_single_stat(stat, 2018, 2022)

x_train = []
y_train = []
x_test = []
y_test = []

for i in train_data:
    x_train.append(i[0])
    y_train.append(i[1])

np_x_train = np.array(x_train).reshape(-1, 1)
np_y_train = np.array(y_train)

for i in test_data:
    x_test.append(i[0])
    y_test.append(i[1])

np_x_test = np.array(x_test).reshape(-1, 1)
np_y_test = np.array(y_test)

print(stat)

log_reg = LogisticRegression()
log_reg.fit(np_x_train, np_y_train)
print(log_reg.score(np_x_test, np_y_test))

gg = log_reg.predict(np_x_test)
print(gg)
print(np_y_test)


#   fg, pf