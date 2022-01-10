from datetime import date
import csv
import os.path

dt = date.today()
tst = "inscrits-" + str(dt) + ".csv"
headerList = ["Nom", "Prenom", "Categorie", "Mail"]

def age(bd):
    age = dt.year - bd.year - ((dt.month, dt.day) < (bd.month, bd.day))
    return age

def categorie(year,month,day):
    cat = {"Poussin": 12, "Cadet": 18, "Junior": 24, "Semi-pro": 30, "Pro": 40}
    nvAge = age(date(int(year), int(month), int(day)))
    if nvAge < 6 or nvAge > 40 :
        return "Non admis"
    for ind,key in enumerate(cat):
        if nvAge < list(cat.values())[ind]:
            return key

def eMail(firstName,secondName):
    fName= firstName[0].upper()
    sName= secondName.lower()
    return '{}.{}@baton-rouge.fr'.format(fName,sName)


def ajout(leMail,laCat,leNom,lePrenom):
    with open(tst,"a") as file:
        informations = csv.writer(file, delimiter=';')
        informations.writerow([leNom,lePrenom,laCat,leMail])

# verifier si le csv du jour est cree
def fichierCSV():
    # Si oui ajouter les donnees en utilisant la fonction
    if not os.path.isfile(tst):
        with open(tst, "a") as file:
            dw = csv.DictWriter(file, delimiter=';', fieldnames=headerList)
            dw.writeheader()
