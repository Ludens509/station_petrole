import functions as fct

# == functions
from Stations.menu_station import ask_which_capacity, askstationname


# functon to ask capacity
def ask_quantity_of_gallon(type_galon) -> float:
    usertype = ""
    while True:
        usertype = input(f"Veuillez entrer le nombre de gallon {type_galon}: a acheter\R- ")
        if usertype.isdigit():
            usertype = float(usertype)
            if 100 <= usertype <= 1000000000000:
                break
            else:
                print("Entrer une acceptable entre (100 entre 1 000 000 000 000")
        else:
            print("Incorrect! Veuillez un nombre")
    return usertype


def saveVente(stationname: str, v_qte_gallon_gazoline: float, v_qte_gallon_diesel: float):
    n = stationname
    g = v_qte_gallon_gazoline
    d = v_qte_gallon_diesel


def addVente():
    usertype = 0.0
    gallon_type = 0
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

    # demander qte gallon a vendre
    gallon_type = ask_which_capacity()
    # stop if user want to return
    if gallon_type == 0:
        return

    if gallon_type == fct.GAZOLINE_CHOICE:
        v_qte_gallon_gazoline = ask_quantity_of_gallon(type_galon=fct.GAZOLINE_CONST)
        saveVente(stationname=stationname, v_qte_gallon_gazoline=v_qte_gallon_gazoline, v_qte_gallon_diesel=0.0)
        return

    elif gallon_type == fct.DIESEL_CHOICE:
        v_qte_gallon_diesel = ask_quantity_of_gallon(type_galon=fct.DIESEL_CONST)
        saveVente(stationname=stationname, v_qte_gallon_gazoline=0.0, v_qte_gallon_diesel=v_qte_gallon_diesel)
        return

    elif gallon_type == fct.BOTH_GAZ_CHOICE:
        v_qte_gallon_gazoline = ask_quantity_of_gallon(type_galon=fct.GAZOLINE_CONST)
        saveVente(stationname=stationname, v_qte_gallon_gazoline=v_qte_gallon_gazoline, v_qte_gallon_diesel=0.0)
        v_qte_gallon_diesel = ask_quantity_of_gallon(type_galon=fct.DIESEL_CONST)
        saveVente(stationname=stationname, v_qte_gallon_gazoline=0.0, v_qte_gallon_diesel=v_qte_gallon_diesel)
        return


# ================================== AFFICHER TOUTES COMMANDE ===============================

def show_all_ventes():
    print("\n\n============| AFFICHER TOUTES LES COMMANDES |============")
    # v_commande.afficher()
