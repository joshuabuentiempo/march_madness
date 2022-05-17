import requests
from bs4 import BeautifulSoup

def get_stats(url):
    page = requests.get("https://www.sports-reference.com" + url)
    soup = BeautifulSoup(page.content, "html.parser")

    a = soup.find(id="schools_per_game")
    td = a.find_all("td")
    x = td[2:23]
    fg = float(x[0].string)
    fga = float(x[1].string)
    fg_pct = float(x[2].string)
    fg2 = float(x[3].string)
    fg2a = float(x[4].string)
    fg2_pct = float(x[5].string)
    fg3 = float(x[6].string)
    fg3a = float(x[7].string)
    fg3_pct = float(x[8].string)
    ft = float(x[9].string)
    fta = float(x[10].string)
    ft_pct = float(x[11].string)
    oreb = float(x[12].string)
    dreb = float(x[13].string)
    treb = float(x[14].string)
    ast = float(x[15].string)
    stl = float(x[16].string)
    blk = float(x[17].string)
    tov = float(x[18].string)
    pf = float(x[19].string)
    pts = float(x[20].string)
    return([fg, fga, fg_pct, fg2, fg2a, fg2_pct, fg3, fg3a, fg3_pct, ft,
            fta, ft_pct, oreb, dreb, treb, ast, stl, blk, tov, pf, pts])

#get_stats("Liberty", "https://www.sports-reference.com/cbb/schools/liberty/2019.html")
#get_stats("Duke", "https://www.sports-reference.com/cbb/schools/duke/2019.html")
#get_stats("Maryland", "https://www.sports-reference.com/cbb/schools/maryland/2019.html")


