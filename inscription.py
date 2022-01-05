import re
from datetime import date
from traits import *

# Donnees inscriptions

nom = input("Ecrire le nom ici:\n")
prenom = input("Ecrire le prenom ici:\n")
nvYear,nvMonth,nvDay = input("Ecrire avec un espace l'année de naissance, le moi et le jour:\n").split(' ')

# Definir age et categorie nouveau inscrit

nvCat = categorie(nvYear,nvMonth,nvDay)
print(nvCat)

# Creation adresse mail

nvEmail = eMail(prenom,nom)
print(nvEmail)
