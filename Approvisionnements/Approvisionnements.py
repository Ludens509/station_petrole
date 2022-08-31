import secrets
import functions


class Approvisionnement:
    def __init__(self,):
        self.station = str()
        self.id = int()
        self.date_app = str()
        self.qte_gallon_gazoline = float()
        self.qte_gallon_diesel = float()

    

    def enregistrer(self, id, station, qte_gallon_diesel, qte_gallon_gazoline, date_app):
        self.id = id
        self.station = station
        self.qte_gallon_diesel = qte_gallon_diesel
        self.qte_gallon_gazoline = qte_gallon_gazoline
        self.date_app = date_app

        functions.all_approvisionnements.update(
            [id, qte_gallon_diesel, qte_gallon_gazoline, date_app])
        print('\nSuccessfully saved!')

    def afficher(self, ):
        print("====LISTE DES APPROVISIONNEMENTS====")
        for i in range(len(functions.all_approvisionnements)):
            print(functions.all_approvisionnements[i], )
            # To verify if command exist
    def verify_command_exist(self):
        if functions.all_commandes == 0:
            print("Aucune commande n\á ete enregistrer:")
        else:
            print    
