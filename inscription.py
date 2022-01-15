import re
from datetime import date,datetime
from calendar import monthrange
import csv
from traits import *

continuer = True

choix = argparse.ArgumentParser()
choix.add_argument("-a","--add",help="Ajout d'inscrits du jour", action="store_true")
choix.add_argument("-d", "--display", help="Choix CSV d'un jour", action="store_true")
args = choix.parse_args()
if args.add:
    # Donnees inscriptions
    while continuer:
        # Nom / Prenom
        nom = input("Ecrire le nom ici:\n")
        prenom = input("Ecrire le prenom ici:\n")
        erreur = True
        while erreur:
            switch = 0
            # Date de naissance
            nvYear = input("Ecrire l'annee de naissance:\n")
            nvMonth = input("Ecrire le moi de naissance:\n")
            nvDay = input("Ecrire le jour de naissance\n")
            if len(nvYear) == 4:
                erreur = False
            else:
                print("l'année doit comporter 4 chiffres")
                erreur = True
                switch = 1
            if int(nvMonth) >= 1 and int(nvMonth) <= 12:
                erreur = False
            else:
                print("il n'y a que 12 mois dans l'année (rentrez une valeur entre 1 et 12)")
                erreur = True
                switch = 1
            if int(nvDay) > 0 and int(nvDay) <= nombreJours(nvYear,nvMonth,nvDay):
                erreur = False
            else:
                print("Il y a entre 1 et {}".format(nombreJours(nvYear,nvMonth,nvDay)))
                erreur = True
                switch = 1
            try:
                nvYear = int(nvYear)
                nvMonth = int(nvMonth)
                nvDay = int(nvDay)
            except ValueError:
                print("Indiquer la date de naissance en chiffre")
            else:
                erreur = False
            if switch == 1:
                erreur = True
        # Definir age et categorie nouveau inscrit (+prints)
        nvCat = categorie(nvYear, nvMonth, nvDay)
        print("--------------")
        print(nom)
        print(prenom)
        print(nvCat)
        # Creation adresse mail
        nvEmail = eMail(prenom, nom)
        print(nvEmail)
        print("--------------")
        # Ajout dans fichier csv
        fichierCSV()
        ajout(nvEmail,nvCat,nom,prenom)
        # Demande reiteration inscription
        suivant = input("avez-vous d'autres inscriptions? y/n \n")
        if suivant == "n":
            continuer = False

if args.display:
    erreurChoix = True
    erreurDate = True
    while erreurChoix:
        choix = int(input("Si vous souhaitez afficher les inscrits du moi, FAITES 1,\nSi vous souhaitez afficher les inscrits d'aujourd'hui, FAITES 2\nEt pour ceux d'un jour particulier, FAITES 3\n"))
        if choix == 1 and choix == 2 and choix == 3:
            erreurChoix = True
        else:
            print("le choix ne peut être que 1, 2 ou 3")
            erreurChoix = False
        if choix == 1:
            csvList, nombreCat = comptage()
            listNoDoub = doublon(csvList)
            triList = leTri(listNoDoub, nombreCat)
            fichierCsvFinal()
            ajoutFinal(triList)
            for i in triList:
                print(" ".join(i),end="\n\n")
        if choix == 2:
            with open('inscriptions\\'+tst, "r") as f:
                for line in f:
                    print(line)
        while erreurDate:
            if choix == 3:
                anneeCSV = datetime.today().year
                moiCSV = input("Ecrire le moi:\n")
                jourCSV = input("Ecrire le jour :\n")
                if int(moiCSV) >= 1 and int(moiCSV) <= 12:
                    erreur = False
                else:
                    print("il n'y a que 12 mois dans l'année (rentrez une valeur entre 1 et 12)")
                    erreur = True
                    switch = 1
                if int(jourCSV) > 0 and int(jourCSV) <= nombreJours(anneeCSV, moiCSV, jourCSV):
                    erreur = False
                else:
                    print("Il y a entre 1 et {}".format(nombreJours(anneeCSV, moiCSV, jourCSV)))
                    erreur = True
                    switch = 1
                try:
                    anneeCSV = int(nvYear)
                    moiCSV = int(moiCSV)
                    jourCSV = int(jourCSV)
                except ValueError:
                    print("Indiquer la date en chiffre")
                else:
                    erreur = False
                if switch == 1:
                    erreur = True
        with open('inscriptions\\'+"inscrits-{}-{}-{}.csv".format(anneeCSV,moiCSV,jourCSV), "r") as f2:
            for line2 in f2:
                print(line2)
