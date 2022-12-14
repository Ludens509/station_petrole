import functions
from Ventes.menu_ventes import addVente, show_all_ventes


def ventes_menu():
    userType = ""
    while True:
        print("============| MENU VENTES |============")
        print("1- Enregistrer une vente")
        print("2- Afficher toutes les ventes")
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
                addVente()
                input("\nPress enter to continue\n")
            case 2:
                show_all_ventes()
                input("\nPress enter to continue\n")
            case 0:
                input("\nRetour au menu Principal\nPress enter to continue\n")
                # functions.clearConsole()
                break
