from Approvisionnements.menu_aprovisionnements import show_all_approvisionnement, addApprovisionnement
from functions import clearConsole


def approvisionnement_menu():
    usertype = ""
    while True:
        print("============| MENU APPROVISIONNEMENT |============")
        print("1- Enregistrer un approvisionnement")
        print("2- Afficher toutes les approvisionnements")
        print("0- Retour")

        while True:
            usertype = input("R- ")
            if usertype.isdigit():
                usertype = int(usertype)
                if usertype >= 0 and usertype <= 2:
                    break
                else:
                    print("La valeur doit etre entre 0 et 2")
            else:
                print("Veuilez entrer une valeur entiere entre 0 et 2")

        # switch
        match usertype:
            case 1:
                addApprovisionnement()
                input("\nPress enter to continue\n")
            case 2:
                show_all_approvisionnement()
                input("\nPress enter to continue\n")
            case 0:
                input("\nRetour au menu Principal\nPress enter to continue\n")
                return clearConsole()
