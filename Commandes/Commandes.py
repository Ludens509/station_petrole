import secrets

import functions
from functions import COMMAND_QTE_GAZOLINE, all_stations, LALUE_CONST, TABARRE_CONST, CLERCINE_CONST, PETION_VILLE_CONST, \
    QTE_GAL_DIESEL_DISPO, QTE_GAL_GAZOLINE_DISPO, all_commandes, CAPACITE_GAZOLINE, CAPACITE_DIESEL, generer_date, \
    generer_etat


class Commande:

    def __init__(self, ):
        self.etat = str()
        self.id = int()
        self.date_commande = str()
        self.qte_gallon_gazoline = float()
        self.qte_gallon_diesel = float()

    def getEtat(self):
        return self.etat

    def setEtat(self, etat):
        self.etat = etat

    def getQte_gazoline_commander(self):
        self.qte_gallon_gazoline = functions.all_commandes[COMMAND_QTE_GAZOLINE][self.qte_gallon_gazoline]
        return self.qte_gallon_gazoline

    def getQte_diesel_commander(self):
        return self.qte_gallon_diesel    

    def generer_id(self, ) -> int:
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
            functions.COMMAND_QTE_GAZOLINE: self.qte_gallon_diesel,
            functions.COMMAND_QTE_DIESEL: self.qte_gallon_gazoline,
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

    def changeStateAllCommands(self,):
        for i in enumerate(functions.all_commandes):
            for key, values in i.items():
                if key == functions.COMMAND_STATE:
                    print(f"In verification: {functions.all_commandes}\n I={i}\n Val:{values}")
                    # i[functions.COMMAND_STATE] = functions.P_STATE_COMMAND
                    # remove last
                    # functions.all_commandes.pop()
                    # add in a list
                    # functions.all_commandes.append(i)

