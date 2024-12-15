
class ensC:
    def __init__(self, id_ens, cin_ens, nom_ens, prenom_ens, date_n_ens, num_ens, mail_ens, id_specialite, id_module):
        self.id_ens = id_ens
        self.cin_ens = cin_ens
        self.nom_ens = nom_ens
        self.prenom_ens = prenom_ens
        self.date_n_ens = date_n_ens
        self.num_ens = num_ens
        self.mail_ens = mail_ens
        self.id_specialite = id_specialite
        self.id_module = id_module
    def getValues(self):
        return (self.id_ens, self.cin_ens, self.nom_ens, self.prenom_ens, self.date_n_ens, self.num_ens, self.mail_ens,
                self.id_specialite, self.id_module)