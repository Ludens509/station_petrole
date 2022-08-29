from Approvisionnements.Approvisionnements import Approvisionnement
from functions import findCommandeById, confirm_identity

v_approvisionnement = Approvisionnement()


# ================================== AJOUTER UN APPROVISIONNEMENT ===============================

def addApprovisionnement():
    usertype = ""

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
                #v_approvisionnement.enregistrer()

                # important to close the function
                return

            else:
                print("Veuillez choisir une valeur entre 0 et 1")
        else:
            print("Entrer une valeur correcte, entre 0 et 1")


# ================================== AFFICHER APPROVISIONNEMENT ===============================

def show_all_approvisionnement():
    print("\n\n============| AFFICHER TOUTES LES APPROVISIONNEMENTS |============")
    # v_approvisionnement.afficher()