import requests
import pandas
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv
import string

# liest die namen in url aus, speichert Set, aus der Spielerbib https://www.fussballdaten.de/person/,

# id = 0 durch id wird set unnötig
Spielerbib = set()
s
# um alle Spieler zu erfassen müssen beide Buchstaben Aa, Ab durchgeklickt werden
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:

        time.sleep(1)
        url = "https://www.fussballdaten.de/person/?letter=" + first_letter + "&sl=" + first_letter + second_letter
        doc = BeautifulSoup(requests.get(url).text, "html.parser")

        # nicht vorhandende Namen anfangen zB Bc
        try:
            doc.select(".row.p20")[0].select("a")
        except:
            print('No name with ' + str(first_letter) + str(second_letter))
            continue

        print(first_letter + second_letter)

        SpielerSeite = doc.select(".row.p20")[0].select("a")

        for i in range(0, len(SpielerSeite)):  # geht alle Spieler auf der Webseite von Xx durch

            link = SpielerSeite[i].attrs["href"][8:-1]
            name = SpielerSeite[i].text

            # print("Die bib sieht so aus " + str(Spielerbib))
            # print("Der neue Eintrag sieht so aus " + str((id,name,link)))

            # Die if Abfrage weil die neue id +1 immer ins set rein bringt
            # if ((id,name,link) in Spielerbib) == False:
            # id = id + 1
            Spielerbib.add((name, link))


with open('Spielerbib.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='; ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(sorted(Spielerbib))
