import functions
from Approvisionnements import approvisionnement_menu
from Commandes.__init__ import commande_menu
from Stations import station_menu
from Ventes import ventes_menu


def show_main_menu():
    userType = ""
    while True:
        print("============| MENU PRINCIPAL |============")
        print("1- Station")
        print("2- Commandes")
        print("3- Approvisionnement")
        print("4- Vente")
        print("0- Quitter")

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
                station_menu()
                # functions.clearConsole()
            case 2:
                commande_menu()
            case 3:
                approvisionnement_menu()
            case 4:
                ventes_menu()
                # functions.clearConsole()
                input("\nPress enter to continue\n")
            case 0:
                print("Case 0")
                print("\n\n\t\t G O O D   B Y E  !\n\n")
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_main_menu()
