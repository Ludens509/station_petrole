import functions

GAZOLINE_CONST ="gazoline"
DIESEL_CONST ="diesel"
GAZOLINE_CHOICE = 1
DIESEL_CHOICE = 2

# function to ask name of a station
def askstationname():
    usertype = ""
    print(f"Veuillez choisir l'une de ces station:")
    print(f"1- {functions.LALUE_CONST}")
    print(f"2- {functions.TABARRE_CONST}")
    print(f"3- {functions.CLECINE_CONST}")
    print(f"4- {functions.PETION_VILLE_CONST}")
    while True:
        usertype = input("R- ")

        if usertype.isdigit():
            if int(usertype) == 1:
                usertype= functions.LALUE_CONST
                break
            elif int(usertype) == 2:
                usertype= functions.TABARRE_CONST
                break
            elif int(usertype) == 3:
                usertype = functions.CLECINE_CONST
                break
            elif int(usertype) == 4:
                usertype = functions.PETION_VILLE_CONST
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
    return GAZOLINE_CONST if (usertype== GAZOLINE_CHOICE) else DIESEL_CONST


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
        nomstation=askstationname()

        # Entrer capacite gazoline
        capacitegazoline= ask_capacity("gazoline")

        # Entrer capacite diesel
        capacitediesel= ask_capacity("diesel")

        print(f"\n\nNom: {nomstation}\nCapacite gazol: {capacitegazoline}\nCapacite die: {capacitediesel}")

        valueReturn = functions.retryFunc()
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
        nomstation = askstationname()

        # Entrer capacite gazoline
        type_capacite = ask_which_capacity()

        # Entrer capacite diesel
        nvle_capacite = ask_capacity(type_capacite)

        valueReturn = functions.retryFunc()
        if valueReturn == 0:
            break

# ================================== AFFICHER TOUTES STATIONS ===============================

def show_all():
    print("\n\n============| AFFICHER TOUTES LES STATIONS |============")

    print(f"\n{functions.LALUE_CONST.upper()}")
    print(f"\tQte gazoline: {2993}")
    print(f"\t% gazoline: {93}%")
    print(f"\tQte diesel: {424}")
    print(f"\t% diesel: {100}%")

    print(f"\n{functions.TABARRE_CONST.upper()}")
    print(f"\tQte gazoline: {2993}")
    print(f"\t% gazoline: {93}%")
    print(f"\tQte diesel: {424}")
    print(f"\t% diesel: {100}%")

    print(f"\n{functions.CLECINE_CONST.upper()}")
    print(f"\tQte gazoline: {2993}")
    print(f"\t% gazoline: {93}%")
    print(f"\tQte diesel: {424}")
    print(f"\t% diesel: {100}%")

    print(f"\n{functions.PETION_VILLE_CONST.upper()}")
    print(f"\tQte gazoline: {2993}")
    print(f"\t% gazoline: {93}%")
    print(f"\tQte diesel: {424}")
    print(f"\t% diesel: {100}%")
