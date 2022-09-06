import secrets

import functions
from functions import COMMAND_QTE_GAZOLINE, COMMAND_QTE_DIESEL, all_stations, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, \
    PETION_VILLE_CONST, \
    QTE_GAL_DIESEL_DISPO, QTE_GAL_GAZOLINE_DISPO, all_commandes, CAPACITE_GAZOLINE, CAPACITE_DIESEL, generer_date, \
    generer_etat


class Commande:

    def __init__(self, ):
        self.etat = str()
        self.id = str()
        self.date_commande = str()
        self.qte_gallon_gazoline = float()
        self.qte_gallon_diesel = float()

    def getEtat(self):
        return self.etat

    def setEtat(self, etat):
        self.etat = etat


    def getQte_gazoline_commander(self,) -> float:
        for i in functions.all_commandes:
            for key, values in i.items():
                if key == functions.COMMAND_QTE_GAZOLINE:
                    self.qte_gallon_gazoline =  values
        return self.qte_gallon_gazoline

    def getQte_diesel_commander(self,) -> float:
        for i in functions.all_commandes:
            for key, values in i.items():
                if key == functions.COMMAND_QTE_DIESEL:
                    self.qte_gallon_diesel =  values
        return self.qte_gallon_diesel

    def generer_id(self, ) -> str:
        # generate 1 secure random numbers between 10 and 500
        for x in range(0, 1):
            secret_id = (10 + secrets.randbelow(500)).__str__()
        # recursive function : get unique ID in all_commandes
        if functions.findCommandeById(secret_id):
            self.generer_id()
        return secret_id

    def enregistrer(self, qte_gallon_diesel: float, qte_gallon_gazoline: float):
        self.qte_gallon_diesel = qte_gallon_diesel
        self.qte_gallon_gazoline = qte_gallon_gazoline

        self.id = self.generer_id()
        self.date_commande = functions.generer_date()
        self.etat = functions.N_STATE_COMMAND

        # to change old commands' state on 'P'
        self.changeStateAllCommands()
        # command_dict =
        functions.all_commandes.append({
            functions.COMMAND_ID: self.id,
            functions.COMMAND_QTE_DIESEL: self.qte_gallon_diesel,
            functions.COMMAND_QTE_GAZOLINE: self.qte_gallon_gazoline,
            functions.COMMAND_DATE: self.date_commande,
            functions.COMMAND_STATE: self.etat
        })

        print('\nSuccessfully saved!')

    def afficher(self, ):

        if len(functions.all_commandes) > 0:
            for i in functions.all_commandes:
                for key, values in i.items():
                    print(f"{key} : {values} ")
                # end for
                print("\n")
            # end for
        else:
            print("\nNo command found\n")

        # end if

    @staticmethod
    def changeStateAllCommands():
        for i, valeur in enumerate(functions.all_commandes):
            for key, val in valeur.items():
                if valeur[key] == functions.N_STATE_COMMAND:
                    functions.all_commandes[i][key] = functions.P_STATE_COMMAND

    @staticmethod
    def findNewCommand() -> bool:
        for i, valeur in enumerate(functions.all_commandes):
            for key, val in valeur.items():
                if valeur[key] == functions.N_STATE_COMMAND:
                    return True
        
        return False