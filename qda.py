import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import classification_report
import query

stats = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

train_df = pd.DataFrame()
test_df = pd.DataFrame()
y_train = np.array([])
y_test = np.array([])

for i in stats:
    train_data = query.get_single_stat(i, 2012, 2019)
    test_data = query.get_single_stat(i, 2023, 2023)
    train_diff = []
    test_diff = []
    for j in train_data:
        train_diff.append(j[0])
        y_train = np.append(y_train, j[1])
    for k in test_data:
        test_diff.append(k[0])
        y_test = np.append(y_test, k[1])
    train_df.insert(0, i, train_diff)
    test_df.insert(0, i, test_diff)

x_train = train_df.to_numpy()
x_test = test_df.to_numpy()

y_train = y_train[:x_train.shape[0]]
y_test = y_test[:x_test.shape[0]]

qda = QuadraticDiscriminantAnalysis()
qda.fit(x_train, y_train)
print(str(stats))
print(qda.score(x_test, y_test))

gg = qda.predict(x_test)
qq = qda.predict_log_proba(x_test)
print("probabilities: " + str(qq))
print("predicted: " + str(gg))
print("actual: " + str(y_test))

