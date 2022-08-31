import os
# import pyautogui
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
PRICE_GAZOLINE = 250
PRICE_DIESEL = 353
AMOUNT_IS_UNDER_MISC = -99
ERROR_MISC = -1

VENTE_ID = "id"
VENTE_STATION = "nom_station"
VENTE_QTE_GAL_GAZOLINE = "qte_gal_gazoline"
VENTE_QTE_GAL_DIESEL = "qte_gal_diesel"
VENTE_DATE = "date"
VENTE_MONTANT_GAZOLINE = "montant_gazoline"
VENTE_MONTANT_DIESEL = "montant_diesel"
VENTE_MONTANT_TOTAL = "montant_total"
VENTE_VERSEMENT_CLIENT = "versement"
VENTE_REMISE = "remise"


def findIfStationExist(name: str):
    if name in all_stations:
        return True

    return False


def findIfQteIsOver(name: str):
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
    # pycham
    # pyautogui.hotkey('command', 'l')


#  ===============================
# generate system date
def generer_date():
    today = date.today()
    # Month abbreviation, day and year
    date_sys = today.strftime("%b-%d-%Y")
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
    is_confirm = False
    print("\n\t\t ========== PRIVILEGE ADMINISTRATEUR ==============")
    print(
        "\nPour continuer, vous devez etre un admin (ou contacter votre supperieur)\nVoulez-vous continuer ?\n1- Oui\n0- Non\n")
    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)
            if usertype == 0:
                return False
            elif usertype == 1:
                name = input("Veuillez entrer votre nom:\nR- ")
                pwd = input("Veuillez entrer votre mot de passe:\nR- ")
                # file access
                is_confirm = fileAccess(nom=name, pwd=pwd)
                if is_confirm:
                    print("Identity is confirm")
                    return True
                else:
                    return False
            else:
                print("Incorrect! Le nombre doit etre 0 ou 1")
        else:
            print("Incorrect! Entrer une valeur entiere")


def fileAccess(nom: str, pwd: str) -> bool:
    filepath = "Documents/auth.txt"
    find_user = False
    try:
        with open(filepath, mode="r", encoding='utf-8') as file:
            for line in file:
                data = line.split("|")
                if data[0] == nom and data[1].replace("\n", "") == pwd:
                    find_user = True
                    break
            # end for

            if find_user:
                return True
            else:
                return False
        # end with
    finally:
        file.close()
