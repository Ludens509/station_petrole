from Stations.stations import Station

lalue, tabarre, clercine, pv = 'Lalue', 'Tabarre', 'Clercine', 'Petion-ville'
b1 = True
while (b1):
    print('\n******  *************MENU***************** ******|')
    print(' a)  Enregistrer une station:                      |')
    print(' b)  Modifier quantite en Gazoline:                |')
    print(' c)  Modifier la quantite en Diesel:               |')
    print(' d)  Afficher les stations:                        |')
    print('\n******  *************COMMANDE************* ******|')
    print(' e) Quitter\n')
    choix = input('saisir la lettre de votre choix: ')

    match choix:
        case 'a':
            nom = ''
            while not (nom.casefold() == lalue.casefold() or nom.casefold() == tabarre.casefold() or nom.casefold() == clercine.casefold() or nom.casefold() == pv.casefold()):
                nom = input(
                    "Entrer le nom de la zones( Lalue, Tabarre, Clercine et Pétion-ville): ")

            capacite_gazoline = 0
            while capacite_gazoline <= 0:
                capacite_gazoline = int(
                    input("Entrer la capacite en Gazoline: "))

                capacite_diesel = 0
            while capacite_diesel <= 0:
                capacite_diesel = int(input("Entrer la capacite en Diesel: "))

            qte_gallon_gazoline_dispo = 0
            if qte_gallon_gazoline_dispo <= capacite_gazoline:
                qte_gallon_gazoline_dispo = int(
                    input("Entrer la quantite de gallons gazoline disponible: "))
                pourcentage_gazoline = (
                    qte_gallon_gazoline_dispo * 100) / capacite_gazoline
            else:
                print('No')

            qte_gallon_diesel_dispo = 0
            if qte_gallon_diesel_dispo <= capacite_diesel:
                qte_gallon_diesel_dispo = int(
                    input("Entrer la quantite de gallons diesel disponible: "))
                pourcentage_diesel = (
                    qte_gallon_diesel_dispo * 100) / capacite_diesel

                station = Station(nom, capacite_gazoline, capacite_diesel,
                                  pourcentage_gazoline, pourcentage_diesel)
                station.enregistrer(nom)
            else:
                print('No')
            input("Presser (Enter) pour continuez!")
        case 'b':

            input("Presser (Enter) pour continuez!")
        case 'c':
            print
        case 'd':
            station.afficher(nom)
            input("Presser (Enter) pour continuez!")
        case 'e':
            b1 = False
            print('over')

        case 'i':
            pass
        case other:
            print('wrong choice')
