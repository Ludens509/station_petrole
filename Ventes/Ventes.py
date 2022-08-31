import secrets

import functions as fct
from Stations.Stations import StationClass


class VentesClass:

    def __init__(self):
        self.id = None
        self.station_name = str()
        self.qte_diesel = float()
        self.qte_gazoline = float()
        self.prix_gazoline = fct.PRICE_GAZOLINE
        self.prix_diesel = fct.PRICE_DIESEL
        self.montant_gazoline = float()
        self.montant_diesel = float()
        self.montant_total = float()
        self.montant_versement_client = float()
        self.montant_remise = float()
        self.date_vente = str()
        self.v_station = StationClass()

    def generer_id_vente(self):
        secret_id = str
        # generate 1 secure random numbers between 10 and 500
        for x in range(0, 1):
            secret_id = (10 + secrets.randbelow(500)).__str__()
        # recursive function : get unique ID in all_ventes
        if secret_id in fct.all_ventes:
            self.generer_id_vente()
        return secret_id

    def enregistrerVente(self, station_name: str, total_qte_gaz: float, total_qte_dies: float,
                         versement_client: float) -> float():

        self.id = self.generer_id_vente()
        self.date_vente = fct.generer_date()

        self.station_name = station_name
        self.qte_gazoline = total_qte_gaz
        self.qte_diesel = total_qte_dies

        self.montant_gazoline = self.qte_gazoline * self.prix_gazoline
        self.montant_diesel = self.qte_diesel * self.prix_diesel
        self.montant_total = self.montant_gazoline + self.montant_diesel

        self.montant_versement_client = versement_client

        # montant a payer est supperieur au montant verser par le client
        if self.montant_total > self.montant_versement_client:
            print("Le montant donne ne doit pas etre inferieur au montant a payer")
            return fct.AMOUNT_IS_UNDER_MISC

        self.montant_remise = self.montant_versement_client - self.montant_total

        if self.qte_gazoline < 0 or self.qte_diesel < 0:
            print("La quante ne doit pas etre inferieur a 0")
            return fct.ERROR_MISC

        elif self.qte_gazoline == 0:

            diminution_qte = self.v_station.diminuerQteDiesel(self.station_name, self.qte_diesel)
            if not diminution_qte:
                print("Impossible de diminuer la quantite de diesel")
                return fct.ERROR_MISC

            fct.all_ventes.append({
                fct.VENTE_ID: self.id,
                fct.VENTE_STATION: self.station_name,
                fct.VENTE_QTE_GAL_DIESEL: self.qte_diesel,
                fct.VENTE_MONTANT_DIESEL: self.montant_diesel,
                fct.VENTE_MONTANT_TOTAL: self.montant_total,
                fct.VENTE_VERSEMENT_CLIENT: self.montant_versement_client,
                fct.VENTE_REMISE: self.montant_remise,
                fct.VENTE_DATE: self.date_vente,
            })

        # end qte gazoline == 0
        elif self.qte_diesel == 0:

            diminution_qte = self.v_station.diminuerQteGazoline(self.station_name, self.qte_gazoline)
            if not diminution_qte:
                print("Impossible de diminuer la quantite de gazoline")
                return fct.ERROR_MISC

            fct.all_ventes.append({
                fct.VENTE_ID: self.id,
                fct.VENTE_STATION: self.station_name,
                fct.VENTE_QTE_GAL_GAZOLINE: self.qte_gazoline,
                fct.VENTE_MONTANT_GAZOLINE: self.montant_gazoline,
                fct.VENTE_MONTANT_TOTAL: self.montant_total,
                fct.VENTE_VERSEMENT_CLIENT: self.montant_versement_client,
                fct.VENTE_REMISE: self.montant_remise,
                fct.VENTE_DATE: self.date_vente,
            })

        # end qte diesel == 0
        else:

            diminution_qte = self.v_station.diminuerQteGazoline(self.station_name, self.qte_gazoline)
            if not diminution_qte:
                print("Impossible de diminuer la quantite de gazoline")
                return fct.ERROR_MISC
            diminution_qte = self.v_station.diminuerQteDiesel(self.station_name, self.qte_diesel)

            if not diminution_qte:
                print("Impossible de diminuer la quantite de diesel")
                return fct.ERROR_MISC

            fct.all_ventes.append({
                fct.VENTE_ID: self.id,
                fct.VENTE_STATION: self.station_name,
                fct.VENTE_QTE_GAL_GAZOLINE: self.qte_gazoline,
                fct.VENTE_MONTANT_GAZOLINE: self.montant_gazoline,
                fct.VENTE_QTE_GAL_DIESEL: self.qte_diesel,
                fct.VENTE_MONTANT_DIESEL: self.montant_diesel,
                fct.VENTE_MONTANT_TOTAL: self.montant_total,
                fct.VENTE_VERSEMENT_CLIENT: self.montant_versement_client,
                fct.VENTE_REMISE: self.montant_remise,
                fct.VENTE_DATE: self.date_vente,
            })

        # end qte gazoline and qte diesel != 0

        if self.montant_remise < 0:
            print("Montant remise is negative")
            return fct.ERROR_MISC
        else:
            return self.montant_remise

    def afficherVentes(self):

        if len(fct.all_ventes) > 0:
            for i in fct.all_ventes:
                for key, values in i.items():
                    print(f"{key.replace('_', ' ')} : {values} ")
                # end for
                print("\n")
            # end for
        else:
            print("\nNo sale found\n")

        # end if
