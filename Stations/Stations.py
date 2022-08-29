from functions import GAZOLINE_CONST, DIESEL_CONST, CAPACITE_GAZOLINE, CAPACITE_DIESEL, QTE_GAL_GAZOLINE_DISPO, \
    QTE_GAL_DIESEL_DISPO, QTE_GAL_GAZOLINE_CONSOMMEE, QTE_GAL_DIESEL_CONSOMMEE, \
    PERCENT_GAL_GAZOLINE, PERCENT_GAL_DIESEL, QTE_GAL_GAZOLINE_MANQUEE, QTE_GAL_DIESEL_MANQUEE, \
    TOTAL_GAL_DIESEL_MANQUEE, TOTAL_GAL_GAZOLINE_MANQUEE

import functions


class StationClass:

    def __init__(self):
        self.nom = str
        self.capacite_gazoline = float()
        self.capacite_diesel = float()
        # dispo
        self.qte_gallon_gazoline_dispo = 0.0
        self.qte_gallon_diesel_dispo = 0.0
        # percent
        self.pourcentage_gazoline = 0.0
        self.pourcentage_diesel = 0.0

    def enregistrer(self, nom: str, capacite_gazoline: float, capacite_diesel: float):
        self.nom = nom
        self.capacite_gazoline = capacite_gazoline
        self.capacite_diesel = capacite_diesel
        # dispo
        self.qte_gallon_gazoline_dispo = self.capacite_gazoline
        self.qte_gallon_diesel_dispo = self.capacite_diesel

        # functions to change percent
        self.changePourcentageGazoline(nom=nom)
        self.changePourcentageDiesel(nom=nom)

        if self.nom == functions.LALUE_CONST or self.nom == functions.TABARRE_CONST \
                or self.nom == functions.CLERCINE_CONST \
                or self.nom == functions.PETION_VILLE_CONST:
            functions.all_stations.update({
                self.nom: {
                    CAPACITE_GAZOLINE: self.capacite_gazoline,
                    CAPACITE_DIESEL: self.capacite_diesel,
                    QTE_GAL_GAZOLINE_DISPO: self.qte_gallon_gazoline_dispo,
                    QTE_GAL_DIESEL_DISPO: self.qte_gallon_diesel_dispo,
                    PERCENT_GAL_GAZOLINE: self.pourcentage_gazoline,
                    PERCENT_GAL_DIESEL: self.pourcentage_diesel,
                }})
            print('\nSuccessfully saved!')
            input("\nPress any key to continue")
        else:
            print("\nErreur d'enregistrement")
            input("\nPress any key to continue")

    def getNom(self):
        return self.nom

    def getCapaciteGazoline(self, ):
        return self.capacite_gazoline

    def setCapaciteGazoline(self, nom: str, newCapacite_gazoline: float):
        self.capacite_gazoline = newCapacite_gazoline
        functions.all_stations[nom][CAPACITE_GAZOLINE] = newCapacite_gazoline
        # change qte dispo
        self.qte_gallon_gazoline_dispo = newCapacite_gazoline
        functions.all_stations[nom][QTE_GAL_GAZOLINE_DISPO] = self.qte_gallon_gazoline_dispo
        # functions to change percent
        self.changePourcentageGazoline(nom=nom)

    def getCapaciteDisesel(self, ):
        return self.capacite_diesel

    def setCapaciteDiesel(self, nom: str, newCapacite_diesel: float):
        self.capacite_diesel = newCapacite_diesel
        functions.all_stations[nom][CAPACITE_DIESEL] = newCapacite_diesel

        # change qte dispo
        self.qte_gallon_diesel_dispo = newCapacite_diesel
        functions.all_stations[nom][QTE_GAL_DIESEL_DISPO] = self.qte_gallon_diesel_dispo

        # functions to change percent
        self.changePourcentageDiesel(nom=nom)


    def getPourcentageGazoline(self, ) -> float:
        return self.pourcentage_gazoline

    def changePourcentageGazoline(self, nom: str):
        self.pourcentage_gazoline = self.qte_gallon_gazoline_dispo / self.capacite_gazoline * 100
        if functions.findIfStationExist(nom):
            functions.all_stations[nom][functions.PERCENT_GAL_GAZOLINE] = self.pourcentage_gazoline

    def getPourcentageDiesel(self, ):
        return self.pourcentage_diesel

    def changePourcentageDiesel(self, nom: str):
        self.pourcentage_diesel = self.qte_gallon_diesel_dispo / self.capacite_diesel * 100
        if functions.findIfStationExist(nom):
            functions.all_stations[nom][functions.PERCENT_GAL_DIESEL] = self.pourcentage_diesel

    def afficher(self, ):
        for k, val in functions.all_stations.items():
            if val.items():
                print(f"\n{k.upper()}\n")
                for cle, value in val.items():
                    if 'percent' in cle:
                        print(f"{cle.replace('_', ' ')} -> {value}%")
                    else:
                        print(f"{cle.replace('_', ' ')} -> {value}")

    def modifier(self, nom: str, typeCapacite: str, nouvellevaleur: float):
        """
        :type nom: str
        :type typeCapacite: str
        :type nouvellevaleur : float
        """
        print(f"LOG: Modifier capacite{typeCapacite}: {nouvellevaleur}")
        if typeCapacite == GAZOLINE_CONST:
            self.setCapaciteGazoline(nom, nouvellevaleur)
            self.changePourcentageGazoline(nom=nom)
            print("\nChanged gazoline successfully!")
        elif typeCapacite == DIESEL_CONST:
            self.capacite_diesel = nouvellevaleur
            self.setCapaciteDiesel(nom, nouvellevaleur)
            self.changePourcentageDiesel(nom=nom)
            print("\nChanged diesel successfully!")
        else:
            print("\nCan't change this capacity!")

    @staticmethod
    def qteEssenceStats(nomstation) -> dict[float]:

        data_essence = dict()
        qte_gaz_consomee = float()
        qte_dies_consommee = float()
        qte_gaz_dispo = float()
        qte_dies_dispo = float()
        cap_gaz = float()
        cap_dies = float()

        if nomstation in functions.all_stations:
            cap_gaz = functions.all_stations[nomstation][CAPACITE_GAZOLINE]
            qte_gaz_dispo = functions.all_stations[nomstation][QTE_GAL_GAZOLINE_DISPO]
            qte_gaz_consomee = functions.all_stations[nomstation][CAPACITE_GAZOLINE] - \
                               functions.all_stations[nomstation][QTE_GAL_GAZOLINE_DISPO]

            cap_dies = functions.all_stations[nomstation][CAPACITE_DIESEL]
            qte_dies_dispo = functions.all_stations[nomstation][QTE_GAL_DIESEL_DISPO]
            qte_dies_consommee = functions.all_stations[nomstation][QTE_GAL_DIESEL_DISPO] - \
                                 functions.all_stations[nomstation][QTE_GAL_DIESEL_DISPO]

            data_essence.update({
                CAPACITE_GAZOLINE: cap_gaz,
                QTE_GAL_GAZOLINE_DISPO: qte_gaz_dispo,
                QTE_GAL_GAZOLINE_CONSOMMEE: qte_gaz_consomee,

                CAPACITE_DIESEL: cap_dies,
                QTE_GAL_DIESEL_DISPO: qte_dies_dispo,
                QTE_GAL_DIESEL_CONSOMMEE: qte_dies_consommee
            })
        # end if

        return data_essence

    def sommeQtes(self, ) -> dict[float]:
        # capacites
        somme_cap_gaz = 0.0
        somme_cap_dies = 0.0
        # disponible
        somme_qte_gaz_dispo = 0.0
        somme_qte_dies_dispo = 0.0
        # consommee
        somme_gaz_cons = 0.0
        somme_dies_cons = 0.0
        # total qte manquantes
        total_gaz_manquantes = 0.0
        total_dies_manquantes = 0.0

        for key, val in functions.all_stations.items():
            statsessence = self.qteEssenceStats(nomstation=key)

            somme_cap_gaz = somme_cap_gaz + statsessence[CAPACITE_GAZOLINE]
            somme_cap_dies = somme_cap_dies + statsessence[CAPACITE_DIESEL]

            somme_qte_gaz_dispo = somme_qte_gaz_dispo + statsessence[QTE_GAL_GAZOLINE_DISPO]
            somme_qte_dies_dispo = somme_qte_dies_dispo + statsessence[QTE_GAL_DIESEL_DISPO]

            somme_gaz_cons = somme_gaz_cons + statsessence[QTE_GAL_GAZOLINE_CONSOMMEE]
            somme_dies_cons = somme_dies_cons + statsessence[QTE_GAL_GAZOLINE_CONSOMMEE]
        # end for

        # Qtes manquantes
        total_gaz_manquantes = somme_cap_gaz - somme_qte_gaz_dispo
        total_dies_manquantes = somme_cap_dies - somme_qte_dies_dispo

        return {
            CAPACITE_GAZOLINE: somme_cap_gaz,
            QTE_GAL_GAZOLINE_DISPO: somme_qte_gaz_dispo,
            QTE_GAL_GAZOLINE_CONSOMMEE: somme_gaz_cons,
            TOTAL_GAL_GAZOLINE_MANQUEE: total_gaz_manquantes,

            CAPACITE_DIESEL: somme_cap_dies,
            QTE_GAL_DIESEL_DISPO: somme_qte_dies_dispo,
            QTE_GAL_DIESEL_CONSOMMEE: somme_dies_cons,
            TOTAL_GAL_DIESEL_MANQUEE: total_dies_manquantes
        }

    def afficherQuantiteGallon(self, ):
        for k, val in functions.all_stations.items():
            if val.items():
                print(f"\n STATION {k.upper()}: \n")
                input("Press any key to continue")
                statsessence = self.qteEssenceStats(nomstation=k)

                print("==========  GAZOLINE ===============")
                print(f"qte gazoline disponible -> {statsessence[QTE_GAL_GAZOLINE_DISPO]}")
                print(
                    f"Qte gazoline consommee -> {statsessence[QTE_GAL_GAZOLINE_CONSOMMEE]}")
                print("==========  DIESEL ===============")
                print(f"qte diesel disponible -> {val[QTE_GAL_DIESEL_DISPO]}")
                print(f"Qte diesel consommee -> {statsessence[QTE_GAL_DIESEL_CONSOMMEE]}")

        somme_quantites = self.sommeQtes()
        if somme_quantites.__sizeof__() > 0:
            print("========== TOTAL DES STATION ===============")
            print(f"Qte gazoline manquee : {somme_quantites[TOTAL_GAL_GAZOLINE_MANQUEE]}")
            print(f"Qte diesel manquee : {somme_quantites[TOTAL_GAL_DIESEL_MANQUEE]}")

        input("Press any key to continue")
