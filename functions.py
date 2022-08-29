import os
from datetime import date

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
P_STATE_COMMAND = "P"
N_STATE_COMMAND = "N"

# ---------- OBJECTS -------

# stations
all_stations = dict()

# attributs of all_stations
CAPACITE_GAZOLINE = "capacite_gazoline"
CAPACITE_DIESEL = "capacite_diesel"
QTE_GAL_GAZOLINE_DISPO = "qte_dispo_gazoline"
QTE_GAL_DIESEL_DISPO = "qte_dispo_disel"
PERCENT_GAL_GAZOLINE = "percent_gazoline"
PERCENT_GAL_DIESEL = "percent_diesel"
QTE_GAL_GAZOLINE_CONSOMMEE = "qte_gazoline_consommee"
QTE_GAL_DIESEL_CONSOMMEE = "qte_diesel_consommee"
QTE_GAL_GAZOLINE_MANQUEE = "qte_gazoline_manquee"
QTE_GAL_DIESEL_MANQUEE = "qte_diesel_manquee"
TOTAL_GAL_GAZOLINE_MANQUEE = "total_gazoline_manquee"
TOTAL_GAL_DIESEL_MANQUEE = "total_diesel_manquee"

# commands
all_commandes = list()

# attributes
COMMAND_ID = "id"
COMMAND_QTE_GAZOLINE = "qte_gaz_command"
COMMAND_QTE_DIESEL = "qte_diesel_command"
COMMAND_STATE = "state_command"
COMMAND_DATE = "date_command"

# approvisionnements
all_approvisionnements = set()

# ventes
all_ventes = list()

# attributes
PRICE_GAZOLINE = "prix_gazoline"
PRICE_DIESEL = "prix_diesel"


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


#  ===============================
# generate system date
def generer_date():
    today = date.today()
    # Month abbreviation, day and year
    date_sys = today.strftime("%b-%d-%Y")
    print("Date sys =", date_sys)
    return date_sys


# generate etat
def generer_etat(state):
    if state == N_STATE_COMMAND:
        return N_STATE_COMMAND

    return P_STATE_COMMAND


# Confirm identity

# functon to confirm commande
def confirm_identity() -> bool:
    usertype = ""
    print("Vous devez confirmer pour continuer ?\n1- Oui\n0- Non\n")
    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)
            if usertype == 0:
                return False
            elif usertype == 1:
                return True
            else:
                print("Incorrect! Le nombre doit etre 0 ou 1")
        else:
            print("Incorrect! Entrer une valeur entiere")
