from datetime import date
import csv
import os.path
from traits import *


# Transforme le csv en list et compte le nombre d'inscrit dans chaque catégorie
csvList,nombreCat= comptage()

# Supprime les doublons
listNoDoub = doublon(csvList)

# Effectue le tri en fonction des catégories (de la plus grand a la plus petite)
triList = leTri(listNoDoub,nombreCat)

# Creation et ajout des inscrits dans le fichier final
fichierCsvFinal()
ajoutFinal(triList)