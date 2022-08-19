import os
LALUE_CONST = "lalue"
TABARRE_CONST = "tabarre"
CLECINE_CONST = "clercine"
PETION_VILLE_CONST = "petion-ville"

all_station = {}

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
