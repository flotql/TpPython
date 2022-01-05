import re
from datetime import date
from traits import *

continuer = True

# Donnees inscriptions

while continuer:
    # Nombre d'inscription
    nb = input("Combien d'inscriptions devez-vous rentrer? \n")
    try:
        nb = int(nb)
    except ValueError:
        print("Rentrer le nombre en chiffre")
    else:
        continuer = False
# Inscriptions
for _ in range(nb):
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
        # Definir age et categorie nouveau inscrit
        nvCat = categorie(nvYear, nvMonth, nvDay)
        print(nvCat)
        # Creation adresse mail
        nvEmail = eMail(prenom, nom)
        print(nvEmail)
        # suivant = input("avez-vous d'autres inscriptions? y/n \n") V3 !!!!!
        # if suivant == "n":
        #     continuer = False









