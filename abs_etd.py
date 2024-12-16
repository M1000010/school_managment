
class abs_etdC:
    def __init__(self, id_abs_etd, date_abs_etd, periode_abs_etd, motif_etd, id_seance, id_etd):
        self.id_abs_etd = id_abs_etd
        self.date_abs_etd = date_abs_etd
        self.periode_abs_etd = periode_abs_etd
        self.motif_etd = motif_etd
        self.id_seance = id_seance
        self.id_etd = id_etd
    def getValues(self):
        return self.id_abs_etd, self.date_abs_etd, self.periode_abs_etd, self.motif_etd, self.id_seance, self.id_etd