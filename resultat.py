
class resultatC:
    def __init__(self, id_resultat, notes, mention, id_etd):
        self.id_etd = id_etd
        self.id_resultat = id_resultat
        self.mention = mention
        self.notes = notes

    def getValues(self):
        return self.id_resultat, self.notes, self.mention, self.id_etd