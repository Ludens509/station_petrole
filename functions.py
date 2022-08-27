import os
LALUE_CONST = "lalue"
TABARRE_CONST = "tabarre"
CLERCINE_CONST = "clercine"
PETION_VILLE_CONST = "petion-ville"

GAZOLINE_CONST = "gazoline"
DIESEL_CONST = "diesel"
GAZOLINE_CHOICE = 1
DIESEL_CHOICE = 2
BOTH_GAZ_CHOICE = 3

ANNULER_OPTION = 'ANNULER'

# objets
all_stations = dict()
# attributs of all_stations
CAPACITE_GAZOLINE = "capacite_gazoline"
CAPACITE_DIESEL = "capacite_diesel"
QTE_GAL_GAZOLINE_DISPO = "qte_dispo_gazoline"
QTE_GAL_DIESEL_DISPO = "qte_dispo_disel"
PERCENT_GAL_GAZOLINE = "percent_gazoline"
PERCENT_GAL_DIESEL = "percent_diesel"

all_commandes = list()
all_approvisionnements =set()

def findIfStationExist(name: str):
    if name in all_stations:
        return True

    return False

def findCommandeById(id: str):
    if id in all_commandes:
        return True
    return False

def retryFunc():
    usertype = ""
    while True:
        usertype = input("Voulez-vous recommencer ?\n1- Oui\n0- Non\nR- ")
        if usertype.isdigit():
            usertype = int(usertype)
            if usertype == 0 or usertype == 1:
                return usertype
            else:
                print("Incorrect! Le nombre doit etre 1 ou 0")
        else:
            print("Incorrect! Entrer une valeur entiere")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
