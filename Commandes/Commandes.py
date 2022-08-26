import functions
from Stations.Stations import StationClass
from functions import all_stations, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, PETION_VILLE_CONST, \
    QTE_GAL_DIESEL_DISPO, QTE_GAL_GAZOLINE_DISPO, all_commandes, CAPACITE_GAZOLINE, CAPACITE_DIESEL


class Commande(StationClass):
    # capacite variables
    capacite_diesel_lalue, capacite_gazoline_lalue = 0, 0
    capacite_diesel_tabarre, capacite_gazoline_tabarre = 0, 0
    capacite_diesel_clercine, capacite_gazoline_clercine = 0, 0
    capacite_diesel_pv, capacite_gazoline_pv = 0, 0
    capacite_total_diesel = 0.0
    capacite_total_gazoline = 0.0
    #  quantite variables
    qte_gallon_gaz_Lalue, qte_gallon_dsel_Lalue = 0, 0
    qte_gallon_gaz_Tabarre, qte_gallon_dsel_Tabbare = 0, 0
    qte_gallon_gaz_Clercine, qte_gallon_dsel_Clercine = 0, 0
    qte_gallon_gaz_pv, qte_gallon_dsel_pv = 0, 0
    total_sation_gallon_diesel = 0.0
    total_sation_gallon_gazoline = 0.0

    def __init__(self, ):
        StationClass.__init__(self, )

    def enregistrer(self, id, qte_gallon_diesel, qte_gallon_gazoline, date_commande, etat):
        self.id = id
        self.qte_gallon_diesel = qte_gallon_diesel
        self.qte_gallon_gazoline = qte_gallon_gazoline
        self.date_commande = date_commande
        self.etat = etat

        functions.all_commandes.extend([id, qte_gallon_diesel, qte_gallon_gazoline, date_commande, etat])
        print('\nSuccessfully saved!')

    def afficher(self, ):
        for i in range(len(functions.all_commandes)):
            print("====LISTE DES COMMANDE====")
            print(all_commandes[i],)


    # these function   return the total gallon diesel  of all the station
    def total_gallon_diesel_maquant(self):
        total_gallon_diesel_manquant = 0.0
        capacite_diesel_lalue = all_stations[LALUE_CONST][CAPACITE_DIESEL]
        capacite_diesel_tabarre = all_stations[TABARRE_CONST][CAPACITE_DIESEL]
        capacite_diesel_clercine = all_stations[CLERCINE_CONST][CAPACITE_DIESEL]
        capacite_diesel_pv = all_stations[PETION_VILLE_CONST][CAPACITE_DIESEL]
        capacite_total_diesel = capacite_diesel_lalue + capacite_diesel_tabarre + capacite_diesel_clercine + capacite_diesel_pv
        # Quantite total gallon diesel disponible
        qte_gallon_dsel_Lalue = all_stations[LALUE_CONST][QTE_GAL_DIESEL_DISPO]
        qte_gallon_dsel_Tabarre = all_stations[TABARRE_CONST][QTE_GAL_DIESEL_DISPO]
        qte_gallon_dsel_Clercine = all_stations[CLERCINE_CONST][QTE_GAL_DIESEL_DISPO]
        qte_gallon_dsel_pv = all_stations[PETION_VILLE_CONST][QTE_GAL_DIESEL_DISPO]
        total_sation_gallon_diesel = qte_gallon_dsel_Lalue + qte_gallon_dsel_Tabarre + qte_gallon_dsel_Clercine + qte_gallon_dsel_pv

        total_gallon_diesel_manquant = capacite_total_diesel + total_sation_gallon_diesel
        return total_gallon_diesel_manquant

    def total_gallon_gazoline_maquant(self):
        # these function   return the total gallon  gazoline of all the station

        total_gallon_gazoline_manquant = 0.0
        capacite_gazoline_lalue = all_stations[LALUE_CONST][CAPACITE_GAZOLINE]
        capacite_gazoline_tabarre = all_stations[TABARRE_CONST][CAPACITE_GAZOLINE]
        capacite_gazoline_clercine = all_stations[CLERCINE_CONST][CAPACITE_GAZOLINE]
        capacite_gazoline_pv = all_stations[PETION_VILLE_CONST][CAPACITE_GAZOLINE]
        capacite_total_gazoline = capacite_gazoline_lalue + capacite_gazoline_tabarre + capacite_gazoline_clercine + capacite_gazoline_pv
        # Quantite total gallon gazoline disponible
        qte_gallon_gaz_Lalue = all_stations[LALUE_CONST][QTE_GAL_GAZOLINE_DISPO]
        qte_gallon_gaz_Tabarre = all_stations[TABARRE_CONST][QTE_GAL_GAZOLINE_DISPO]
        qte_gallon_gaz_Clercine = all_stations[CLERCINE_CONST][QTE_GAL_GAZOLINE_DISPO]
        qte_gallon_gaz_pv = all_stations[PETION_VILLE_CONST][QTE_GAL_GAZOLINE_DISPO]
        total_station_gallon_gazoline = qte_gallon_gaz_Lalue + qte_gallon_gaz_Tabarre + qte_gallon_gaz_Clercine + qte_gallon_gaz_pv

        total_gallon_gazoline_manquant = capacite_total_gazoline - total_station_gallon_gazoline
        return total_gallon_gazoline_manquant
