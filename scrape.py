import requests
from bs4 import BeautifulSoup

year = ""
url = "https://www.sports-reference.com/cbb/postseason/2019-ncaa.html"
games =[]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

east = soup.find(id="east")
east_results = east.find(id="bracket")
#print(results.prettify())

def get_losers():
    teams = results.find_all("div", class_="")
    for team in teams:
        games.append(team)
    losers = games[1::2]
    return losers

def get_winners():
    winners = []
    teams = results.find_all("div", class_="winner")
    #for i in teams:
    #    winners.append(i)
    for team in teams:
        names = teams.find("a")["href"]
    return names
"""
a = east_results.find_all('a')
del a[4::5]
for i in a:
    print(i.string)

print("------------------")
print("------------------")
print("------------------")
print("------------------")
print("------------------")

west = soup.find(id="west")
west_results = west.find(id="bracket")
b = west_results.find_all('a')
del b[4::5]
for i in b:
    print(i.string)

print("------------------")
print("------------------")
print("------------------")
print("------------------")
print("------------------")

midwest = soup.find(id="midwest")
midwest_results = midwest.find(id="bracket")
c = midwest_results.find_all('a')
del c[4::5]
for i in c:
    print(i.string)
"""
z = []
south = soup.find(id="south")
south_results = south.find(id="bracket")
d = south_results.find_all('a')
del d[4::5]
for i in d:
    z.append(i.string)
#print(z)

q = str(z[0].string)
w = int(z[1].string)
qq = z[::2]
ww = z[1::2]

arr1 = []
arr2 = []

i = 0
while i < len(qq) and i < len(ww):
    arr1.append([qq[i], ww[i]])
    i += 2

x = 1
while x < len(qq) and x < len(ww):
    arr2.append([qq[x], ww[x]])
    x += 2

p = 0
while p < len(arr1):
    print(arr1[p],arr2[p])
    p += 1 

south_teams = set(qq)