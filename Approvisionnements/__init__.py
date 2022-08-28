from functions import clearConsole
from Approvisionnements.menu_approvisionnements import show_all, addApprovisionnement

def approvisionnement_menu():
    usertype = ""
    while True:
        print("============| MENU APPROVISIONNEMENTS |============")
        print("1- Enregistrer un approvisionnement")
        print("2- Afficher toutes les approvisionnement")
        print("0- Retour")

        while True:
            userType = input("R- ")
            if userType.isdigit():
                userType = int(userType)
                if userType >= 0 and userType <= 2:
                    break
                else:
                    print("La valeur doit etre entre 0 et 2")
            else:
                print("Veuilez entrer une valeur entiere entre 0 et 2")

        # switch
        match userType:
            case 1:
                addApprovisionnement()
                input("\nPress enter to continue\n")
            case 2:
                show_all()
                input("\nPress enter to continue\n")
            case 0:
                input("\nRetour au menu Principal\nPress enter to continue\n")
                return clearConsole()
