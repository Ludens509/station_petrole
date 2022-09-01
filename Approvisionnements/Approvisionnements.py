import secrets
import functions


class Approvisionnement:
    def __init__(self,):
        self.station = str()
        self.id = int()
        self.date_app = str()
        self.qte_gallon_gazoline = float()
        self.qte_gallon_diesel = float()

    def generer_id(self, ) -> str:
        # generate 1 secure random numbers between 10 and 500
        for x in range(0, 1):
            secret_id = (10 + secrets.randbelow(500)).__str__()
        # recursive function : get unique ID in all_commandes
        if functions.findCommandeById(secret_id):
            self.generer_id()
        return secret_id

    def enregistrer(self, station, qte_gallon_diesel, qte_gallon_gazoline):
        self.id = self.generer_id()
        self.station = station
        self.qte_gallon_diesel = qte_gallon_diesel
        self.qte_gallon_gazoline = qte_gallon_gazoline
        self.date_app = functions.generer_date()

        functions.all_approvisionnements.update(
            [self.id, qte_gallon_diesel, qte_gallon_gazoline, self.date_app])
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
