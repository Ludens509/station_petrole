from Approvisionnements.Approvisionnements import Approvisionnement
from Commandes.Commandes import Commande
from Stations.Stations import StationClass
from functions import confirm_identity
import functions

v_approvisionnement = Approvisionnement()
v_commande = Commande()


#     # Get the amount of gazoline and diesel odered
# def getQte_commander(self,):

#     etat = "N"
#     if etat in functions.all_commandes:
#         qte_diesel_commander = Commande.getQte_diesel_commander()
#         qte_gazoline_commander = Commande.getQte_gazoline_commander
#         Commande.setEtat("P")
#     else:
#         print("Pas de nouvelle commande")    


# ================================== AJOUTER UN APPROVISIONNEMENT ===============================

def addApprovisionnement():
    usertype = ""
    v_qte_diesel_command = 0.0
    v_qte_gazoline_command = 0.0

    print("Pour lancer un approvisionnement,")
    print(f"Veuillez d'abord confirmer votre identite. Etes-vous un admin ?")
    print(f"1- Oui")
    print("0- Non")

    while True:
        usertype = input("R- ")
        if usertype.isdigit():
            usertype = int(usertype)

            # stop if user want to return
            if usertype == 0:
                return

            # if user want to confirm
            elif usertype == 1:
                confirm_id = False
                confirm_id = confirm_identity()

                # stop if user not confirm the command
                if not confirm_id:
                    print("\nWe can't confirm your identity\n")
                    input("Press any key to continue\n")
                    return

                # l'approvisionnement peut etre lancee
                if len(functions.all_commandes) > 0:
                    for i in functions.all_commandes:
                        for key, val in i.items():
                            if key == functions.COMMAND_STATE and val == "N":
                                qte_diesel_command = v_commande.getQte_diesel_commander()
                                qte_gazoline_command = v_commande.getQte_gazoline_commander()
                                Commande.changeStateAllCommands
                else:
                    print("\nNo command found\n")

                qte_dies_manquante = 0.0
                qte_gaz_manquante = 0.0
                v_qte_diesel_command = qte_diesel_command
                v_qte_gazoline_command = qte_gazoline_command
                # LALUE
                for cle, valeur in functions.all_stations.items():
                    if cle == functions.LALUE_CONST:
                        # id = generer_id()
                        station = functions.LALUE_CONST
                        date = functions.generer_date()

                        qte_essence = StationClass.qteEssenceStats(station)
                        if len(qte_essence) == 0:
                            # vide
                            return
                        qte_gaz_manquante = qte_essence[functions.QTE_GAL_GAZOLINE_CONSOMMEE]
                        qte_dies_manquante = qte_essence[functions.QTE_GAL_DIESEL_CONSOMMEE]

                        if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                            StationClass().setQte_diesel(station,qte_dies_manquante)
                            v_approvisionnement.enregistrer(station=station,qte_gallon_diesel=qte_dies_manquante,qte_gallon_gazoline=0)
                        elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer( station=station, qte_gallon_diesel= 0,qte_gallon_gazoline=qte_gaz_manquante)
                        else:
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            StationClass().setQte_diesel(station, qte_dies_manquante)
                            v_approvisionnement.enregistrer( station=station, qte_gallon_diesel= qte_dies_manquante,qte_gallon_gazoline=qte_gaz_manquante)
                # TABARRE
                    elif cle == functions.TABARRE_CONST:
                        # id = generer_id()
                        station = functions.TABARRE_CONST
                        date = functions.generer_date()

                        qte_essence = StationClass.qteEssenceStats(station)
                        if len(qte_essence) == 0:
                            # vide
                            return
                        qte_gaz_manquante = qte_essence[functions.QTE_GAL_GAZOLINE_CONSOMMEE]
                        qte_dies_manquante = qte_essence[functions.QTE_GAL_DIESEL_CONSOMMEE]

                        if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                            StationClass().setQte_diesel(station,qte_dies_manquante)
                            v_approvisionnement.enregistrer(station=station,qte_gallon_diesel=qte_dies_manquante,qte_gallon_gazoline=0)
                        elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer(station=station, qte_gallon_diesel= 0,qte_gallon_gazoline=qte_gaz_manquante)
                        else:
                            StationClass().setQte_diesel(station, qte_dies_manquante)
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer(station=station, qte_gallon_diesel= qte_dies_manquante,qte_gallon_gazoline=qte_gaz_manquante)
                # CLERCINE
                    elif cle == functions.CLERCINE_CONST:
                        # id = generer_id()
                        station = functions.CLERCINE_CONST
                        date = functions.generer_date

                        qte_essence = StationClass.qteEssenceStats(station)
                        if len(qte_essence) == 0:
                            # vide
                            return
                        qte_gaz_manquante = qte_essence[functions.QTE_GAL_GAZOLINE_CONSOMMEE]
                        qte_dies_manquante = qte_essence[functions.QTE_GAL_DIESEL_CONSOMMEE]

                        if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                            StationClass().setQte_diesel(station,qte_dies_manquante)
                            v_approvisionnement.enregistrer(station=station,qte_gallon_diesel=qte_dies_manquante,qte_gallon_gazoline=0)
                        elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer( station=station, qte_gallon_diesel= 0,qte_gallon_gazoline=qte_gaz_manquante)
                        else:
                            StationClass().setQte_diesel(station, qte_dies_manquante)
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer(station=station, qte_gallon_diesel= qte_dies_manquante,qte_gallon_gazoline=qte_gaz_manquante)
                # PETION-VILLE       
                    else :
                        # id = generer_id()
                        station = functions.PETION_VILLE_CONST
                        date = functions.generer_date

                        qte_essence = StationClass.qteEssenceStats(station)
                        if len(qte_essence) == 0:
                            # vide
                            return
                        qte_gaz_manquante = qte_essence[functions.QTE_GAL_GAZOLINE_CONSOMMEE]
                        qte_dies_manquante = qte_essence[functions.QTE_GAL_DIESEL_CONSOMMEE]

                        if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                            StationClass().setQte_diesel(station,qte_dies_manquante)
                            v_approvisionnement.enregistrer(station=station,qte_gallon_diesel=qte_dies_manquante,qte_gallon_gazoline=0)
                        elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer(station=station, qte_gallon_diesel= 0,qte_gallon_gazoline=qte_gaz_manquante)
                        else:
                            StationClass().setQte_diesel(station, qte_dies_manquante)
                            StationClass().setQte_gazoline(station, qte_gaz_manquante)
                            v_approvisionnement.enregistrer(station=station, qte_gallon_diesel= qte_dies_manquante,qte_gallon_gazoline=qte_gaz_manquante)

                # important to close the function
                return

            else:
                print("Veuillez choisir une valeur entre 0 et 1")
        else:
            print("Entrer une valeur correcte, entre 0 et 1")

# ================================== AFFICHER APPROVISIONNEMENT ===============================

def show_all_approvisionnement():
    print("\n\n============| AFFICHER TOUTES LES APPROVISIONNEMENTS |============")
    v_approvisionnement.afficher()