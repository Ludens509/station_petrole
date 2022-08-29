import secrets
from datetime import date

from Approvisionnements.Approvisionnements import Approvisionnement
from Commandes import menu_commande
from functions import findCommandeById, retryFunc

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
    return date_sys


# generate etat
def generer_etat(state):
    etat = state
    return etat

# functon to confirm approvisionnement
def confirm_approvisionnememt():
    usertype =""
    while True:
        print("Voulez-vous confirmer l'enregistrement de l'approvisionnement ?\n1- Oui\n0- Non\n ")
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)
            if usertype == 0 or usertype == 1:
                return usertype
            else:
                print("Incorrect! Le nombre doit etre 1 ou 0")
        else:
            print("Incorrect! Entrer une valeur entiere")


def addApprovisionnement():
    usertype = ""

    print("============| AJOUT D'UNE COMMANDE |============")

    while True:
        id = generer_id()
        qte_gallon_gazoline = menu_commande.qte_gallon_gazoline()
        station = "lalue"
        qte_gallon_diesel = menu_commande.qte_gallon_diesel()
        date_app = generer_date()

        v_approvisionnement.enregistrer(id=id,station= station, qte_gallon_gazoline=qte_gallon_gazoline, qte_gallon_diesel=qte_gallon_diesel,
                               date_app=date_app)
        input("\nPress any key to continue")

        valueReturn = retryFunc()
        if valueReturn == 0:
            break

# ================================== AFFICHER TOUTES LES APPROVISIONNEMENTS ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES APPROVISIONNEMENTS |============")
    v_approvisionnement.afficher()