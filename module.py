
class moduleC:
    def __init__(self, id_module, nom_module, coef, id_niv, id_ens):
        self.id_module = id_module
        self.nom_module = nom_module
        self.coef = coef
        self.id_niv= id_niv
        self.id_ens = id_ens
    def getValues(self):
        return self.id_module, self.nom_module, self.coef, self.id_niv, self.id_ens