"""
import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.sports-reference.com/cbb/postseason/2013-ncaa.html")
soup = BeautifulSoup(page.content, "html.parser")

f = open("html_code.txt", "w")
f.write(soup)
f.close()
"""

########################################################################################################################################## Check databases

"""
import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "qQmbPo.89",
    database = "my_db"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM games"
#sql = "SHOW TABLES"
sql = "DELETE FROM teams"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)

mydb.commit()

print("Success")

"""

###########################################################################################

"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression, LinearRegression
from scipy.special import expit

# Generate a toy dataset, it's just a straight line with some Gaussian noise:
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]


# Fit the classifier
clf = LogisticRegression(C=1e5)
clf.fit(X, y)

# and plot the result
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.scatter(X.ravel(), y, color="black", zorder=20)
X_test = np.linspace(-5, 10, 300)

loss = expit(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color="red", linewidth=3)


plt.show()



"""
