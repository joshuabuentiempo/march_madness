# Scrapes the data for each March Madness year starting in 2012 
# Gives a set of all teams participating
# Gives a set of all games played

from email.errors import HeaderDefect
import requests
from bs4 import BeautifulSoup

teams = []
games = []


for y in range(2012, 2023):  # get 2012 to 2019 data for training
    year = str(y)
    if y == 2020:
        pass
    else:
        url = "https://www.sports-reference.com/cbb/postseason/" + year + "-ncaa.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        yr_teams = []
        team_a = []
        team_b = []
        regions = ["east", "west", "midwest", "south", "national"]
        
        for a in regions:
            regional_data = soup.find(id=a)
            regional_bracket = regional_data.find(id="bracket")
            regional_games = regional_bracket.find_all("a")
            regional_games.pop(len(regional_games) - 1)


            for i in range(0, len(regional_games)):
                regional_games[i] = (regional_games[i].string, regional_games[i])


            for i in range(0, len(regional_games)):
                if regional_games[i][0].string.startswith("at"):
                    regional_games[i] = 0


            for i in regional_games:
                if i == 0:
                   regional_games.remove(i)

            

            for i in range(0, len(regional_games)):
                regional_games[i] = list(regional_games[i])
                if regional_games[i][0].isdigit():
                    regional_games[i][0] = int(regional_games[i][0].string)
                else:
                    regional_games[i][0] = str(regional_games[i][0].string)

            for i in range(1, len(regional_games)):
                if type(regional_games[i][0]) == type(regional_games[i-1][0]):
                    regional_games[i-1] = [0,0]
                    regional_games[i] = [0,0]

            regional_games = [i for i in regional_games if i != [0,0]]



            bracket_teams = regional_games[::2]
            bracket_scores = regional_games[1::2]


            arr1 = []      # [team, score] for each "top" team
            arr2 = []      # [team, score] for each "bottom" team
                       
            a = 0
            while a < len(bracket_teams) and a < len(bracket_scores):
                arr1.append([bracket_teams[a][0], bracket_scores[a][0]])
                a += 2

            b = 1
            while b < len(bracket_teams) and b < len(bracket_scores):
                arr2.append([bracket_teams[b][0], bracket_scores[b][0]])
                b += 2
   

            for i in arr1:
                team_a.append(i)
            arr1.clear()

            for i in arr2:
                team_b.append(i)
            arr2.clear()

            c = 0
            while c < len(bracket_teams):
                a = (bracket_teams[c][0], year, bracket_teams[c][1].get("href"))
                yr_teams.append(a)
                c += 1

        for i in yr_teams:
            teams.append(i)
        yr_teams.clear()

        i = 0
        while i < len(team_a):
            games.append((team_a[i], team_b[i], year))
            i += 1
        

def get_teams():
    return set(teams)


def get_games():
    return games

