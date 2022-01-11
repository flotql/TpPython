from datetime import date
import csv
import os.path
import argparse

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

# csv en list
def comptage():
    with open('inscriptions\\'+tst) as file:
        writer = []
        compte = {"Poussin": 0, "Cadet": 0, "Junior": 0, "Semi-pro": 0, "Pro": 0}
        lec = csv.reader(file, delimiter=";")
        for i in lec:
            if len(i) != 0:
                if i[2] != 'Categorie':
                    compte[i[2]] += 1
                    writer.append(i)
    return writer, compte

# suppr les doublons
def doublon(writer):
    writer2 = {}
    for i,val in enumerate(writer):
        writer2[writer[i][3]] = [writer[i][0],writer[i][1],writer[i][2],writer[i][3]]
    return list(writer2.values())

# tri par cat et nbr dans cat
def leTri(writer2,compte):
    compteOrder = sorted(compte.items(), key=lambda x: x[1], reverse=True)
    writerFinal = []
    for i in compteOrder:
        for j,val in enumerate(writer2):
            if writer2[j][2] == i[0]:
                writerFinal.append(writer2[j])
    return writerFinal

# creation fichier final
def fichierCsvFinal():
    if not os.path.isfile('inscriptions\\'+'inscrits_total.csv'):
        with open('inscriptions\\'+'inscrits_total.csv', "a") as file:
            dw = csv.DictWriter(file, delimiter=';', fieldnames=headerList)
            dw.writeheader()

# ajout données dans fichier final
def ajoutFinal(writerFinal):
    with open('inscriptions\\'+'inscrits_total.csv',"a") as file:
        informations = csv.writer(file, delimiter=';')
        for i,val in enumerate(writerFinal):
            informations.writerow(writerFinal[i])

# Choix csv par moi oui jour
def leChoix():
    choix = argparse.ArgumentParser()
    choix.add_argument("-m", "--month", type=str, help="Choix CSV du moi")
    choix.add_argument("-d", "--day", type=str, help="Choix CSV d'un jour")
    args = choix.parse_args()
    # si choix par moi, prendre tous les fichiers du moi indiquer
    if args.month:
        with open("inscriptions\\"+"inscrits-"+args.month+"csv", "x") as file:
            inscritsMoi = csv.writer(file, delimiter=";")
            inscritsMoi.writerow()
            print("le fichier {} a bien  été créé".format(args.month))
    # si choix par jour, prendre le fichier du jour indiquer
    if args.day:
        with open("inscriptions\\"+"inscrits-"+args.day+"csv", "x") as file2:
            inscritsJour = csv.writer(file2,delimiter=";")
            inscritsJour.writerow(args.day)
            print("le fichier {} a bien  été créé".format(args.day))


