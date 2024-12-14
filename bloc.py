class blocC:
    def __init__(self, id_bloc, nom_bloc, nbr_salle):
        self.id_bloc = id_bloc
        self.nom_bloc = nom_bloc
        self.nbr_salle = nbr_salle
    def getValues(self):
        return self.id_bloc, self.nom_bloc, self.nbr_salle
