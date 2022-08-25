import secrets
from Commandes.Commandes import Commande
from Stations.Stations import StationClass
from functions import clearConsole, retryFunc, GAZOLINE_CHOICE, DIESEL_CHOICE, BOTH_GAZ_CHOICE, findCommandeById

v_station = StationClass()
v_commande = Commande()

def generer_id():
    # generate 1 secure random numbers between 10 and 500

    for x in range(0, 1):
        secret_id = (10 + secrets.randbelow(500)).__str__()
        print(secret_id)  # for show but no need
    # recursive function : get unique ID in all_commandes
    if findCommandeById(secret_id):
        generer_id()

    return secret_id


# functon to confirm commande
def confirm_commande():
    v_station.afficher()
    usertype = input("Voulez-vous confirmer la nouvelle commande ?\n1- Oui\n0- Non\nR- ")
    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)
            if usertype == 0 or usertype == 1:
                return usertype
            else:
                print("Incorrect! Le nombre doit etre 1 ou 0")
        else:
            print("Incorrect! Entrer une valeur entiere")


def ask_choice_commande():
    usertype = ""
    print(f"Veuillez choisir l'une de ces commandes:")
    print(f"1- {GAZOLINE_CHOICE}")
    print(f"2- {DIESEL_CHOICE}")
    print(f"3- {BOTH_GAZ_CHOICE}")
    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            if int(usertype) == 1:
                if confirm_commande() == 1:
                    # addCommande()
                    print("Add commande function")
                else:
                    valueReturn = retryFunc()
                    if valueReturn == 0:
                        break
            elif int(usertype) == 2:
                if confirm_commande() == 1:
                    # addCommande()
                    print("Add commande function")
                else:
                    valueReturn = retryFunc()
                    if valueReturn == 0:
                        break

            elif int(usertype) == 3:
                if confirm_commande() == 1:
                    # addCommande()
                    print("Add commande function")
                else:
                    valueReturn = retryFunc()
                    if valueReturn == 0:
                        break

            else:
                print("Veuillez choisir une valeur entre 1 et 3")
        else:
            print("Entrer une valeur correcte, entre 1 et 3")


def qte_gallon_diesel():
    qte_gallon_diesel = (1.10 * v_commande.total_gallon_diesel_maquant())
    return qte_gallon_diesel

def qte_gallon_gazoline():
    qte_gallon_gazoline = (1.25 * v_commande.total_gallon_gazoline_maquant())
    return qte_gallon_gazoline


def addCommande():
    usertype=""

    print("============| AJOUT D'UNE COMMANDE |============")
    print("Etat des stations")
    v_station.afficher()
    while True:

        v_commande.enregistrer()
        input("\nPress any key to continue")

        valueReturn = retryFunc()
        if valueReturn == 0:
            break


# ================================== AFFICHER TOUTES COMMANDE ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES COMMANDES |============")
    # v_station.afficher()