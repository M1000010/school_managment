
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import mysql.connector

import Menu
import register_def
from bloc_base import blocController
import bloc_def
from registre_base import registreController


class registreMain :
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )
        self.window = Tk()
        self.controller = registreController(self.connection)

        self.ui = register_def.registerUI(self.window, self.controller)

        # Initialiser l'interface utilisateur
        self.initialize_ui()

    def initialize_ui(self):
        # Charger les images et créer les éléments de l'interface

        # Ajoutez d'autres boutons et widgets similaires ici...

        self.ui.setup_ui()

    def run(self):
            self.window.mainloop()


if __name__ == "__main__":
        registre = registreMain()
        registre.run()




