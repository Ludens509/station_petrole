from re import T

import functions


class Station():
    # lalue, tabarre, clercine, petion_ville, all_station = dict(
    # ), dict(), dict(), dict(), dict()

    # dispo
    qte_gallon_gazoline_dispo = 0.0
    qte_gallon_diesel_dispo = 0.0
    # percent
    pourcentage_diesel = 0.0
    pourcentage_gazoline = 0.0

    def __int__(self):
        pass

    def construct(self, nom, capacite_gazoline, capacite_diesel):
        self.nom = nom
        self.capacite_gazoline = capacite_gazoline
        self.capacite_diesel = capacite_diesel

        self.qte_gallon_diesel_dispo = self.capacite_diesel
        self.qte_gallon_gazoline_dispo = self.capacite_gazoline
        # percent
        self.pourcentage_gazoline = self.qte_gallon_gazoline_dispo / self.capacite_gazoline * 100
        self.pourcentage_diesel = self.qte_gallon_diesel_dispo / self.capacite_diesel * 100

        if not (self.nom == functions.LALUE_CONST and self.nom == functions.TABARRE_CONST and self.nom == functions.CLECINE_CONST and self.nom != functions.PETION_VILLE_CONST):
            functions.all_station[self.nom].update({
                "nom": self.nom,
                "capacite_gazoline": self.capacite_gazoline,
                "capacite_diesel": self.capacite_diesel,
                "percent_diesel": self.pourcentage_diesel,
                "percent_gazoline": self.capacite_gazoline,
                "qte_dispo_gazoline": self.qte_gallon_gazoline_dispo,
                "qte_dispo_diesel": self.qte_gallon_diesel_dispo,
            })
            print('Successfully saved!')

    def getNom(self):
        return self.nom

    def getCapaciteGazoline(self, ):
        return self.capacite_gazoline

    def setCapaciteGazoline(self, newCapacite_gazoline):
        self.capacite_gazoline = newCapacite_gazoline

    def getCapaciteDisesel(self, ):
        return self.capacite_diesel

    def setCapaciteDiesel(self, newCapacite_diesel):
        self.capacite_diesel = newCapacite_diesel

    def getPourcentageGazoline(self, ):
        return self.pourcentage_gazoline

    def getPourcentageDiesel(self, ):
        return self.pourcentage_gazoline

    def enregistrer(self=None,):

        print("To save")
        print(f"{self.nom}")
        print(f"{self.capacite_gazoline}")

        try:
            if not (self.nom == functions.LALUE_CONST and self.nom == functions.TABARRE_CONST and self.nom == functions.CLECINE_CONST and self.nom != functions.PETION_VILLE_CONST):
                functions.all_station[self.nom].update({
                    "nom": self.nom,
                    "capacite_gazoline": self.capacite_gazoline,
                    "capacite_diesel": self.capacite_diesel,
                    "percent_diesel": self.pourcentage_diesel,
                    "percent_gazoline": self.capacite_gazoline,
                    "qte_dispo_gazoline":self.qte_gallon_gazoline_dispo,
                    "qte_dispo_diesel": self.qte_gallon_diesel_dispo,
                })
                print('Successfully saved!')

        except:
            print("An exception occurred")


    def afficher(self,):
        for k, val in functions.all_station.items():
            print(f"{k.upper()}\n")
            for cle, value in val.items():
                print(f"{cle} --> {value}")

            print("\n")


    def modifier(self, nom):
        pass
