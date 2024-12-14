class salleC:
    def __init__(self, id_salle, nom_salle, capacite, id_bloc):
        self.id_salle = id_salle
        self.nom_salle = nom_salle
        self.capacite = capacite
        self.id_bloc = id_bloc
    def getValues(self):
        return self.id_salle, self.nom_salle, self.capacite, self.id_bloc
