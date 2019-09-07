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


def HeimGewProSpielArray(SpielID_HeimID_Ergebnis_BL):
    # Auslesen der SpielerIDs aus der letzten Aufstellung
    SpielerIDsletzteAuf = []
    for i in range(1, 12):
        SpielerIDsletzteAuf.append(int(SpielID_HeimID_Ergebnis_BL[-1:][str(i)]))

    # definiere null vektoren zum schleifen summieren
    pos1 = np.zeros(SpielID_HeimID_Ergebnis_BL["1"].shape)
    pos2 = np.zeros(SpielID_HeimID_Ergebnis_BL["2"].shape)
    pos3 = np.zeros(SpielID_HeimID_Ergebnis_BL["3"].shape)
    pos4 = np.zeros(SpielID_HeimID_Ergebnis_BL["4"].shape)
    pos5 = np.zeros(SpielID_HeimID_Ergebnis_BL["5"].shape)
    pos6 = np.zeros(SpielID_HeimID_Ergebnis_BL["6"].shape)
    pos7 = np.zeros(SpielID_HeimID_Ergebnis_BL["7"].shape)
    pos8 = np.zeros(SpielID_HeimID_Ergebnis_BL["8"].shape)
    pos9 = np.zeros(SpielID_HeimID_Ergebnis_BL["9"].shape)
    pos10 = np.zeros(SpielID_HeimID_Ergebnis_BL["10"].shape)
    pos11 = np.zeros(SpielID_HeimID_Ergebnis_BL["11"].shape)

    # Vergleichen ob ein Spieler der letzten Aufstellung auf Pos 1 bis 11 jemals gespielt hat
    for SpielerID in SpielerIDsletzteAuf:
        pos1 = pos1 + np.array(SpielID_HeimID_Ergebnis_BL["1"] == SpielerID)
        pos2 = pos2 + np.array(SpielID_HeimID_Ergebnis_BL["2"] == SpielerID)
        pos3 = pos3 + np.array(SpielID_HeimID_Ergebnis_BL["3"] == SpielerID)
        pos4 = pos4 + np.array(SpielID_HeimID_Ergebnis_BL["4"] == SpielerID)
        pos5 = pos5 + np.array(SpielID_HeimID_Ergebnis_BL["5"] == SpielerID)
        pos6 = pos6 + np.array(SpielID_HeimID_Ergebnis_BL["6"] == SpielerID)
        pos7 = pos7 + np.array(SpielID_HeimID_Ergebnis_BL["7"] == SpielerID)
        pos8 = pos8 + np.array(SpielID_HeimID_Ergebnis_BL["8"] == SpielerID)
        pos9 = pos9 + np.array(SpielID_HeimID_Ergebnis_BL["9"] == SpielerID)
        pos10 = pos10 + np.array(SpielID_HeimID_Ergebnis_BL["10"] == SpielerID)
        pos11 = pos11 + np.array(SpielID_HeimID_Ergebnis_BL["11"] == SpielerID)

    MatrixTransponiert = np.vstack((pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11))
    Matrix = MatrixTransponiert.T

    # die gewichtungen
    GesSpiele = Matrix.shape[0]
    GewichtungproSpiel = []
    HeimGesamtGewicht = sum(sum(Matrix))

    for game in range(0, GesSpiele):
        GewichtungproSpiel.append(sum(Matrix[game]))

    # Fehlermeldungen!
    for i in range(0, Matrix.shape[0]):
        for j in range(0, Matrix.shape[1]):
            if Matrix[i][j] != 1 and Matrix[i][j] != 0:
                print("Matrixeintrag Zeile/Spiel " + str(i + 1) + " Spalte/Position " + str(j + 1) + " ist " + str(
                    Matrix[i][j]) + " und nicht 1!")

    if sum(GewichtungproSpiel) / HeimGesamtGewicht != 1:
        print(" !Achtung Gewichtung hat nicht ide Länge 1! ")

    if sum(GewichtungproSpiel) / HeimGesamtGewicht == 0:
        print(" !Achtung Gewichtung ist für alle Spiele Null! ")
    # Fehlermeldungen Ende!

    HeimGewProSpielArr = np.array(GewichtungproSpiel)
    return HeimGewProSpielArr, HeimGesamtGewicht


