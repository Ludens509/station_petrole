from Stations.stations import Station
from functions import LALUE_CONST,TABARRE_CONST,CLERCINE_CONST,PETION_VILLE_CONST,QTE_GAL_DIESEL,QTE_GAL_GAZOLINE
import functions
class Commande(Station):
  # capacite variables
  capacite_diesel_lalue,capacite_gazoline_lalue = 0,0
  capacite_diesel_tabarre, capacite_gazoline_tabarre =0,0
  capacite_diesel_clercine, capacite_gazoline_clercine =0,0
  capacite_diesel_pv, capacite_gazoline_pv =0,0
  capacite_total_diesel =0.0
  capacite_total_gazoline =0.0
#  quantite variables
  qte_gallon_gaz_Lalue ,qte_gallon_dsel_Lalue = 0,0
  qte_gallon_gaz_Tabarre ,qte_gallon_dsel_Tabbare = 0,0
  qte_gallon_gaz_Clercine ,qte_gallon_dsel_Clercine = 0,0
  qte_gallon_gaz_pv ,qte_gallon_dsel_pv = 0,0
  total_sation_gallon_diesel =0.0
  total_sation_gallon_gazoline =0.0
  def __init__(self,):
   Station.__int__(self,)
      

  def enregistrer(self,id, qte_gallon_diesel ,qte_gallon_gazoline, date_commande,etat):
    self.id = id
    self.qte_gallon_diesel = qte_gallon_diesel
    self.qte_gallon_gazoline = qte_gallon_gazoline
    self.date_commande = date_commande
    self.etat = etat


    print('\nSuccessfully saved!')

  def afficher(self,):
        pass

    #these function   return the total gallon diesel  of all the station
  def  total_gallon_diesel_maquant(self):
     total_gallon_diesel_manquant = 0.0
     capacite_diesel_lalue = functions.all_station[LALUE_CONST]["capacite_diesel"] 
     capacite_diesel_tabarre = functions.all_station[TABARRE_CONST]["capacite_diesel"] 
     capacite_diesel_clercine = functions.all_station[CLERCINE_CONST]["capacite_diesel"] 
     capacite_diesel_pv = functions.all_station[PETION_VILLE_CONST]["capacite_diesel"] 
     capacite_total_diesel = capacite_diesel_lalue+capacite_diesel_tabarre+capacite_diesel_clercine+capacite_diesel_pv
       # Quantite total gallon diesel disponible
     qte_gallon_dsel_Lalue = functions.all_station[LALUE_CONST][QTE_GAL_DIESEL] 
     qte_gallon_dsel_Tabarre = functions.all_station[TABARRE_CONST][QTE_GAL_DIESEL] 
     qte_gallon_dsel_Clercine = functions.all_station[CLERCINE_CONST][QTE_GAL_DIESEL]
     qte_gallon_dsel_pv = functions.all_station[PETION_VILLE_CONST][QTE_GAL_DIESEL]
     total_sation_gallon_diesel = qte_gallon_dsel_Lalue+qte_gallon_dsel_Tabarre+qte_gallon_dsel_Clercine+qte_gallon_dsel_pv

     total_gallon_diesel_manquant = capacite_total_diesel+total_sation_gallon_diesel
     return total_gallon_diesel_manquant 

  def total_gallon_gazoline_maquant(self):
     #these function   return the total gallon  gazoline of all the station
  
     total_gallon_gazoline_manquant = 0.0
     capacite_gazoline_lalue = functions.all_station[LALUE_CONST]["capacite_diesel"] 
     capacite_gazoline_tabarre = functions.all_station[TABARRE_CONST]["capacite_diesel"] 
     capacite_gazoline_clercine = functions.all_station[CLERCINE_CONST]["capacite_diesel"] 
     capacite_gazoline_pv = functions.all_station[PETION_VILLE_CONST]["capacite_diesel"] 
     capacite_total_gazoline = capacite_gazoline_lalue+capacite_gazoline_tabarre+capacite_gazoline_clercine+capacite_gazoline_pv
       # Quantite total gallon gazoline disponible
     qte_gallon_gaz_Lalue = functions.all_station[LALUE_CONST][QTE_GAL_GAZOLINE]
     qte_gallon_gaz_Tabarre = functions.all_station[TABARRE_CONST][QTE_GAL_GAZOLINE] 
     qte_gallon_gaz_Clercine = functions.all_station[CLERCINE_CONST][QTE_GAL_GAZOLINE]
     qte_gallon_gaz_pv = functions.all_station[PETION_VILLE_CONST][QTE_GAL_GAZOLINE]
     total_station_gallon_gazoline = qte_gallon_gaz_Lalue+qte_gallon_gaz_Tabarre+qte_gallon_gaz_Clercine+qte_gallon_gaz_pv

     total_gallon_gazoline_manquant = capacite_total_gazoline - total_station_gallon_gazoline
     return total_gallon_gazoline_manquant