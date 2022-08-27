import secrets
from datetime import date

from Approvisionnements.Approvisionnements import Approvisionnement
from functions import findCommandeById

v_approvisionnement = Approvisionnement()

def generer_id():
    # generate 1 secure random numbers between 10 and 500

    for x in range(0, 1):
        secret_id = (10 + secrets.randbelow(500)).__str__()
        print(secret_id)  # for show but no need
    # recursive function : get unique ID in all_commandes
    if findCommandeById(secret_id):
        generer_id()

    return secret_id


# generate system date
def generer_date():
    today = date.today()
    # Month abbreviation, day and year
    date_sys = today.strftime("%b-%d-%Y")
    # print("d4 =", d4)
    return date_sys


# generate etat
def generer_etat(state):
    etat = state
    return etat

# ================================== AFFICHER TOUTES LES APPROVISIONNEMENTS ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES APPROVISIONNEMENTS |============")
    v_approvisionnement.afficher()