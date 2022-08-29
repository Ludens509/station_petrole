import functions


class Ventes:

    def __init__(self):
        self.qte_diesel = float()
        self.qte_gazoline = float()
        self.prix_gazoline = functions.PRICE_GAZOLINE
        self.prix_diesel = functions.PRICE_DIESEL

    def enregistrer(self, qte_gaz, qte_dies):
        self.qte_gazoline = qte_gaz
        self.qte_diesel = qte_dies
