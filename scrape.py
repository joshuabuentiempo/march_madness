import requests
from bs4 import BeautifulSoup

year = ""
url = "https://www.sports-reference.com/cbb/postseason/2019-ncaa.html"
games =[]

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="bracket")
#print(results.prettify())

def get_losers():
    teams = results.find_all("div", class_="")
    for team in teams:
        games.append(team)
    losers = games[1::2]
    return losers
#for i in losers:
#    print(i, end='\n'*2)

def get_winners():
    winners = []
    teams = results.find_all("div", class_="winner")
    for i in teams:
        winners.append(i)
    return winners