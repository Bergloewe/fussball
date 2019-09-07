import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import time
import csv
import string
import matplotlib.pyplot as plt
import numpy as np
import random as random
import math as math


def calc(HeimMannschaftLink,AuswMannschaftLink):
    # Mannschafts ID suchen

    with open('TeamID_Team.csv', 'r', newline='', encoding='utf-8') as csvfile:
        TeamID_Team = csv.reader(csvfile, delimiter=',', quotechar='"')

        for Team in TeamID_Team:
            Heimgefunden = False

            if Team[2] == HeimMannschaftLink:
                Heimgefunden = True
                HeimMannschaft = Team[1]
                HeimMannschaftID = Team[0]
                break

        if Heimgefunden == False:
            print("Heimmannschaft nicht gefunden!")

    with open('TeamID_Team.csv', 'r', newline='', encoding='utf-8') as csvfile:
        TeamID_Team = csv.reader(csvfile, delimiter=',', quotechar='"')

        for Team in TeamID_Team:
            Auswgefunden = False

            if Team[2] == AuswMannschaftLink:
                Auswgefunden = True
                AuswMannschaft = Team[1]
                AuswMannschaftID = Team[0]
                break

        if Auswgefunden == False:
            print("Auswärtsmannschaft nicht gefunden!")


    # Berechnet den Durchschnitts Tore und Gegentore über All time
    SpielID_TeamsID_Ergebnis_BL = pd.read_csv("bl_mit_allspieler.csv")

    SpielID_HeimID_Ergebnis_BL = SpielID_TeamsID_Ergebnis_BL[SpielID_TeamsID_Ergebnis_BL["team1_id"] == int(HeimMannschaftID)]
    SpielID_AuswID_Ergebnis_BL = SpielID_TeamsID_Ergebnis_BL[SpielID_TeamsID_Ergebnis_BL["team2_id"] == int(AuswMannschaftID)]

    HeimMann_DsTore = sum(SpielID_HeimID_Ergebnis_BL["tore_heim"]) / len(SpielID_HeimID_Ergebnis_BL["tore_heim"])
    HeimMann_DsGegenTore = sum(SpielID_HeimID_Ergebnis_BL["tore_aus"]) / len(SpielID_HeimID_Ergebnis_BL["tore_aus"])

    AuswMann_DsTore = sum(SpielID_AuswID_Ergebnis_BL["tore_aus"]) / len(SpielID_AuswID_Ergebnis_BL["tore_aus"])
    AuswMann_DsGegenTore = sum(SpielID_AuswID_Ergebnis_BL["tore_heim"]) / len(SpielID_AuswID_Ergebnis_BL["tore_heim"])


    # Ang/Vert auswerten

    PrgTorHeim = (HeimMann_DsTore * AuswMann_DsGegenTore) ** 0.5
    PrgTorAus = (AuswMann_DsTore * HeimMann_DsGegenTore) ** 0.5

    print(HeimMannschaft + " " + str(PrgTorHeim) + " : " + str(PrgTorAus) + " " + AuswMannschaft)

    # Formel der Poisson-Verteilung
    def poisson(k, lambda_):
        return (math.exp(-1 * lambda_) * lambda_ ** k) / math.factorial(k)

    Results=[]

    for TheoHeimTore in range(0, 6):
        for TheoAusTore in range(0, 6):
            Results.append([TheoHeimTore, TheoAusTore, poisson(TheoHeimTore, PrgTorHeim) * poisson(TheoAusTore, PrgTorAus) * 100])

    return np.array(Results)







