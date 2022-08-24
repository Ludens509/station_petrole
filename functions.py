import os
LALUE_CONST = "lalue"
TABARRE_CONST = "tabarre"
CLERCINE_CONST = "clercine"
PETION_VILLE_CONST = "petion-ville"

GAZOLINE_CONST = "gazoline"
DIESEL_CONST = "diesel"
GAZOLINE_CHOICE = 1
DIESEL_CHOICE = 2
BOTH_GAZ_CHOICE = 3
QTE_GAL_GAZOLINE = "qte_dispo_gazoline"
QTE_GAL_DIESEL = "qte_dispo_disel"

all_station = {}
all_commande = ()

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
