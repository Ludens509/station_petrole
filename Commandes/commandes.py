from stations import Station
class Commande(Station):

  def __init__(self,id):
   Station.__int__(self)
      

  def enregistrer(self,id, qte_gallon_diesel ,qte_gallon_gazoline, date_commande,etat):
    self.id = id
    self.qte_gallon_diesel = qte_gallon_diesel
    self.qte_gallon_gazoline = qte_gallon_gazoline
    self.date_commande = date_commande
    self.etat = etat

  def afficher(self,):
    pass
    