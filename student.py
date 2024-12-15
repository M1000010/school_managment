
class etudiant:
    def __init__(self, id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd, mail_etd, filiere, id_niv):
        self.id_etd = id_etd
        self.cin_etd = cin_etd
        self.cne_etd = cne_etd
        self.nom_etd = nom_etd
        self.prenom_etd = prenom_etd
        self.date_n_etd = date_n_etd
        self.num_etd = num_etd
        self.mail_etd = mail_etd
        self.filiere = filiere
        self.id_niv = id_niv
    def getValues(self):
        return self.id_etd, self.cin_etd, self.cne_etd, self.nom_etd, self.prenom_etd, self.date_n_etd, self.num_etd, self.mail_etd, self.filiere, self.id_niv