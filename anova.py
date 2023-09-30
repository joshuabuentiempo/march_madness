from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import pandas as pd
import numpy as np
import query


stats = ["fg", "fga", "fg_pct", "fg2", "fg2a", "fg2_pct", "fg3", "fg3a", "fg3_pct", "ft", "fta", "ft_pct", "oreb", "dreb", "treb", "ast", "stl", "blk", "tov", "pf", "pts"]

df = pd.DataFrame()

for i in stats:
    a = query.get_single_stat(i, 2012, 2019)
    diff = []
    for j in a:
        diff.append(j[0])
    df.insert(0, i, diff)

b = query.get_single_stat("pts", 2012, 2019)
outcome = []
for i in b:
    outcome.append(i[1])
np_outcome = np.array(outcome)

df.to_numpy()
print(df)


fs = SelectKBest(f_classif, k=4)
model = fs.fit_transform(df, np_outcome)
print(fs.get_feature_names_out())
print(model)


#   "fg", "fg_pct", "tov", "pf", "pts"