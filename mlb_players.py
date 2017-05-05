from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.foxsports.com/mlb/players")
bsObj = BeautifulSoup(html, "html.parser")



def get_player_pages(html, bsObj):
    players = bsObj.findAll("a", {"class": "wisbb_fullPlayer"})
    for player in players:
        if 'href' in player.attrs:
            partial = str(player.attrs['href'])
            new_url = "http://www.foxsports.com" + partial
        print(new_url)
