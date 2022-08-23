import secrets, functions

from functions import all_commande, all_station, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, PETION_VILLE_CONST, \
    DIESEL_CONST, \
    DIESEL_CHOICE, retryFunc, GAZOLINE_CHOICE, GAZOLINE_CONST
from Commandes.commandes import Commande
from Stations.stations import Station

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


def askifexist(self, ):
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

        if usertype == askifexist:
            usertype = askifexist()
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
        elif usertype == askifexist:
            usertype = TABARRE_CONST
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
        elif usertype == askifexist:
            usertype = CLERCINE_CONST
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
        elif usertype == askifexist:
            usertype = PETION_VILLE_CONST
            is_exist = findIfStationExist(usertype)
            if is_exist and not toChange:
                print("Cette station existe deja,  vous pouvez donc effectuer votre commmande")
            else:
                print("Cette station n\'existe pas donc impossible de passe une commande")
                break
    return usertype


# functon to ask capacity
def ask_commande(type_galon):
    choix = ""
    while True:
        v_station.afficher()
        choix = input(f"Veuillez entrer sa capacite en {type_galon}: ")
        if usertype.isdigit():
            usertype = float(usertype)
            if 100 <= usertype <= 1000000000000:
                break
            else:
                print("Entrer une acceptable entre (100 entre 1000000000000")
        else:
            print("Incorrect! Veuillez un nombre")
    return usertype


def addCommande():
    usertype = ""

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
