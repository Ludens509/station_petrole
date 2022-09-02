
import functions
class Approvisionnement:
    def __init__(self, id, station, qte_gallon_diesel, qte_gallon_gazoline, date_app):
        self.id=id
        self.station = station
        self.qte_gallon_diesel = qte_gallon_diesel
        self.qte_gallon_gazoline = qte_gallon_gazoline
        self.date_app = date_app



    # def enregistrer(self, station, qte_gallon_diesel, qte_gallon_gazoline):
    #     self.id = self.generer_id()
    #     self.station = station
    #     self.qte_gallon_diesel = qte_gallon_diesel
    #     self.qte_gallon_gazoline = qte_gallon_gazoline
    #     self.date_app = functions.generer_date()


    def afficher(self):
    
        print('-------------->>> ', self.station, ' <<<-------------')
        print('| ID ------------------------->>>', self.id)
        print('| Quantite gallon diesel ----->>>', self.qte_gallon_diesel, 'gallon')
        print('| Quantite gallon gazoline---->>>', self.qte_gallon_gazoline, 'gallon')
        print('| Date approvisionnement ----->>>', self.date_app)
        print('----------------------------------------------------')
        input("Pressez pour continuer")

            # To verify if command exist
    def verify_command_exist(self):
        if functions.all_commandes == 0:
            print("Aucune commande n\á ete enregistrer:")
        else:
            print    
