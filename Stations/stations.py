from re import T
from functions import GAZOLINE_CONST

import functions


class Station():

    # dispo
    qte_gallon_gazoline_dispo = 0.0
    qte_gallon_diesel_dispo = 0.0
    # percent
    pourcentage_diesel = 0.0
    pourcentage_gazoline = 0.0

    def __int__(self):
        pass

    def enregistrer(self, nom, capacite_gazoline, capacite_diesel):
        self.nom = nom
        self.capacite_gazoline = capacite_gazoline
        self.capacite_diesel = capacite_diesel

        # functions to change percent
        self.changePourcentageGazoline()
        self.changePourcentageDiesel()

        if not (self.nom == functions.LALUE_CONST and self.nom == functions.TABARRE_CONST and self.nom == functions.CLERCINE_CONST and self.nom != functions.PETION_VILLE_CONST):
            functions.all_station.update({
                self.nom: {
                    "nom": self.nom,
                    "capacite_gazoline": self.capacite_gazoline,
                    "capacite_diesel": self.capacite_diesel,
                    "percent_diesel": self.pourcentage_diesel,
                    "percent_gazoline": self.capacite_gazoline,
                    "qte_dispo_gazoline": self.qte_gallon_gazoline_dispo,
                    "qte_dispo_diesel": self.qte_gallon_diesel_dispo,
            }})
            print('\nSuccessfully saved!')


    def getNom(self):
        return self.nom

    def getCapaciteGazoline(self, ):
        return self.capacite_gazoline

    def setCapaciteGazoline(self, newCapacite_gazoline):
        self.capacite_gazoline = newCapacite_gazoline
        # functions to change percent
        self.changePourcentageGazoline()

    def getCapaciteDisesel(self, ):
        return self.capacite_diesel

    def setCapaciteDiesel(self, newCapacite_diesel):
        self.capacite_diesel = newCapacite_diesel
        # functions to change percent
        self.changePourcentageDiesel()

    def getPourcentageGazoline(self, ):
        return self.pourcentage_gazoline

    def changePourcentageGazoline(self, ):
        self.pourcentage_gazoline = self.qte_gallon_gazoline_dispo / self.capacite_gazoline * 100

    def getPourcentageDiesel(self, ):
        return self.pourcentage_gazoline

    def changePourcentageDiesel(self,):
        self.pourcentage_diesel = self.qte_gallon_diesel_dispo / self.capacite_diesel * 100

    def afficher(self,):
        for k, val in functions.all_station.items():
            if val.items():
                print(f"\n{k.upper()}\n")
                for cle, value in val.items():
                    print(f"{cle}       --> {value}")

    def modifier(self,nom, typeCapacite, nouvellevaleur):

        print("To change: ", typeCapacite)
        if typeCapacite == GAZOLINE_CONST:
            functions.all_station[nom]["capacite_gazoline"] = nouvellevaleur
        else:
            functions.all_station[nom]["capacite_diesel"] = nouvellevaleur
        print("Changed successfully!")

# all_station={
#     "lalue":{
#         "capacite_gazoline": 33
#     }
# }