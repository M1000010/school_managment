from tkinter import Tk

import mysql.connector

from authentication_base import authController
import authentication_def

class authMain:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )
        self.controller = authController(self.connection)
        self.root = Tk()


        self.ui = authentication_def.logUI(self.root, self.controller)
        self.initialize_ui()

    def initialize_ui(self):

        self.ui.setup_ui()
        self.ui.salam()
    def run(self):
            # Lancer la boucle principale de l'application
            self.root.resizable(False, False)
            self.root.mainloop()



if __name__ == "__main__":
    app = authMain()
    app.run()
