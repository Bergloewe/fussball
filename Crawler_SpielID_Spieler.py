import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urljoin
import time
import csv
import string

liga = 'bundesliga'

SpielSpielerbib_jahr = []
Spieltag = []
ID = 15845

for year in range(2016, 2020):

    for day in range(1, 38):

        time.sleep(0.2)
        url = "https://www.fussballdaten.de/" + liga + "/" + str(year) + "/" + str(day)
        html_ausgelesen = requests.get(url)
        doc = BeautifulSoup(html_ausgelesen.text, "html.parser")
        print("https://www.fussballdaten.de/" + liga + "/" + str(year) + "/" + str(day) + " wird ausgelesen!")

        # Wenn nicht vorhandende Spieltageberichte
        if doc.select(".spiel-button-row") == []:
            print('No day ' + str(day) + " in year " + str(year))
            continue

        # Damit zum Schluss nicht Relegationsberichte eingfügt
        if day == 1:
            Spiele_pro_Tag = len(doc.select(".spiel-button-row"))
        SpielandemTag = 1

        # Jetzt wird der Spielreport der einzelen Spiele an dem Tag "angeklickt"
        for spielbuttonhtml in doc.select(".spiel-button-row"):
            spielreport_url = urljoin(url, spielbuttonhtml.select_one("a").attrs["href"]) + "aufstellung/"

            time.sleep(0.2)
            html_Reportausgelesen = requests.get(spielreport_url)
            Spielreport = BeautifulSoup(html_Reportausgelesen.text, "lxml")

            if Spielreport.select(".box-taktik") == []:  # keine BoxTaktikdarstellung

                for i in range(0, 22):

                    # wenn nicht genug Daten zu Spiel
                    if len(Spielreport.select(".text.lineup")) < 22:
                        Spieltag = ["leider nicht genug Daten unter " + spielreport_url]
                        break

                    name = Spielreport.select(".text.lineup")[i].text
                    link = Spielreport.select(".text.lineup")[i].attrs["href"][8:-6]

                    Spieltag.append((name, link))


            else:  # Mit Boxtaktik Darstellung

                # hier geht die schleife nicht bis 11, da zB in Spiel 2016/27/1 nur 10 Spieler in der Taktikbox eingetragen sind
                for i in range(0, len(Spielreport.select(".box-taktik")[0].select("a"))):
                    name = Spielreport.select(".box-taktik")[0].select("a")[i].select("span")[0].attrs["title"]
                    link = Spielreport.select(".box-taktik")[0].select("a")[i].attrs["href"][8:-1]

                    Spieltag.append((name, link))

                for i in range(0, len(Spielreport.select(".box-taktik")[1].select("a"))):
                    name = Spielreport.select(".box-taktik")[1].select("a")[i].select("span")[0].attrs["title"]
                    link = Spielreport.select(".box-taktik")[1].select("a")[i].attrs["href"][8:-1]

                    Spieltag.append((name, link))

            SpielSpielerbib_jahr.append((ID, Spieltag))
            print(ID)
            ID = ID + 1
            Spieltag = []

            # Damit nicht die Spielberichte der Relegation am letzten Tag angeklickt werden
            if SpielandemTag == Spiele_pro_Tag:
                break
            SpielandemTag = SpielandemTag + 1

    # Jahr in csv reinschreiben
    with open('SpielSpielerbib.csv', 'a', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerows(SpielSpielerbib_jahr)
        SpielSpielerbib_jahr = []