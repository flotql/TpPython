from datetime import date
import csv
def age(bd):
    atm = date.today()
    age = atm.year - bd.year - ((atm.month, atm.day) < (bd.month, bd.day))
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

# def save(leMail,laCat,leNom,lePrenom,lAge,dateInscrip):
#     with open("donnees.csv","w") as file:
#         informations = csv.writer(file)
#         informations.writerow(leNom,lePrenom,lAge,laCat,leMail,dateInscrip)
#
#
# informations.writerow(["Nom,Prénom", "Age", "Catégorie", "eMail", "Date d'inscription"])