from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.foxsports.com/mlb/players")
bsObj = BeautifulSoup(html, "html.parser")
f = open("mlb_urls.txt", 'w')

def get_next_page(html, bsObj):
    for i in range (1, 123):
        new_url = "http://www.foxsports.com/mlb/players?teamId=0&season=2017&position=0&page=" + str(i) + "&country=0&grouping=0&weightclass=0"
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        get_player_pages(bsObj)

def get_player_pages(bsObj):
    players = bsObj.findAll("a", {"class": "wisbb_fullPlayer"})
    for player in players:
        if 'href' in player.attrs:
            partial = str(player.attrs['href'])
            new_url = "http://www.foxsports.com" + partial
            f.write(str(new_url) + "\n")
    get_next_page(html, bsObj)

get_player_pages(bsObj)
f.close()
