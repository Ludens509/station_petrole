
from Stations.Stations import StationClass
from functions import ANNULER_OPTION, findIfStationExist, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, \
    PETION_VILLE_CONST, GAZOLINE_CONST, DIESEL_CONST, retryFunc

v_station = StationClass()
reponse_in_function = None

# ========================= function

# function to ask name of a station
def askstationname():
    usertype = ""
    print(f"Veuillez choisir l'une de ces station:")
    print(f"1- {LALUE_CONST}")
    print(f"2- {TABARRE_CONST}")
    print(f"3- {CLERCINE_CONST}")
    print(f"4- {PETION_VILLE_CONST}")
    print(f"0- Annuler")

    while True:
        usertype = input("R- ")

        if usertype.isdigit():
            if int(usertype) == 0:
                usertype = ANNULER_OPTION
                break

            elif int(usertype) == 1:
                usertype = LALUE_CONST
                break

            elif int(usertype) == 2:
                usertype = TABARRE_CONST
                break

            elif int(usertype) == 3:
                usertype = CLERCINE_CONST
                break

            elif int(usertype) == 4:
                usertype = PETION_VILLE_CONST
                break

            else:
                print("Veuillez choisir une valeur entre 0 et 4")
        else:
            print("Entrer une valeur correcte, entre 0 et 4")

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
    print("fChoisissez l'une de ces capacites:")
    print(f"1- {GAZOLINE_CONST}\n"
          f"2- {DIESEL_CONST}\n"
          f"3- Les deux(2)\n"
          f"0- Annuler")
    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)
            if 0 <= usertype <= 3:
                return usertype
            else:
                print(f"Le choix doit etre 0 et 3")
        else:
            print("Inccorrect! veuillez entrer un chiffre")


# ================================== AJOUTER CAPACITE GALON ===============================

def addStation():
    usertype = ""
    nomstation = ""
    capacitegazoline = 0.0
    capacitediesel = 0.0

    while True:
        print("============| AJOUT D'UNE STATION |============")
        # Entrer le nom
        while True:
            reponse_in_function = askstationname()

            if reponse_in_function == ANNULER_OPTION:
                return
            elif not findIfStationExist(reponse_in_function):
                nomstation = reponse_in_function
                break
            else:
                print("Cette station existe deja! Faites un autre choix")
                input("\nPress Enter to continue")

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
    response_in_function = ""
    nomstation = ""
    type_capacite = ""
    nvle_capacite = 0.0

    while True:
        print("============| MODIFIER GALLON STATION |============")
        # Entrer le nom de la station
        while True:
            reponse_in_function = askstationname()

            if reponse_in_function == ANNULER_OPTION:
                return
            elif findIfStationExist(reponse_in_function):
                nomstation = reponse_in_function
                break
            else:
                print("Cette station n'existe pas encore! Faites un autre choix")
                input("\nPress Enter to continue")

        # Entrer capacite gazoline
        # type_capacite = ask_which_capacity()
        response_in_function = ask_which_capacity()
        if reponse_in_function == 0:
            return
        else:
            if response_in_function == 1:
                # capacite gazoline
                type_capacite = GAZOLINE_CONST
                nvle_capacite = ask_capacity(type_capacite)
                v_station.modifier(nom=nomstation, typeCapacite=type_capacite, nouvellevaleur=nvle_capacite)

            elif response_in_function == 2:
                # capacite diesel
                type_capacite = DIESEL_CONST
                nvle_capacite = ask_capacity(type_capacite)
                v_station.modifier(nom=nomstation, typeCapacite=type_capacite, nouvellevaleur=nvle_capacite)

            else:
                # capacite gazoline
                type_capacite = GAZOLINE_CONST
                nvle_capacite = ask_capacity(type_capacite)
                v_station.modifier(nom=nomstation, typeCapacite=type_capacite, nouvellevaleur=nvle_capacite)
                # capacite diesel
                type_capacite = DIESEL_CONST
                nvle_capacite = ask_capacity(type_capacite)
                v_station.modifier(nom=nomstation, typeCapacite=type_capacite, nouvellevaleur=nvle_capacite)

        valueReturn = retryFunc()
        if valueReturn == 0:
            break


# ================================== AFFICHER TOUTES STATIONS ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES STATIONS |============")
    v_station.afficher()




# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     askstationname()
#     ask_capacity()
#     ask_which_capacity()
#
