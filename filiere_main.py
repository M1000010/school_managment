from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel

import mysql.connector

import  Menu
from filiere_base import filiereController
from filiere_def import filiereUI


class filiereMain:
    def __init__(self):
        # Initialiser la connexion à la base de données MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )
        self.controller = filiereController(self.connection)

        self.window = Tk()

        # Charger les ressources
        self.ui = filiereUI(self.window, self.controller)

        # Initialiser l'interface utilisateur
        self.initialize_ui()

    def initialize_ui(self):
            # Charger les images et créer les éléments de l'interface

            # Ajoutez d'autres boutons et widgets similaires ici...

        self.ui.Table()
        self.ui.displaydata()
        self.ui.setup_ui()


    def run(self):
            # Lancer la boucle principale de l'application
            self.window.resizable(False, False)
            self.window.mainloop()


if __name__ == "__main__":
        app = filiereMain()
        app.run()




