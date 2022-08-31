import functions as fct

# == functions
from Stations.Stations import StationClass
from Stations.menu_station import ask_which_capacity, askstationname
from Ventes.Ventes import VentesClass

v_vente = VentesClass()
v_station = StationClass()


# functon to ask capacity
def ask_quantity_of_gallon(type_galon) -> float:
    usertype = ""

    while True:
        usertype = input(f"Veuillez entrer le nombre de gallon {type_galon} a acheter: \nR- ")
        if usertype.isdigit():
            usertype = float(usertype)
            if 1 <= usertype <= 1000000000000:
                break
            else:
                print("Entrer une acceptable(minimum 1) ")
        else:
            print("Incorrect! Veuillez un nombre")
    return usertype


def ask_enter_price(stationname: str, qte_gaz: float, qte_dies: float) -> bool | float:
    usertype = ""
    somme_due: float()

    # qte essence dispo pour la station -> (dict)
    qte_essence: dict = v_station.qteEssenceStats(stationname)
    # verifier si qte entrer est supperieur a qte disponible
    if qte_gaz > qte_essence[fct.QTE_GAL_GAZOLINE_DISPO] or qte_dies > qte_essence[fct.QTE_GAL_DIESEL_DISPO]:
        print("Vous n'avez pas suffisamment d'essence pour cette vente")
        return False
        # end if

    # somme a payer
    somme_due = qte_gaz * fct.PRICE_GAZOLINE + qte_dies * fct.PRICE_DIESEL
    print(f"\nLe montant a payer est {somme_due} HTG\n")

    while True:
        usertype = input(f"Combien voulez-vous donner:\nR- ")
        if usertype.isdecimal():
            usertype = float(usertype)
            # valeur saisie est entre montant a payer et somme_due + 1000
            if somme_due <= usertype <= (somme_due + 1000):
                break
            else:
                print(f"Le montant a payer doit etre entre {somme_due} HTG et {somme_due + 1000} HTG")
        else:
            print("Incorrect! Veuillez un nombre")
    return usertype


def saveVente(stationname: str, v_qte_gallon_gazoline: float, v_qte_gallon_diesel: float, montant_versement: float):
    qte_essence: dict = v_station.qteEssenceStats(stationname)
    somme_due: float()

    if v_qte_gallon_gazoline > qte_essence[fct.QTE_GAL_GAZOLINE_DISPO]:
        print("La quantite gazoline est trop elevee")
        return False
    if v_qte_gallon_diesel > qte_essence[fct.QTE_GAL_DIESEL_DISPO]:
        print("La quantite diesel est trop elevee")
        return False

    resultat_enregistrement = v_vente.enregistrerVente(station_name=stationname, total_qte_gaz=v_qte_gallon_gazoline,
                                                       total_qte_dies=v_qte_gallon_diesel,
                                                       versement_client=montant_versement)

    if resultat_enregistrement == fct.AMOUNT_IS_UNDER_MISC:
        print("le montant donne est inferieur au montant a payer")
    elif resultat_enregistrement > 0:
        print(f"Remise {resultat_enregistrement} HTG")
    else:
        print("Quelque chose s'est mal passe")


def addVente():
    usertype = 0.0
    gallon_type = 0
    somme_donnee = float
    stationname = ""
    reponse_in_function = None
    v_qte_gallon_gazoline = 0.0
    v_qte_gallon_diesel = 0.0

    # demander le nom de la station qui doit vendre
    while True:
        reponse_in_function = askstationname()
        # stop if user want to return
        if reponse_in_function == fct.ANNULER_OPTION:
            return
        elif fct.findIfStationExist(reponse_in_function):
            stationname = reponse_in_function
            break
        else:
            print("Cette station n'existe pas encore! Faites un autre choix")
            input("\nPress Enter to continue")
    # end while

    # demander type de gallon a vendre
    gallon_type = ask_which_capacity()
    # stop if user want to return
    if gallon_type == 0:
        return

    if gallon_type == fct.GAZOLINE_CHOICE:

        v_qte_gallon_gazoline = ask_quantity_of_gallon(type_galon=fct.GAZOLINE_CONST)
        # demander le prix a payer
        somme_donne = ask_enter_price(stationname=stationname, qte_gaz=v_qte_gallon_gazoline, qte_dies=0.0)

        if type(somme_donne) == bool:
            return

        saveVente(stationname=stationname, v_qte_gallon_gazoline=v_qte_gallon_gazoline, v_qte_gallon_diesel=0.0,
                  montant_versement=somme_donne)
        return

    elif gallon_type == fct.DIESEL_CHOICE:

        v_qte_gallon_diesel = ask_quantity_of_gallon(type_galon=fct.DIESEL_CONST)
        # demander le prix a payer
        somme_donne = ask_enter_price(stationname=stationname, qte_gaz=0.0, qte_dies=v_qte_gallon_diesel)
        if type(somme_donne) == bool:
            return
        # ----
        saveVente(stationname=stationname, v_qte_gallon_gazoline=0.0, v_qte_gallon_diesel=v_qte_gallon_diesel,
                  montant_versement=somme_donne)
        return

    elif gallon_type == fct.BOTH_GAZ_CHOICE:

        v_qte_gallon_gazoline = ask_quantity_of_gallon(type_galon=fct.GAZOLINE_CONST)
        v_qte_gallon_diesel = ask_quantity_of_gallon(type_galon=fct.DIESEL_CONST)

        # demander le prix a payer
        somme_donne = ask_enter_price(stationname=stationname, qte_gaz=v_qte_gallon_gazoline,
                                      qte_dies=v_qte_gallon_diesel)

        if type(somme_donne) == bool:
            return
        # ----

        saveVente(stationname=stationname, v_qte_gallon_gazoline=v_qte_gallon_gazoline,
                  v_qte_gallon_diesel=v_qte_gallon_diesel, montant_versement=somme_donne)

        return

    # ================================== AFFICHER TOUTES COMMANDE ===============================


def show_all_ventes():
    print("\n\n============| AFFICHER TOUTES LES COMMANDES |============")
    v_vente.afficherVentes()
