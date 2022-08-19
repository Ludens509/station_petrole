from re import T


class Station():
    lalue, tabarre, clercine, petion_ville, all_station = dict(), dict(), dict(), dict(), dict()
    

    def __init__(self, nom, capacite_gazoline, capacite_diesel, pourcentage_gazoline, pourcentage_diesel):
        self.nom = nom
        self.capacite_gazoline = capacite_gazoline
        self.capacite_diesel = capacite_diesel
        self.pourcentage_gazoline = pourcentage_gazoline
        self.pourcentage_diesel = pourcentage_diesel

        def getNom():
            return self.nom

        def getCapaciteGazoline():
            return self.capacite_gazoline

        def setCapaciteGazoline(newCapacite_gazoline):
            self.capacite_gazoline = newCapacite_gazoline

        def getCapaciteDisesel():
            return self.capacite_diesel

        def setCapaciteDiesel(newCapacite_diesel):
            self.capacite_diesel = newCapacite_diesel

        def getPourcentageGazoline():
            return self.pourcentage_gazoline

        def getPourcentageDiesel():
            return self.pourcentage_gazoline

    def enregistrer(self, nom):
        if self.nom == "Lalue":
            Station.lalue.update(
                {"nom": self.nom, "capacite Gazoline": self.capacite_gazoline, "capacite Diesel": self.capacite_diesel
                    , "% Diesel": self.pourcentage_diesel, "%tage Gazoline": self.pourcentage_gazoline})
            print('Successfully saved!')
        elif self.nom == "Tabarre":
            Station.tabarre.update(
                {"nom": self.nom, "capacite Gazoline": self.capacite_gazoline, "capacite Diesel": self.capacite_diesel
                    , "% Diesel": self.pourcentage_diesel, "%tage Gazoline": self.pourcentage_gazoline})
            print('Successfully saved!')
        elif self.nom == "Clercine":
            Station.clercine.update(
                {"nom": self.nom, "capacite Gazoline": self.capacite_gazoline, "capacite Diesel": self.capacite_diesel
                    , "% Diesel": self.pourcentage_diesel, "%tage Gazoline": self.pourcentage_gazoline})
            print('Successfully saved!')
        else:
            Station.petion_ville.update(
                {"nom": self.nom, "capacite Gazoline": self.capacite_gazoline, "capacite Diesel": self.capacite_diesel
                    , "% Diesel": self.pourcentage_diesel, "%tage Gazoline": self.pourcentage_gazoline})
            print('Successfully saved!')
            
    def afficher(self,nom):
         
       for cle, value in enumerate(Station.lalue.items()):
         print(cle, value, sep="--=> ")
       for cle, value in enumerate(Station.tabarre.items()):  
         print(cle, value, sep="--=> ")
       for cle, value in enumerate(Station.clercine.items()):  
         print(cle, value, sep="--=> ")
       for cle, value in enumerate(Station.petion_ville.items()):  
         print(cle, value, sep="--=> ")
   

    def modifier(self,nom):
        pass      