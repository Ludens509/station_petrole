from stations import Station

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
          nom=''
          
          while(nom != "Lalue" or nom !="Tabarre" or nom !="Clercine" or nom !="Petion-ville"):
            nom =input("Entrer le nom de la zones( Lalue, Tabarre, Clercine et Pétion-ville): ")
          
          capacite_gazoline=0
          while(capacite_gazoline <= 0 ):
            capacite_gazoline= int(input("Entrer la capacite en Gazoline"))

            capacite_diesel=0
          while(capacite_diesel < 0 ):  
            capacite_diesel= int(input("Entrer la capacite en Diesel"))

          qte_gallon_dispo = 0
          while(qte_gallon_dispo <=0  and qte_gallon_dispo>capacite_gazoline):
            qte_gallon_dispo= input("Entrer la quantite de gallons disponible ")

          station = Station(nom,capacite_gazoline,pourcentage_gazoline,pourcentage_diesel,capacite_diesel)
          station.enregistrer(nom)
          input("Presser (Enter) pour continuez!")
        case 'b':
           
           input("Presser (Enter) pour continuez!")
        case 'c':
           print
        case 'd':
          print
        case 'e':
           print
                                 
        case 'i':
            b1 = False
            print('over')
        case other:
            print('wrong choice')