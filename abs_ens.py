
class abs_ensC:
    def __init__(self, id_abs_ens, date_abs_ens, periode_abs_ens, motif_ens, id_ens):
        self.id_abs_ens = id_abs_ens
        self.date_abs_ens = date_abs_ens
        self.periode_abs_ens = periode_abs_ens
        self.motif_ens = motif_ens
        self.id_ens = id_ens

    def getValues(self):
        return self.id_abs_ens, self.date_abs_ens, self.periode_abs_ens, self.motif_ens, self.id_ens