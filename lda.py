import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pull_data

var = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

xy_diff = []
result = []

a = pull_data.get_stats(var[0], var[1], 1)

for i in a:
    xy_diff.append([i[0], i[1]])
    result.append(i[2])

np_xy_diff = np.array(xy_diff)
np_result = np.array(result)

clf = LinearDiscriminantAnalysis().fit(np_xy_diff, np_result)

print(clf.predict([[-6, -6]]))
