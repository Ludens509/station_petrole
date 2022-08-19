import functions
from Stations.show_station_menu import show_all, show_edit_galon, addStation

def station_menu():
    userType = ""
    while True:
        print("============| MENU STATION |============")
        print("1- Enregistrer une station")
        print("2- Modifier quantité gallon pour une station")
        print("3- Afficher toutes les stations")
        print("0- Retour")

        while True:
            userType = input("R- ")
            if userType.isdigit():
                userType = int(userType)
                if userType >= 0 and userType <= 4:
                    break
                else:
                    print("La valeur doit etre entre 0 et 4")
            else:
                print("Veuilez entrer une valeur entiere entre 0 et 4")

        # switch
        match userType:
            case 1:
                addStation()
                input("\nPress enter to continue\n")
            case 2:
                show_edit_galon()
                input("\nPress enter to continue\n")
            case 3:
                show_all()
                input("\nPress enter to continue\n")
            case 0:
                input("\nRetour au menu Principal\nPress enter to continue\n")
                functions.clearConsole()
                break

# ================================= LOGIQUE FOR EDIT GALON =========
def edit_galon(nom_station, type_capacite, valeur):
    pass
