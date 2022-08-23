from stations import Station
from functions import LALUE_CONST,TABARRE_CONST,CLERCINE_CONST,PETION_VILLE_CONST,QTE_GAL_DIESEL,QTE_GAL_GAZOLINE
import functions
class Commande(Station):

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

  def afficher(self,):
        for k, val in functions.all_commande.items():
            if val.items():
                print(f"\n{k.upper()}\n")
                for cle, value in val.items():
                    print(f"{cle}       --> {value}")

    #those function   return the total gallon diesel and gazoline of all the station 
  def  total_gallon_diesel(self):
     qte_gallon_dsel_Lalue = functions.all_station[LALUE_CONST][QTE_GAL_DIESEL]
     qte_gallon_dsel_Tabarre = functions.all_station[TABARRE_CONST][QTE_GAL_DIESEL] 
     qte_gallon_dsel_Clercine = functions.all_station[CLERCINE_CONST][QTE_GAL_DIESEL]
     qte_gallon_dsel_pv = functions.all_station[PETION_VILLE_CONST][QTE_GAL_DIESEL]
     total_sation_gallon_diesel = qte_gallon_dsel_Lalue+qte_gallon_dsel_Tabarre+qte_gallon_dsel_Clercine+qte_gallon_dsel_pv
     return total_sation_gallon_diesel 

  def total_gallon_gazoline():

     qte_gallon_gaz_Lalue = functions.all_station[LALUE_CONST][QTE_GAL_GAZOLINE]
     qte_gallon_gaz_Tabarre = functions.all_station[TABARRE_CONST][QTE_GAL_GAZOLINE] 
     qte_gallon_gaz_Clercine = functions.all_station[CLERCINE_CONST][QTE_GAL_GAZOLINE]
     qte_gallon_gaz_pv = functions.all_station[PETION_VILLE_CONST][QTE_GAL_GAZOLINE]
     total_station_gallon_gazoline = qte_gallon_gaz_Lalue+qte_gallon_gaz_Tabarre+qte_gallon_gaz_Clercine+qte_gallon_gaz_pv
     return total_station_gallon_gazoline