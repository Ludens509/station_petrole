import functions


class Approvisionnement:
    def __init__(self):
       pass

    def enregistrer(self, id, station, qte_gallon_diesel, qte_gallon_gazoline, date_app):
        self.id = id
        self.station =station
        self.qte_gallon_diesel = qte_gallon_diesel
        self.qte_gallon_gazoline = qte_gallon_gazoline
        self.date_app = date_app

        functions.all_approvisionnements.update([id, qte_gallon_diesel, qte_gallon_gazoline, date_commande, etat])
        print('\nSuccessfully saved!')

    def afficher(self, ):
        print("====LISTE DES APPROVISIONNEMENTS====")
        for i in range(len(functions.all_approvisionnements)):
            print(functions.all_approvisionnements[i], )
