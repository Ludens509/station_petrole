

class Station():

  lalue,tabarre,clercine,petion_ville = dict(), dict(), dict(), dict()

  def __init__(self,nom,capacite_gazoline,pourcentage_gazoline,pourcentage_diesel,capacite_diesel):
    self.nom = nom
    self.capacite_gazoline = capacite_gazoline
    self.capacite_diesel = capacite_diesel
    self.pourcentage_diesel = pourcentage_diesel
    self.pourcentage_gazoline = pourcentage_gazoline

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
      Station.lalue.update({"nom":self.nom, "capacite Gazoline":self.capacite_gazoline,"capacite Diesel":self.capacite_diesel,"% Diesel":self.pourcentage_diesel,"%tage Gazoline":self.pourcentage_gazoline})
      
    