
class evalC:
    def __init__(self, id_eval, date_eval, type_eval, h_debut_eval, h_fin_eval, id_module):
        self.id_eval = id_eval
        self.type_eval = type_eval
        self.date_eval = date_eval
        self.h_debut_eval = h_debut_eval
        self.h_fin_eval = h_fin_eval
        self.id_module = id_module


    def getValues(self):
        return self.id_eval, self.date_eval, self.type_eval, self.h_debut_eval, self.h_fin_eval, self.id_module