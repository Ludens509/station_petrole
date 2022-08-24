
import secrets

import functions
from Commandes.commandes import Commande
from Stations.stations import Station
from functions import all_station,all_commande, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, PETION_VILLE_CONST, \
    DIESEL_CHOICE, retryFunc, BOTH_GAZ_CHOICE, GAZOLINE_CHOICE

v_station = Station()
v_commande = Commande()


def findIfStationExist(name):
    for key, value in all_station.items():
        if name == key:
            return True
    return False


# function for generate Id
def generer_id():
    # generate 1 secure random numbers between 10 and 500
    for x in range(0, 1):
        secret_id = 10 + secrets.randbelow(500)
        print(secret_id)  # for show but no need
    return secret_id


def qte_gallon_diesel():
    qte_gallon_diesel = (1.10 * v_commande.total_gallon_diesel_maquant())
    return qte_gallon_diesel

def qte_gallon_gazoline():
    qte_gallon_gazoline = (1.25 * v_commande.total_gallon_gazoline_maquant())
    return qte_gallon_gazoline

def askifexist():
    cle =""
    for key in functions.all_station.keys():
        if key == LALUE_CONST:
            cle = LALUE_CONST
        elif key == TABARRE_CONST:
            cle = TABARRE_CONST
        elif key == CLERCINE_CONST:
            cle = CLERCINE_CONST
        elif key == PETION_VILLE_CONST:
            cle = PETION_VILLE_CONST
    return cle

# function to ask name of a station
def askstationname(toChange=False):
    usertype = ""

    while True:

        if usertype == askifexist():
            usertype = askifexist()
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
        elif usertype == askifexist():
            usertype = askifexist()
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
        elif usertype == askifexist():
            usertype = askifexist()
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
        elif usertype == askifexist():
            usertype = askifexist()
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
    return usertype


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
    print(f"3- {BOTH_GAZ_CHOICE }")
    while True:
      usertype = input("R- ") 
      if usertype.isdigit():
            if int(usertype) == 1:
                if confirm_commande() == 1:
                    addCommande()
                else:
                    valueReturn = retryFunc()
                    if valueReturn == 0:
                        break
            elif int(usertype) == 2:
                if confirm_commande() == 1:
                    addCommande()
                else:
                    valueReturn = retryFunc()
                    if valueReturn == 0:
                        break
            
            elif int(usertype) == 3:
                if confirm_commande() == 1:
                 addCommande()
                else:
                    valueReturn = retryFunc()
                    if valueReturn == 0:
                        break
                
            else:
                print("Veuillez choisir une valeur entre 1 et 3")
      else:
        print("Entrer une valeur correcte, entre 1 et 3")





def addCommande():

    while True:

        print("============| AJOUT D'UNE COMMANDE |============")

        v_commande.enregistrer()

        valueReturn = retryFunc()
        if valueReturn == 0:
            break


# ================================== AFFICHER TOUTES COMMANDE ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES STATIONS |============")
    v_station.afficher()
