import secrets
from datetime import date

import functions
from Commandes.Commandes import Commande
from Stations.Stations import StationClass
from functions import clearConsole, retryFunc, GAZOLINE_CHOICE, DIESEL_CHOICE, BOTH_GAZ_CHOICE, findCommandeById, \
    GAZOLINE_CONST, DIESEL_CONST, TOTAL_GAL_DIESEL_MANQUEE, \
    TOTAL_GAL_GAZOLINE_MANQUEE, confirm_identity

v_station = StationClass()
v_commande = Commande()


def getQteGallonDieselToCommand() -> float:
    total_to_comnand = v_station.sommeQtes()
    return 1.10 * float(total_to_comnand[TOTAL_GAL_DIESEL_MANQUEE])


def getQteGallonGazolineToCommand() -> float:
    return 1.25 * float(v_station.sommeQtes()[TOTAL_GAL_GAZOLINE_MANQUEE])


def addCommande():
    usertype = ""
    v_qte_gallon_gazoline = 0.0
    v_qte_gallon_diesel = 0.0

    print("Pour placer une commande,")
    print(f"Veuillez choisir l'une de ces options:")
    print(f"1- {GAZOLINE_CONST}")
    print(f"2- {DIESEL_CONST}")
    print(f"3- LES DEUX(2)")
    print("0- Retour")

    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)

            # stop if user want to return
            if usertype == 0:
                return

            confirm_id = False
            confirm_id = confirm_identity()

            # stop if user not confirm the command
            if not confirm_id:
                print("\nVous avez choisi de ne pas continuer\n")
                return

            if usertype == GAZOLINE_CHOICE:
                v_qte_gallon_gazoline = getQteGallonGazolineToCommand()
                saveCommande(v_qte_gallon_gazoline=v_qte_gallon_gazoline, v_qte_gallon_diesel=0.0)
                return

            elif usertype == DIESEL_CHOICE:
                v_qte_gallon_diesel = getQteGallonDieselToCommand()
                saveCommande(v_qte_gallon_gazoline=0.0, v_qte_gallon_diesel=v_qte_gallon_diesel)
                return

            elif usertype == BOTH_GAZ_CHOICE:
                v_qte_gallon_diesel = getQteGallonDieselToCommand()
                v_qte_gallon_gazoline = getQteGallonGazolineToCommand()
                saveCommande(v_qte_gallon_gazoline=v_qte_gallon_gazoline, v_qte_gallon_diesel=v_qte_gallon_diesel)
                return

            else:
                print("Veuillez choisir une valeur entre 1 et 3")
        else:
            print("Entrer une valeur correcte, entre 1 et 3")


def saveCommande(v_qte_gallon_gazoline=0.0, v_qte_gallon_diesel=0.0):
    v_commande.enregistrer(qte_gallon_gazoline=v_qte_gallon_gazoline, qte_gallon_diesel=v_qte_gallon_diesel)


# ================================== AFFICHER TOUTES COMMANDE ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES COMMANDES |============")
    v_commande.afficher()
