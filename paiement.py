class paiementC:
    def __init__(self, id_paiement, montant, date_paiement, statut, id_etd):
        self.id_paiement = id_paiement
        self.montant = montant
        self.date_paiement = date_paiement
        self.statut = statut
        self.id_etd = id_etd

    def getValues(self):
        return self.id_paiement, self.montant, self.date_paiement, self.statut, self.id_etd
