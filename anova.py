from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import pandas as pd
import numpy as np
import query


stats = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

df = pd.DataFrame()

for i in stats:
    a = query.get_single_stat(i, 2012, 2022)
    diff = []
    for j in a:
        diff.append(j[0])
    df.insert(0, i, diff)

b = query.get_single_stat("fg", 2012, 2022)
outcome = []
for i in b:
    outcome.append(i[1])
np_outcome = np.array(outcome)

df.to_numpy()
#df.insert(0, "outcome", outcome)

print(np_outcome)
print(df)

fs = SelectKBest(score_func=f_classif, k=5)
model = fs.fit(df, outcome)
xx = fs.fit_transform(df, outcome)
print(model.scores_)
print(model.pvalues_)
print(xx)


#   "fg", "fg_pct", "tov", "pf", "pts"