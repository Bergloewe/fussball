import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv

liga = 'bundesliga'
year=1970
day=2

"""
class CrawledArticle():
    def __init__(self, Team1Spieler1, Team1Spieler2, Team1Spieler3, Team1Spieler4, Team1Spieler5, Team1Spieler6,...):
        self.Team1Spieler1 = Team1Spieler1
        self.Team1Spieler2 = Team1Spieler2
        self.Team1Spieler3 = Team1Spieler3
        self.Team1Spieler4 = Team1Spieler4
        self.Team1Spieler5 = Team1Spieler5
        self.Team1Spieler6 = Team1Spieler6
        self.Team1Spieler7 = Team1Spieler7
        self.Team1Spieler8 = Team1Spieler8
        self.Team1Spieler9 = Team1Spieler9
        self.Team1Spieler10 = Team1Spieler10
        self.Team1Spieler11 = Team1Spieler11
        self.Team1Trainer = Team1Trainer

        self.Team2Spieler1 = Team2Spieler1
        self.Team2Spieler2 = Team2Spieler2
        self.Team2Spieler3 = Team2Spieler3
        self.Team2Spieler4 = Team2Spieler4
        self.Team2Spieler5 = Team2Spieler5
        self.Team2Spieler6 = Team2Spieler6
        self.Team2Spieler7 = Team2Spieler7
        self.Team2Spieler8 = Team2Spieler8
        self.Team2Spieler9 = Team2Spieler9
        self.Team2Spieler10 = Team2Spieler10
        self.Team2Spieler11 = Team2Spieler11
        self.Team2Trainer = Team2Trainer
"""


class ArticleFetcher():
    def fetch(self):

        url = "https://www.fussballdaten.de/" + liga + "/" + str(year) + "/" + str(day)
        Personen = []


        time.sleep(1)
        html_ausgelesen = requests.get(url)
        doc = BeautifulSoup(html_ausgelesen.text, "html.parser")
        i = 1

        while url != "":

            # Jetzt wird der Spielreport "angeklickt"

            for spielbuttonhtml in doc.select(".spiel-button-row"):
                spielreport_url = urljoin(url, spielbuttonhtml.select_one("a").attrs["href"]) + "aufstellung/"

                html_Reportausgelesen = requests.get(spielreport_url)
                Spielreport = BeautifulSoup(html_Reportausgelesen.text, "lxml")

                for Spieler in Spielreport.select(".text.lineup"):
                    player.append(Spieler.text)
                    player.append(Spieler.attrs["href"][8:-6])
                    time.sleep(1)








                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                crawled = CrawledArticle(title, emojiemoji, content, image)
                articles.append(crawled)

            i = i + 1  # Schleifen durchlauf zähler

            # Nächste Seite
            test = doc.select(".navigation")
            if test:

                navigation = doc.select(".navigation")[0]
                url = urljoin(url, navigation.select_one("a").attrs["href"])
                r = requests.get(url)
                doc = BeautifulSoup(r.text, "html.parser")
            else:
                print("finish")
                return articles

