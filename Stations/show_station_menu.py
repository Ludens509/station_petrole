from functions import all_station, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, PETION_VILLE_CONST, DIESEL_CONST, \
    DIESEL_CHOICE, retryFunc, GAZOLINE_CHOICE, GAZOLINE_CONST
from Stations.stations import Station

v_station = Station()


def findIfStationExist(name):
    for key, value in all_station.items():
        if name == key:
            return True
    return False


# function to ask name of a station
def askstationname(toChange=False):
    usertype = ""
    print(f"Veuillez choisir l'une de ces station:")
    print(f"1- {LALUE_CONST}")
    print(f"2- {TABARRE_CONST}")
    print(f"3- {CLERCINE_CONST}")
    print(f"4- {PETION_VILLE_CONST}")
    while True:
        usertype = input("R- ")

        if usertype.isdigit():

            if int(usertype) == 1:
                usertype = LALUE_CONST
                is_exist = findIfStationExist(usertype)
                if is_exist and not toChange:
                    print("Cette station existe deja, si vous souhaitez la modifier, choissez l'option qui convient")
                else:
                    break
            elif int(usertype) == 2:
                usertype = TABARRE_CONST
                is_exist = findIfStationExist(usertype)
                if is_exist and not toChange:
                    print("Cette station existe deja, si vous souhaitez la modifier, choissez l'option qui convient")
                else:
                    break
            elif int(usertype) == 3:
                usertype = CLERCINE_CONST
                is_exist = findIfStationExist(usertype)
                if is_exist and not toChange:
                    print("Cette station existe deja, si vous souhaitez la modifier, choissez l'option qui convient")
                else:
                    break
            elif int(usertype) == 4:
                usertype = PETION_VILLE_CONST
                is_exist = findIfStationExist(usertype)
                if is_exist and not toChange:
                    print("Cette station existe deja, si vous souhaitez la modifier, choissez l'option qui convient")
                else:
                    break
            else:
                print("Veuillez choisir une valeur entre 1 et 4")
        else:
            print("Entrer une valeur correcte, entre 1 et 4")

    return usertype


# functon to ask capacity
def ask_capacity(type_galon):
    usertype = ""
    while True:
        usertype = input(f"Veuillez entrer sa capacite en {type_galon}: ")
        if usertype.isdigit():
            usertype = float(usertype)
            if 100 <= usertype <= 1000000000000:
                break
            else:
                print("Entrer une acceptable entre (100 entre 1000000000000")
        else:
            print("Incorrect! Veuillez un nombre")
    return usertype


# function to ask_choice_which_capacity
def ask_which_capacity():
    usertype = ""
    while True:
        usertype = input(f"Choisissez l'une de ces capacites:\n1- {GAZOLINE_CONST}\n2-{DIESEL_CONST}\nR- ")
        if usertype.isdigit():
            if int(usertype) == GAZOLINE_CHOICE or int(usertype) == DIESEL_CHOICE:
                usertype = int(usertype)
                break
            else:
                print(f"Le choix doit etre {GAZOLINE_CHOICE} ou {DIESEL_CHOICE}")
        else:
            print("Inccorrect! veuillez entrer un chiffre")

    # condition ternaire :
    # val_if_true if condition else val_if_false
    return GAZOLINE_CONST if (usertype == GAZOLINE_CHOICE) else DIESEL_CONST


def addStation():
    usertype = ""
    nomstation = ""
    capacitegazoline = 0.0
    # percentgazoline = 0.0
    capacitediesel = 0.0
    # percentdiesel = 0.0

    while True:
        print("============| AJOUT D'UNE STATION |============")
        # Entrer le nom
        nomstation = askstationname()

        # Entrer capacite gazoline
        capacitegazoline = ask_capacity("gazoline")

        # Entrer capacite diesel
        capacitediesel = ask_capacity("diesel")

        # print(f"\n\nNom: {nomstation}\nCapacite gazol: {capacitegazoline}\nCapacite die: {capacitediesel}")
        v_station.enregistrer(nom=nomstation, capacite_gazoline=capacitegazoline, capacite_diesel=capacitediesel)

        valueReturn = retryFunc()
        if valueReturn == 0:
            break


# ================================== MODIFIER CAPACITE GALON ===============================

def show_edit_galon():
    usertype = ""
    nomstation = ""
    type_capacite = ""
    nvle_capacite = 0.0

    while True:
        print("============| MODIFIER GALON STATION |============")
        # Entrer le nom de la station
        nomstation = askstationname(toChange=True)

        # Entrer capacite gazoline
        type_capacite = ask_which_capacity()

        # Entrer capacite diesel
        nvle_capacite = ask_capacity(type_capacite)

        v_station.modifier(nom=nomstation, typeCapacite=type_capacite, nouvellevaleur=nvle_capacite)

        valueReturn = retryFunc()
        if valueReturn == 0:
            break


# ================================== AFFICHER TOUTES STATIONS ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES STATIONS |============")
    v_station.afficher()
