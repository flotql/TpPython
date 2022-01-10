from datetime import date
import csv
import os.path

dt = date.today()
tst = "inscrits-" + str(dt) + ".csv"
headerList = ["Nom", "Prenom", "Categorie", "Mail"]

# definir l'age de l'inscrit
def age(bd):
    age = dt.year - bd.year - ((dt.month, dt.day) < (bd.month, bd.day))
    return age

# ajout inscrit dans categorie
def categorie(year,month,day):
    cat = {"Poussin": 12, "Cadet": 18, "Junior": 24, "Semi-pro": 30, "Pro": 40}
    nvAge = age(date(int(year), int(month), int(day)))
    if nvAge < 6 or nvAge > 40 :
        return "Non admis"
    for ind,key in enumerate(cat):
        if nvAge < list(cat.values())[ind]:
            return key

# creation email
def eMail(firstName,secondName):
    fName= firstName[0].upper()
    sName= secondName.lower()
    return '{}.{}@baton-rouge.fr'.format(fName,sName)

# ajout d'inscrits dans le fichier csv
def ajout(leMail,laCat,leNom,lePrenom):
    with open('inscriptions\\'+tst,"a") as file:
        informations = csv.writer(file, delimiter=';')
        informations.writerow([leNom,lePrenom,laCat,leMail])

# verifier si le csv du jour est cree et creation si il n'existe pas
def fichierCSV():
    if not os.path.isfile('inscriptions\\'+tst):
        with open('inscriptions\\'+tst, "a") as file:
            dw = csv.DictWriter(file, delimiter=';', fieldnames=headerList)
            dw.writeheader()
