from functions import GAZOLINE_CONST, CAPACITE_GAZOLINE, CAPACITE_DIESEL, QTE_GAL_GAZOLINE_DISPO, QTE_GAL_DIESEL_DISPO, PERCENT_GAL_GAZOLINE, PERCENT_GAL_DIESEL

import functions


class StationClass:

    def __init__(self):
        self.nom = str
        self.capacite_gazoline = float
        self.capacite_diesel = float
        # dispo
        self.qte_gallon_gazoline_dispo = 0.0
        self.qte_gallon_diesel_dispo = 0.0
        # percent
        self.pourcentage_diesel = 0.0
        self.pourcentage_gazoline = 0.0

    def enregistrer(self, nom: str, capacite_gazoline: float, capacite_diesel: float):
        self.nom = nom
        self.capacite_gazoline = capacite_gazoline
        self.capacite_diesel = capacite_diesel

        # functions to change percent
        self.changePourcentageGazoline(nom=nom)
        self.changePourcentageDiesel(nom=nom)

        if self.nom == functions.LALUE_CONST or self.nom == functions.TABARRE_CONST \
                or self.nom == functions.CLERCINE_CONST \
                or self.nom == functions.PETION_VILLE_CONST :
            functions.all_stations.update({
                self.nom: {
                    CAPACITE_GAZOLINE: self.capacite_gazoline,
                    CAPACITE_DIESEL: self.capacite_diesel,
                    QTE_GAL_GAZOLINE_DISPO: self.qte_gallon_gazoline_dispo,
                    QTE_GAL_DIESEL_DISPO: self.qte_gallon_diesel_dispo,
                    PERCENT_GAL_GAZOLINE: self.pourcentage_gazoline,
                    PERCENT_GAL_DIESEL: self.pourcentage_diesel,
                }})
            print('\nSuccessfully saved!')
            input("\nPress any key to continue")
        else:
            print("\nErreur d'enregistrement")
            input("\nPress any key to continue")

    def getNom(self):
        return self.nom

    def getCapaciteGazoline(self, ):
        return self.capacite_gazoline

    def setCapaciteGazoline(self, nom: str, newCapacite_gazoline:float):
        self.capacite_gazoline = newCapacite_gazoline
        functions.all_stations[nom][CAPACITE_GAZOLINE] = newCapacite_gazoline
        # functions to change percent
        self.changePourcentageGazoline(nom=nom)


    def getCapaciteDisesel(self,):
        return self.capacite_diesel

    def setCapaciteDiesel(self, nom: str, newCapacite_diesel: float):
        self.capacite_diesel = newCapacite_diesel
        functions.all_stations[nom][CAPACITE_DIESEL] = newCapacite_diesel
        # functions to change percent
        self.changePourcentageDiesel(nom=nom)

    def getPourcentageGazoline(self, ) -> float:
        return self.pourcentage_gazoline

    def changePourcentageGazoline(self, nom: str):
        self.pourcentage_gazoline = self.qte_gallon_gazoline_dispo / self.capacite_gazoline * 100
        if functions.findIfStationExist(nom) :
            functions.all_stations[nom][functions.PERCENT_GAL_GAZOLINE] = self.pourcentage_gazoline

    def getPourcentageDiesel(self, ):
        return self.pourcentage_gazoline

    def changePourcentageDiesel(self, nom: str ):
        self.pourcentage_diesel = self.qte_gallon_diesel_dispo / self.capacite_diesel * 100
        if functions.findIfStationExist(nom):
            functions.all_stations[nom][CAPACITE_DIESEL] = self.pourcentage_diesel

    def afficher(self, ):
        for k, val in functions.all_stations.items():
            if val.items():
                print(f"\n{k.upper()}\n")
                for cle, value in val.items():
                    if 'percent' in cle:
                        print(f"{cle.replace('_', ' ')} -> {value}%")
                    else:
                        print(f"{cle.replace('_', ' ')} -> {value}")

    def modifier(self, nom: str, typeCapacite: str, nouvellevaleur: float):
        """
        :type nom: str
        :type typeCapacite: str
        :type nouvellevaleur : float
        """
        if typeCapacite == GAZOLINE_CONST:
            self.setCapaciteGazoline(nom, nouvellevaleur)
            self.changePourcentageGazoline(nom=nom)
        else:
            self.setCapaciteDiesel(nom, nouvellevaleur)
            self.changePourcentageDiesel(nom=nom)

        print("Changed successfully!")

    @staticmethod
    def substractItems(item1:  float, item2:float)->float:
        return item1 - item2

    def afficherQuantiteGallon(self, ):
        for k, val in functions.all_stations.items():
            if val.items():
                print(f"\n{k.upper()}\n")
                print(f"qte gazoline dispo -> {self.substractItems(val[CAPACITE_GAZOLINE], val[QTE_GAL_GAZOLINE_DISPO])}")
                print(f"qte gazoline consommee -> {val['qte_dispo_gazoline']}")
                print(f"qte diesel dispo -> {val['qte_dispo_diesel']}")
