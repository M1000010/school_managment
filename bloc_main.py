
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import mysql.connector

import Menu
from bloc_base import blocController
from bloc_def import blocUI


class blocMain :
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )
        self.window = Tk()
        self.controller = blocController(self.connection)

        self.ui = blocUI(self.window, self.controller)

        # Initialiser l'interface utilisateur
        self.initialize_ui()

    def initialize_ui(self):
        # Charger les images et créer les éléments de l'interface

        # Ajoutez d'autres boutons et widgets similaires ici...

        self.ui.Table()
        self.ui.displaydata()
        self.ui.setup_ui()

    def run(self):
            self.window.mainloop()


if __name__ == "__main__":
        bloc = blocMain()
        bloc.run()




