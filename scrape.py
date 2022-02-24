import requests
from bs4 import BeautifulSoup

teams = []

yr = 2
while yr < 9:
    year = "201" + str(yr)
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
        games = regional_bracket.find_all('a')

        del games[4::5]

        #url
        site = []
        for i in games[::2]:
            site.append(i["href"])

        i = 0
        while i < len(games):
            games[i] = games[i].string
            i += 1

        bracket_teams = games[::2]
        bracket_scores = games[1::2]

        arr1 = [] # [team, score] for each "top" team
        arr2 = [] # [team, score] for each "bottom" team
        
        a = 0
        while a < len(bracket_teams) and a < len(bracket_scores):
            arr1.append([bracket_teams[a], bracket_scores[a]])
            a += 2

        b = 1
        while b < len(bracket_teams) and b < len(bracket_scores):
            arr2.append([bracket_teams[b], bracket_scores[b]])
            b += 2

        for i in arr1:
            team_a.append(i)
        arr1.clear()

        for i in arr2:
            team_b.append(i)
        arr2.clear()

        c = 0
        while c < len(bracket_teams):
            a = (bracket_teams[c], "201" + str(yr), site[c])
            yr_teams.append(a)
            c += 1

    for i in yr_teams:
        teams.append(i)
    yr_teams.clear()

    yr += 1

def get_teams():
    return set(teams)


def games():
    return [team_as, team_bs]