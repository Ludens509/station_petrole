from Stations.index import station_menu

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
                input("\nPress enter to continue\n")
            case 2:
                print("Case 2")
                input("\nPress enter to continue\n")
            case 3:
                print("Case 3")
                input("\nPress enter to continue\n")
            case 4:
                print("Case 4")

                input("\nPress enter to continue\n")
            case 0:
                print("Case 0")
                print("Domaine name: inuka.edu")
                print("IP: 192.168.40.1/24 ")
                print("\n\n\t\t G O O D   B Y E  !\n\n")
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_main_menu()
