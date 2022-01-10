import re
from datetime import date
import csv
from traits import *

continuer = True

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







