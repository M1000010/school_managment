
from tkinter import Tk

import mysql.connector

import Menu
from salle_base import salleController
import salle_def


class salleMain:
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )
        self.controller = salleController(self.connection)

        self.window = Tk()
        self.ui = salle_def.salleUI(self.window, self.controller)

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

    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

if __name__ == "__main__":
    salle = salleMain()
    salle.run()






