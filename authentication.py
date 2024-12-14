class authentication:
    def __init__(self, id_auth, username, password):
        self.idauth = id_auth
        self.username = username
        self.password = password
    def getValues(self):
        return self.idauth, self.username, self.password