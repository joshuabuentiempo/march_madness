import requests
from bs4 import BeautifulSoup

yr = 2
while yr < 9:
    year = "201" + str(yr)
    url = "https://www.sports-reference.com/cbb/postseason/" + year + "-ncaa.html"
    print(year)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #print(results.prettify())


    # Create array of each game for East =========================================================================================================
    east_z = []
    east = soup.find(id="east")
    east_results = east.find(id="bracket")
    east_a = east_results.find_all('a')

    del east_a[4::5]

    for i in east_a:
        east_z.append(i.string)

    #print(east_z) east_z = [game1_team1, game1_team1_score, game1_team2, game1_team2_score, game2_team1, game2_team1_score, game2_team2, game2_team2_score, ......]

    all_east_games_teams = east_z[::2]
    all_east_games_scores = east_z[1::2]

    east_arr1 = [] # [team, score] for each "top" team
    east_arr2 = [] # [team, score] for each "bottom" team

    east_i = 0
    while east_i < len(all_east_games_teams) and east_i < len(all_east_games_scores):
        east_arr1.append([all_east_games_teams[east_i], all_east_games_scores[east_i]])
        east_i += 2

    east_x = 1
    while east_x < len(all_east_games_teams) and east_x < len(all_east_games_scores):
        east_arr2.append([all_east_games_teams[east_x], all_east_games_scores[east_x]])
        east_x += 2

    east_p = 0
    while east_p < len(east_arr1):
        #print(east_arr1[east_p], east_arr2[east_p])
        east_p += 1 


    # Create array of each game for West =========================================================================================================
    west_z = []
    west = soup.find(id="west")
    west_results = west.find(id="bracket")
    west_a = west_results.find_all('a')
    del west_a[4::5]
    for i in west_a:
        west_z.append(i.string)

    all_west_games_teams = west_z[::2]
    all_west_games_scores = west_z[1::2]

    west_arr1 = []
    west_arr2 = []

    west_i = 0
    while west_i < len(all_west_games_teams) and west_i < len(all_west_games_scores):
        west_arr1.append([all_west_games_teams[west_i], all_west_games_scores[west_i]])
        west_i += 2

    west_x = 1
    while west_x < len(all_west_games_teams) and west_x < len(all_west_games_scores):
        west_arr2.append([all_west_games_teams[west_x], all_west_games_scores[west_x]])
        west_x += 2

    west_p = 0
    while west_p < len(west_arr1):
        #print(west_arr1[west_p], west_arr2[west_p])
        west_p += 1 


    # Create array of each game for Midwest =========================================================================================================
    midwest_z = []
    midwest = soup.find(id="midwest")
    midwest_results = midwest.find(id="bracket")
    midwest_a = midwest_results.find_all('a')
    del midwest_a[4::5]
    for i in midwest_a:
        midwest_z.append(i.string)

    all_midwest_games_teams = midwest_z[::2]
    all_midwest_games_scores = midwest_z[1::2]

    midwest_arr1 = []
    midwest_arr2 = []

    midwest_i = 0
    while midwest_i < len(all_midwest_games_teams) and midwest_i < len(all_midwest_games_scores):
        midwest_arr1.append([all_midwest_games_teams[midwest_i], all_midwest_games_scores[midwest_i]])
        midwest_i += 2

    midwest_x = 1
    while midwest_x < len(all_midwest_games_teams) and midwest_x < len(all_midwest_games_scores):
        midwest_arr2.append([all_midwest_games_teams[midwest_x], all_midwest_games_scores[midwest_x]])
        midwest_x += 2

    midwest_p = 0
    while midwest_p < len(midwest_arr1):
        #print(midwest_arr1[midwest_p], midwest_arr2[midwest_p])
        midwest_p += 1


    # Create array of each game for South =========================================================================================================
    south_z = []
    south = soup.find(id="south")
    south_results = south.find(id="bracket")
    south_a = south_results.find_all('a')
    del south_a[4::5]
    for i in south_a:
        south_z.append(i.string)

    all_south_games_teams = south_z[::2]
    all_south_games_scores = south_z[1::2]

    south_arr1 = []
    south_arr2 = []

    south_i = 0
    while south_i < len(all_south_games_teams) and south_i < len(all_south_games_scores):
        south_arr1.append([all_south_games_teams[south_i], all_south_games_scores[south_i]])
        south_i += 2

    south_x = 1
    while south_x < len(all_south_games_teams) and south_x < len(all_south_games_scores):
        south_arr2.append([all_south_games_teams[south_x], all_south_games_scores[south_x]])
        south_x += 2

    south_p = 0
    while south_p < len(south_arr1):
        #print(south_arr1[south_p],south_arr2[south_p])
        south_p += 1 


    # Create array of each game for Final =========================================================================================================
    final_z = []
    final = soup.find(id="national")
    final_results = final.find(id="bracket")
    final_a = final_results.find_all('a')

    del final_a[4::5]
    final_a.pop()

    for i in final_a:
        final_z.append(i.string)

    all_final_games_teams = final_z[::2]

    all_final_games_scores = final_z[1::2]

    final_arr1 = []
    final_arr2 = []

    final_i = 0
    while final_i < len(all_final_games_teams) and final_i < len(all_final_games_scores):
        final_arr1.append([all_final_games_teams[final_i], all_final_games_scores[final_i]])
        final_i += 2

    final_x = 1
    while final_x < len(all_final_games_teams) and final_x < len(all_final_games_scores):
        final_arr2.append([all_final_games_teams[final_x], all_final_games_scores[final_x]])
        final_x += 2

    final_p = 0
    while final_p < len(final_arr1):
        #print(final_arr1[final_p],final_arr2[final_p])
        final_p += 1 

    team_as = east_arr1 + west_arr1 + midwest_arr1 + south_arr1 + final_arr1
    team_bs = east_arr2 + west_arr2 + midwest_arr2 + south_arr2 + final_arr2

    tt = 0
    while tt < len(team_bs):
        print(team_as[tt], team_bs[tt])
        tt += 1

    yr += 1


"""
    east_teams = set(all_east_games_teams)
    west_teams = set(all_west_games_teams)
    midwest_teams = set(all_midwest_games_teams)
    south_teams = set(all_south_games_teams)


    # dictionary of { team : team_url }
    team_dict = {}
    east_g = east_a[::2]
    west_g = west_a[::2]
    midwest_g = midwest_a[::2]
    south_g = south_a[::2]
    g = east_g + west_g + midwest_g + south_g
    for i in g:
        team_dict.update({ i.string : "https://www.sports-reference.com"+i["href"]})
    #for key, value in team_dict.items():
    #    print(key , " : ", value)

    # masterlist of teams
    master_teams = east_teams.union(west_teams.union(midwest_teams.union(south_teams)))
    #for i in master_teams:
    #    print(i)

    def get_teams():
        return team_dict
"""

def games():
    return [team_as, team_bs]
