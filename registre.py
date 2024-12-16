
class userC:
    def __init__(self, id_user, username, password, Role):
        self.id_user = id_user
        self.username = username
        self.password = password
        self.Role = Role

    def getValues(self):
        return self.id_user, self.username, self.password, self.Role