from tkinter.ttk import Combobox

"""import paiement
import Filiere
import niveau
import abs_enseign
import absence_etd
import bloc
import enseignant
import evaluation
import module
import salle
import seance
import specialite
import Student"""
from tkcalendar import DateEntry

def add_date_entry(self, x, y, width, height, image_file, bg_x, bg_y):
    """
    Ajoute un champ de saisie de date avec un arrière-plan et un format de date.
    """
    self.add_image(image_file, bg_x, bg_y)
    date_entry = DateEntry(
        self.root,
        width=int(width / 10),  # Ajuste la largeur
        background='white',
        foreground='black',
        borderwidth=0,
        date_pattern='yyyy-mm-dd'  # Modifiez selon le format souhaité

    )
    date_entry.place(x=x, y=y, width=width, height=height)
    return date_entry


def add_combobox(self, x, y, width, height, image_file, bg_x, bg_y, values):
    """
    Ajoute un champ déroulant (Combobox) à la fenêtre.

    Args:
        x (float): Position x du Combobox.
        y (float): Position y du Combobox.
        width (float): Largeur du Combobox.
        height (float): Hauteur du Combobox.
        values (list): Liste des options à afficher dans le Combobox.
        default_index (int): Index de l'option par défaut sélectionnée.

    Returns:
        Combobox: L'instance de Combobox créée.
    """
    self.add_image(image_file, bg_x, bg_y)
    combobox = Combobox(
        self.root,
        values=values
    )
    combobox.place(x=x, y=y, width=width, height=height)
    # combobox.current(default_index)  # Définit la sélection par défaut
    return combobox