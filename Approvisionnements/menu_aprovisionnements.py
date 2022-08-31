from distutils.cmd import Command
import secrets
from Approvisionnements.Approvisionnements import Approvisionnement
from Commandes.Commandes import Commande
from Stations.Stations import StationClass
from functions import findCommandeById, confirm_identity
import functions

v_approvisionnement = Approvisionnement()


def generer_id() -> int:
    # generate 1 secure random numbers between 10 and 500
    for x in range(0, 1):
        secret_id = (10 + secrets.randbelow(500)).__str__()

    # recursive function : get unique ID in all_commandes
    if functions.findCommandeById(secret_id):
        self.generer_id()

    return secret_id


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
                # for i in functions.all_commandes:
                #     for key, val in i.items():
                #         if key == functions.COMMAND_STATE and val == "N":
                #             v_qte_diesel_command = Commande.getQte_diesel_commander
                #             v_qte_gazoline_command = Commande.getQte_gazoline_commander
                #             Commande.setEtat("P")
                #         else:
                #             print("Pas de nouvelle commande")
                gallon_diesel_manquant = 0.0
                gallon_gazoline_manquant = 0.0
                # LALUE
                for cle, valeur in functions.all_stations.items():
                    if cle == functions.LALUE_CONST:
                        id = generer_id()
                        station = functions.LALUE_CONST
                        date = functions.generer_date()

                        gallon_diesel_manquant = StationClass.getCapaciteDiesel(station) - StationClass.getQte_diesel(station)
                        gallon_gazoline_manquant = StationClass.getCapaciteGazoline(station) - StationClass.getQte_gazoline(station)

                        if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                            StationClass.setQte_diesel(station,gallon_diesel_manquant)
                            v_approvisionnement.enregistrer(id=id,station=station,qte_gallon_diesel=gallon_diesel_manquant,qte_gallon_gazoline=0,date_app=date)
                        elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                            StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                            v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel= 0,qte_gallon_gazoline=gallon_gazoline_manquant, date_app=date)
                        else:
                            StationClass.setQte_diesel(station, gallon_diesel_manquant)
                            StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                            v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel= gallon_diesel_manquant,qte_gallon_gazoline=gallon_gazoline_manquant, date_app=date)

                # TABARRE
                for cle, valeur in functions.all_stations.items():
                    if cle == functions.TABARRE_CONST:
                        id = generer_id()
                        station = functions.TABARRE_CONST
                        date = functions.generer_date()

                        gallon_diesel_manquant = StationClass.getCapaciteDiesel(station) - StationClass.getQte_diesel(station)
                        gallon_gazoline_manquant = StationClass.getCapaciteGazoline(station) - StationClass.getQte_gazoline(station)

                        if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                            StationClass.setQte_diesel(station,gallon_diesel_manquant)
                            v_approvisionnement.enregistrer(id=id,station=station,qte_gallon_diesel=gallon_diesel_manquant,qte_gallon_gazoline=0,date_app=date)
                        elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                            StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                            v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel= 0,qte_gallon_gazoline=gallon_gazoline_manquant, date_app=date)
                        else:
                            StationClass.setQte_diesel(station, gallon_diesel_manquant)
                            StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                            v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel= gallon_diesel_manquant,qte_gallon_gazoline=gallon_gazoline_manquant, date_app=date)

                            # CLERCINE
                            for cle, valeur in functions.all_stations.items():
                                if cle == functions.CLERCINE_CONSTT:
                                    id = generer_id()
                                    station = functions.CLERCINE_CONST
                                    date = functions.generer_date()

                                    gallon_diesel_manquant = StationClass.getCapaciteDiesel(station) - StationClass.getQte_diesel(station)
                                    gallon_gazoline_manquant = StationClass.getCapaciteGazoline(station) - StationClass.getQte_gazoline(station)

                                    if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                                        StationClass.setQte_diesel(station, gallon_diesel_manquant)
                                        v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel=gallon_diesel_manquant,qte_gallon_gazoline=0, date_app=date)
                                    elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                                        StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                                        v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel=0,qte_gallon_gazoline=gallon_gazoline_manquant,date_app=date)
                                    else:
                                        StationClass.setQte_diesel(station, gallon_diesel_manquant)
                                        StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                                        v_approvisionnement.enregistrer(id=id, station=station,qte_gallon_diesel=gallon_diesel_manquant,qte_gallon_gazoline=gallon_gazoline_manquant, date_app=date)

                                        # PETION-VILLE
                                        for cle, valeur in functions.all_stations.items():
                                            if cle == functions.PETION_VILLE_CONST:
                                                id = generer_id()
                                                station = functions.PETION_VILLE_CONST
                                                date = functions.generer_date()

                                                gallon_diesel_manquant = StationClass.getCapaciteDiesel(station) - StationClass.getQte_diesel(station)
                                                gallon_gazoline_manquant = StationClass.getCapaciteGazoline(station) - StationClass.getQte_gazoline(station)

                                                if v_qte_diesel_command > 0 and v_qte_gazoline_command == 0:
                                                    StationClass.setQte_diesel(station, gallon_diesel_manquant)
                                                    v_approvisionnement.enregistrer(id=id, station=station, qte_gallon_diesel=gallon_diesel_manquant,qte_gallon_gazoline=0,date_app=date)
                                                elif v_qte_diesel_command == 0 and v_qte_gazoline_command > 0:
                                                    StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                                                    v_approvisionnement.enregistrer(id=id, station=station,qte_gallon_diesel=0,qte_gallon_gazoline=gallon_gazoline_manquant, date_app=date)
                                                else:
                                                    StationClass.setQte_diesel(station, gallon_diesel_manquant)
                                                    StationClass.setQte_gazoline(station, gallon_gazoline_manquant)
                                                    v_approvisionnement.enregistrer(id=id, station=station,qte_gallon_diesel=gallon_diesel_manquant,qte_gallon_gazoline=gallon_gazoline_manquant,date_app=date)

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


