import requests
from bs4 import BeautifulSoup

def get_stats(team, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    a = soup.find(id="schools_per_game")
    print(a)
