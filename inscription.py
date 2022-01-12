import re
from datetime import date,datetime
import csv
from traits import *

continuer = True

choix = argparse.ArgumentParser()
choix.add_argument("--add",help="Ajout d'inscrits du jour", action="store_true")
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
            if (len(nvMonth) == 1 or len(nvMonth) == 2) and (len(nvDay) == 1 or len(nvDay) == 2):
                erreur = False
            else:
                print("le moi et le jour doivent comporter 1 ou 2 chiffres")
                erreur = True
                switch = 1
            if int(nvMonth) != 0 and int(nvDay) != 0:
                erreur = False
            else:
                print("le moi ou le jour 0 n'existe pas")
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
    choix = int(input("Si vous souhaitez afficher les inscrits du moi, FAITES 1,\nSi vous souhaitez afficher les inscrits d'aujourd'hui, FAITES 2\nEt pour ceux d'un jour particulier, FAITES 3\n"))

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
    if choix == 3:
        anneeCSV = datetime.today().year
        moiCSV = input("Ecrire le moi:\n")
        jourCSV = input("Ecrire le jour :\n")
        with open('inscriptions\\'+"inscrits-{}-{}-{}.csv".format(anneeCSV,moiCSV,jourCSV), "r") as f2:
            for line2 in f2:
                print(line2)