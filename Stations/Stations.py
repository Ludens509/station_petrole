from lib2to3.pgen2.token import PERCENT

import functions
from functions import GAZOLINE_CONST, DIESEL_CONST, CAPACITE_GAZOLINE, CAPACITE_DIESEL, QTE_GAL_GAZOLINE_DISPO, \
    QTE_GAL_DIESEL_DISPO, QTE_GAL_GAZOLINE_CONSOMMEE, QTE_GAL_DIESEL_CONSOMMEE, \
    PERCENT_GAL_GAZOLINE, PERCENT_GAL_DIESEL, QTE_GAL_GAZOLINE_MANQUEE, QTE_GAL_DIESEL_MANQUEE, \
    TOTAL_GAL_DIESEL_MANQUEE, TOTAL_GAL_GAZOLINE_MANQUEE

import functions as fct


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
        # self.qte_gallon_gazoline_dispo = self.capacite_gazoline
        # self.qte_gallon_diesel_dispo = self.capacite_diesel

        # functions to change percent
        self.changePourcentageGazoline(nom=nom)
        self.changePourcentageDiesel(nom=nom)

        if self.nom == fct.LALUE_CONST or self.nom == fct.TABARRE_CONST \
                or self.nom == fct.CLERCINE_CONST \
                or self.nom == fct.PETION_VILLE_CONST:
            fct.all_stations.update({
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

    def getCapaciteGazoline(self, nom: str):
        if functions.findIfStationExist(name=nom):
            self.capacite_gazoline = fct.all_stations[nom][CAPACITE_GAZOLINE]
            return self.capacite_gazoline
        return 0

    def setCapaciteGazoline(self, nom: str, newCapacite_gazoline: float):
        self.capacite_gazoline = newCapacite_gazoline
        fct.all_stations[nom][CAPACITE_GAZOLINE] = newCapacite_gazoline
        # change qte dispo
        self.qte_gallon_gazoline_dispo = newCapacite_gazoline
        fct.all_stations[nom][QTE_GAL_GAZOLINE_DISPO] = self.qte_gallon_gazoline_dispo
        # functions to change percent
        self.changePourcentageGazoline(nom=nom)

    def getCapaciteDiesel(self, nom: str):
        self.capacite_diesel = fct.all_stations[nom][CAPACITE_DIESEL]
        return self.capacite_diesel

    def setCapaciteDiesel(self, nom: str, newCapacite_diesel: float):
        self.capacite_diesel = newCapacite_diesel
        fct.all_stations[nom][CAPACITE_DIESEL] = newCapacite_diesel
        # change qte dispo
        self.qte_gallon_diesel_dispo = newCapacite_diesel
        fct.all_stations[nom][QTE_GAL_DIESEL_DISPO] = self.qte_gallon_diesel_dispo
        # functions to change percent
        self.changePourcentageDiesel(nom=nom)

    def getQte_diesel(self, nom: str):
        self.qte_gallon_diesel_dispo = fct.all_stations[nom][QTE_GAL_DIESEL_DISPO]
        return self.qte_gallon_diesel_dispo

    def setQte_diesel(self, nom: str, newQte_diesel: float):
        self.qte_gallon_diesel_dispo = newQte_diesel + self.qte_gallon_diesel_dispo
        fct.all_stations[nom][QTE_GAL_DIESEL_DISPO] = self.qte_gallon_diesel_dispo
        if functions.findIfStationExist(nom):
            self.changePourcentageDiesel(nom=nom)

    def getQte_gazoline(self, nom: str):
        self.qte_gallon_gazoline_dispo = fct.all_stations[nom][QTE_GAL_GAZOLINE_DISPO]
        return self.qte_gallon_gazoline_dispo

    def setQte_gazoline(self, nom: str, newQte_gazoline: float):
        self.qte_gallon_gazoline_dispo = newQte_gazoline + self.qte_gallon_gazoline_dispo
        fct.all_stations[nom][QTE_GAL_GAZOLINE_DISPO] = self.qte_gallon_gazoline_dispo
        if functions.findIfStationExist(nom):
            self.changePourcentageGazoline(nom=nom)

    def getPourcentageGazoline(self, ) -> float:
        return self.pourcentage_gazoline

    def changePourcentageGazoline(self, nom: str):

        if fct.findIfStationExist(nom):
            cap_gaz = fct.all_stations[nom][fct.CAPACITE_GAZOLINE]
            self.capacite_gazoline = cap_gaz or 0
            if cap_gaz <= 0:
                return
            self.pourcentage_gazoline = self.qte_gallon_gazoline_dispo / self.capacite_gazoline * 100
            fct.all_stations[nom][fct.PERCENT_GAL_GAZOLINE] = self.pourcentage_gazoline

    def getPourcentageDiesel(self, ):
        return self.pourcentage_diesel

    def changePourcentageDiesel(self, nom: str):
        if fct.findIfStationExist(nom):
            cap_dies = fct.all_stations[nom][fct.CAPACITE_DIESEL]
            self.capacite_diesel = cap_dies or 0
            if cap_dies <= 0:
                return
            self.pourcentage_diesel = self.qte_gallon_diesel_dispo / self.capacite_diesel * 100
            fct.all_stations[nom][fct.PERCENT_GAL_DIESEL] = self.pourcentage_diesel

    def afficher(self, ):
        if len(fct.all_stations) == 0:
            print("\nPas de station trouve")

        for k, val in fct.all_stations.items():
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
        percent_gaz_dispo = float()
        percent_dies_dispo = float()
        cap_gaz = float()
        cap_dies = float()

        if nomstation in fct.all_stations:
            cap_gaz = fct.all_stations[nomstation][CAPACITE_GAZOLINE]
            qte_gaz_dispo = fct.all_stations[nomstation][QTE_GAL_GAZOLINE_DISPO]
            qte_gaz_consomee = fct.all_stations[nomstation][CAPACITE_GAZOLINE] - \
                               fct.all_stations[nomstation][QTE_GAL_GAZOLINE_DISPO]
            percent_gaz_dispo = fct.all_stations[nomstation][PERCENT_GAL_GAZOLINE]

            cap_dies = fct.all_stations[nomstation][CAPACITE_DIESEL]
            qte_dies_dispo = fct.all_stations[nomstation][QTE_GAL_DIESEL_DISPO]
            qte_dies_consommee = fct.all_stations[nomstation][QTE_GAL_DIESEL_DISPO] - \
                                 fct.all_stations[nomstation][QTE_GAL_DIESEL_DISPO]
            percent_dies_dispo = fct.all_stations[nomstation][PERCENT_GAL_DIESEL]

            data_essence.update({
                CAPACITE_GAZOLINE: cap_gaz,
                QTE_GAL_GAZOLINE_DISPO: qte_gaz_dispo,
                PERCENT_GAL_GAZOLINE: percent_gaz_dispo,
                QTE_GAL_GAZOLINE_CONSOMMEE: qte_gaz_consomee,

                CAPACITE_DIESEL: cap_dies,
                QTE_GAL_DIESEL_DISPO: qte_dies_dispo,
                PERCENT_GAL_DIESEL: percent_dies_dispo,
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

        for key, val in fct.all_stations.items():
            statsessence = self.qteEssenceStats(nomstation=key)

            somme_cap_gaz = somme_cap_gaz + statsessence[CAPACITE_GAZOLINE]
            somme_cap_dies = somme_cap_dies + statsessence[CAPACITE_DIESEL]

            somme_qte_gaz_dispo = somme_qte_gaz_dispo + \
                                  statsessence[QTE_GAL_GAZOLINE_DISPO]
            somme_qte_dies_dispo = somme_qte_dies_dispo + \
                                   statsessence[QTE_GAL_DIESEL_DISPO]

            somme_gaz_cons = somme_gaz_cons + \
                             statsessence[QTE_GAL_GAZOLINE_CONSOMMEE]
            somme_dies_cons = somme_dies_cons + \
                              statsessence[QTE_GAL_GAZOLINE_CONSOMMEE]
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
        for k, val in fct.all_stations.items():
            if val.items():
                print(f"\n STATION {k.upper()}: \n")
                input("Press any key to continue")
                statsessence = self.qteEssenceStats(nomstation=k)

                print("\n---------  GAZOLINE ---------")
                print(
                    f"qte gazoline disponible -> {statsessence[QTE_GAL_GAZOLINE_DISPO]}")
                print(
                    f"Qte gazoline consommee -> {statsessence[QTE_GAL_GAZOLINE_CONSOMMEE]}")
                print("---------  DIESEL ---------")
                print(f"qte diesel disponible -> {val[QTE_GAL_DIESEL_DISPO]}")
                print(
                    f"Qte diesel consommee -> {statsessence[QTE_GAL_DIESEL_CONSOMMEE]}")

        somme_quantites = self.sommeQtes()
        if len(somme_quantites) > 0:
            print("\n\t\t=============== TOTAL DES STATIONS ===============\n")
            print(
                f"Qte gazoline manquee : {somme_quantites[TOTAL_GAL_GAZOLINE_MANQUEE]}")
            print(
                f"Qte diesel manquee : {somme_quantites[TOTAL_GAL_DIESEL_MANQUEE]}\n")

        input("Press any key to continue")

    @staticmethod
    def diminuerQteGazoline(station: str, qte: float) -> bool:
        if fct.findIfStationExist(station):
            qte_dispo_in_dict = fct.all_stations[station][fct.QTE_GAL_GAZOLINE_DISPO]
            cap_gaz = fct.all_stations[station][fct.CAPACITE_GAZOLINE]

            if qte_dispo_in_dict >= qte:
                fct.all_stations[station][fct.QTE_GAL_GAZOLINE_DISPO] = qte_dispo_in_dict - qte
                # recuperer la nouvelle valeur
                qte_dispo_in_dict = fct.all_stations[station][fct.QTE_GAL_GAZOLINE_DISPO]
                fct.all_stations[station][fct.PERCENT_GAL_GAZOLINE] = qte_dispo_in_dict / cap_gaz * 100
                return True
            else:
                print("La quantite saisie est supperieur a la quantite disponible")
                return False
        else:
            print("Il n'y a pas de station portant ce nom")
            return False

    @staticmethod
    def diminuerQteDiesel(station: str, qte: float) -> bool:
        if fct.findIfStationExist(station):
            qte_dispo_in_dict = fct.all_stations[station][fct.QTE_GAL_DIESEL_DISPO]
            cap_dies = fct.all_stations[station][fct.CAPACITE_DIESEL]

            if qte_dispo_in_dict >= qte:
                fct.all_stations[station][fct.QTE_GAL_DIESEL_DISPO] = qte_dispo_in_dict - qte
                # recuperer la nouvelle valeur
                qte_dispo_in_dict = fct.all_stations[station][fct.QTE_GAL_DIESEL_DISPO]
                fct.all_stations[station][fct.PERCENT_GAL_DIESEL] = qte_dispo_in_dict / cap_dies * 100
                return True
            else:
                print("La quantite saisie est supperieur a la quantite disponible")
                return False
        else:
            print("Il n'y a pas de station portant ce nom")
            return False
