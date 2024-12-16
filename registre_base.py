from tkinter import messagebox

import bcrypt



class registreController:
    def __init__(self, connection):
        self.connection = connection



    def addUser(self, username, password, role):
        try:
            cursor = self.connection.cursor()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            query = "INSERT INTO user (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, hashed_password, role))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de l'enregistrement : {e}")
            return False
        finally:
            cursor.close()



