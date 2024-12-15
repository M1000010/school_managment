
class seanceC:
    def __init__(self, id_seance, date_seance, h_debut_seance, h_fin_seance, type_seance,id_salle, id_ens):
        self.id_seance = id_seance
        self.date_seance = date_seance
        self.h_debut_seance = h_debut_seance
        self.h_fin_seance = h_fin_seance
        self.type_seance = type_seance
        self.id_salle = id_salle
        self.id_ens = id_ens
    def getValues(self):
        return (self.id_seance, self.date_seance, self.h_debut_seance, self.h_fin_seance, self.type_seance,
                self.id_salle, self.id_ens)