def AuswGewProSpielArray(SpielID_AuswID_Ergebnis_BL):
    # Auslesen der SpielerIDs aus der letzten Aufstellung
    SpielerIDsletzteAuf = []
    for i in range(12, 23):
        SpielerIDsletzteAuf.append(int(SpielID_AuswID_Ergebnis_BL[-1:][str(i)]))

    # definiere null vektoren zum schleifen summieren
    pos1 = np.zeros(SpielID_AuswID_Ergebnis_BL["12"].shape)
    pos2 = np.zeros(SpielID_AuswID_Ergebnis_BL["13"].shape)
    pos3 = np.zeros(SpielID_AuswID_Ergebnis_BL["14"].shape)
    pos4 = np.zeros(SpielID_AuswID_Ergebnis_BL["15"].shape)
    pos5 = np.zeros(SpielID_AuswID_Ergebnis_BL["16"].shape)
    pos6 = np.zeros(SpielID_AuswID_Ergebnis_BL["17"].shape)
    pos7 = np.zeros(SpielID_AuswID_Ergebnis_BL["18"].shape)
    pos8 = np.zeros(SpielID_AuswID_Ergebnis_BL["19"].shape)
    pos9 = np.zeros(SpielID_AuswID_Ergebnis_BL["20"].shape)
    pos10 = np.zeros(SpielID_AuswID_Ergebnis_BL["21"].shape)
    pos11 = np.zeros(SpielID_AuswID_Ergebnis_BL["22"].shape)

    # Vergleichen ob ein Spieler der letzten Aufstellung auf Pos 1 bis 11 jemals gespielt hat
    for SpielerID in SpielerIDsletzteAuf:
        pos1 = pos1 + np.array(SpielID_AuswID_Ergebnis_BL["12"] == SpielerID)
        pos2 = pos2 + np.array(SpielID_AuswID_Ergebnis_BL["13"] == SpielerID)
        pos3 = pos3 + np.array(SpielID_AuswID_Ergebnis_BL["14"] == SpielerID)
        pos4 = pos4 + np.array(SpielID_AuswID_Ergebnis_BL["15"] == SpielerID)
        pos5 = pos5 + np.array(SpielID_AuswID_Ergebnis_BL["16"] == SpielerID)
        pos6 = pos6 + np.array(SpielID_AuswID_Ergebnis_BL["17"] == SpielerID)
        pos7 = pos7 + np.array(SpielID_AuswID_Ergebnis_BL["18"] == SpielerID)
        pos8 = pos8 + np.array(SpielID_AuswID_Ergebnis_BL["19"] == SpielerID)
        pos9 = pos9 + np.array(SpielID_AuswID_Ergebnis_BL["20"] == SpielerID)
        pos10 = pos10 + np.array(SpielID_AuswID_Ergebnis_BL["21"] == SpielerID)
        pos11 = pos11 + np.array(SpielID_AuswID_Ergebnis_BL["22"] == SpielerID)

    MatrixTransponiert = np.vstack((pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11))
    Matrix = MatrixTransponiert.T

    # die Gewichtungen
    GesSpiele = Matrix.shape[0]
    GewichtungproSpiel = []
    AuswGesamtGewicht = sum(sum(Matrix))

    for game in range(0, GesSpiele):
        GewichtungproSpiel.append(sum(Matrix[game]))

    # Fehlermeldungen!
    for i in range(0, Matrix.shape[0]):
        for j in range(0, Matrix.shape[1]):
            if Matrix[i][j] != 1 and Matrix[i][j] != 0:
                print("Matrixeintrag Zeile/Spiel " + str(i + 1) + " Spalte/Position " + str(j + 1) + " ist " + str(
                    Matrix[i][j]) + " und nicht 1!")

    if sum(GewichtungproSpiel) / AuswGesamtGewicht != 1:
        print(" !Achtung Gewichtung hat nicht die Länge 1! sondern " + str(sum(GewichtungproSpiel) / AuswGesamtGewicht))

    if sum(GewichtungproSpiel) / AuswGesamtGewicht == 0:
        print(" !Achtung Gewichtung ist für alle Spiele Null! ")
    # Fehlermeldungen Ende!

    AuswGewProSpielArr = np.array(GewichtungproSpiel)
    return AuswGewProSpielArr, AuswGesamtGewicht




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



    ##########Berechnet den Gewichteten Durchschnitts Tore und Gegentore über Spieler des letzten Aufstellung############

    # Datenbank mit Ergbnissen und Spielern auslesen
    SpielID_TeamsID_Ergebnis = pd.read_csv("bl_mit_allspieler.csv")

    # Ang/Ver der HEIMMANNSCHAFT
    SpielID_HeimID_Ergebnis_BL = SpielID_TeamsID_Ergebnis[SpielID_TeamsID_Ergebnis["team1_id"] == int(HeimMannschaftID)]

    # Berechne Array der Gewichtung pro Spiel bestimmt nach Spielern welche in der letzt Aufstellung vorkommen
    HeimGewProSpielArr, HeimGesGewicht = HeimGewProSpielArray(SpielID_HeimID_Ergebnis_BL)

    HeimMann_GewDsTore = sum(np.array(SpielID_HeimID_Ergebnis_BL["tore_heim"]) * HeimGewProSpielArr / HeimGesGewicht)
    HeimMann_GewDsGegenTore = sum(np.array(SpielID_HeimID_Ergebnis_BL["tore_aus"]) * HeimGewProSpielArr / HeimGesGewicht)


    # Ang/Ver der AUSWÄRTSMANNSCHAFT
    SpielID_AuswID_Ergebnis_BL = SpielID_TeamsID_Ergebnis[SpielID_TeamsID_Ergebnis["team2_id"] == int(AuswMannschaftID)]

    # Berechne Array der Gewichtung pro Spiel bestimmt nach Spielern welche in der letzt Aufstellung vorkommen
    AuswGewProSpielArr, AuswGesGewicht = AuswGewProSpielArray(SpielID_AuswID_Ergebnis_BL)

    AuswMann_GewDsTore = sum(np.array(SpielID_AuswID_Ergebnis_BL["tore_aus"]) * AuswGewProSpielArr / AuswGesGewicht)
    AuswMann_GewDsGegenTore = sum(np.array(SpielID_AuswID_Ergebnis_BL["tore_heim"]) * AuswGewProSpielArr / AuswGesGewicht)


    # Ang/Vert auswerten

    PrgTorHeim = (HeimMann_GewDsTore * AuswMann_GewDsGegenTore) ** 0.5
    PrgTorAus = (AuswMann_GewDsTore * HeimMann_GewDsGegenTore) ** 0.5

    print(HeimMannschaft + " " + str(PrgTorHeim) + " : " + str(PrgTorAus) + " " + AuswMannschaft)

    # Formel der Poisson-Verteilung
    def poisson(k, lambda_):
        return (math.exp(-1 * lambda_) * lambda_ ** k) / math.factorial(k)

    Results=[]

    for TheoHeimTore in range(0, 6):
        for TheoAusTore in range(0, 6):
            Results.append([TheoHeimTore, TheoAusTore, poisson(TheoHeimTore, PrgTorHeim) * poisson(TheoAusTore, PrgTorAus) * 100])

    return np.array(Results)

