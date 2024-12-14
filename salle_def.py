
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox, END
from tkinter.ttk import Combobox

from salle import *
import Menu
class salleUI:
    def __init__(self, root, controller):
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.window = root
        self.window.geometry("900x500")
        self.window.configure(bg="#FFFFFF")
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\salle")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=900,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Store references to images
        self.images = {}

        self.setup_ui()
    def relative_to_assets(self,path: str) -> Path:
            return self.ASSETS_PATH / Path(path)
    def setup_ui(self):
        # Adding images
        self.add_image("image_1.png", 299.0, 325.0)
        self.add_image("image_2.png", 738.0, 305.0)
        self.add_image("image_3.png", 505.0, 59.0)

        # Adding entries

        self.barreRechercheF = self.add_entry(113.0, 141.0, 676.0, 22.0, "entry_1.png", 451.0, 153.0)
        self.id_blocF = self.add_entry(731.0, 338.0, 134.0, 15.0, "entry_2.png", 798.0, 346.5)
        self.capaciteF = self.add_entry(731.0, 308.0, 134.0, 15.0, "entry_3.png", 798.0, 316.5)
        self.nom_salleF = self.add_entry(731.0, 278.0, 134.0, 15.0, "entry_4.png", 798.0, 286.5)
        self.id_salleF = self.add_entry(731.0, 248.0, 134.0, 15.0, "entry_5.png", 798.0, 256.5)

        # Adding buttons
        self.rechercher = self.add_button(794.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.ajouter = self.add_button(798.0, 431.0, 87.0, 22.0, "button_2.png", self.addSalle)
        self.modifier = self.add_button(602.0, 431.0, 87.0, 22.0, "button_3.png", self.updateSalle)
        self.supprimer = self.add_button(700.0, 431.0, 87.0, 22.0, "button_4.png", self.deletesalle)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id = self.add_button(18.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        self.window.resizable(False, False)

    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")


    def add_entry(self, x, y, width, height, image_file, bg_x, bg_y):
        self.add_image(image_file, bg_x, bg_y)
        entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)
        return entry


    def add_button(self, x, y, width, height, image_file, command):
        self.add_image(image_file, x + width / 2, y + height / 2)
        button = Button(
            image=self.images[image_file],
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat",
            cursor="hand2"
        )
        button.place(x=x, y=y, width=width, height=height)

    def displaydata(self):
        self.loadSalles()

    def loadSalles(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        salles = self.controller.getAllSalles()
        for salle in salles:
            self.tree.insert("", "end", values=salle)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addSalle(self):
        print("Ajouter un étudiant")
        # Code pour ajouter un étudiant, par exemple :
        salle = salleC(None, self.nom_salleF.get(), self.capaciteF.get(), self.id_blocF.get())
        self.controller.addSalle(salle)
        self.loadSalles()
        self.clearForm()

    def updateSalle(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun étudiant sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_salle = values[0]

            salle = salleC(
                id_salle=int(id_salle),
                nom_salle=self.nom_salleF.get(),
                capacite=self.capaciteF.get(),
                id_bloc=self.id_blocF.get(),
            )

            self.controller.updateSalle(salle)
            self.loadSalles()
            self.clearForm()
            messagebox.showinfo("Succès", "Salle modifié avec succès.")
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deletesalle(self):
        print("delete salle")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_salle = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteSalle(id_salle)
            self.loadSalles()
            self.clearForm()



        else:
            print("No student selected")
            messagebox.showinfo("Error", "No student selected")

    def fillForm(self, salle):
        self.clearForm()
        self.nom_salleF.insert(0, salle.nom_salle)
        self.capaciteF.insert(0, salle.capacite)
        self.id_blocF.insert(0, salle.id_bloc)


    def clearForm(self):
        widgets = [self.nom_salleF, self.capaciteF, self.id_blocF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_salleF = None

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
            self.window,
            values=values
        )
        combobox.place(x=x, y=y, width=width, height=height)
        #combobox.current(default_index)  # Définit la sélection par défaut
        return combobox

    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.window, columns=(
            "id_salle", "nom_salle", "capacite", "id_bloc"
        ), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_salle", text="ID Salle")
        self.tree.heading("nom_salle", text="Nom Salle")
        self.tree.heading("capacite", text="Capacite")
        self.tree.heading("id_bloc", text="ID Bloc")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_salle", width=150, anchor="center")
        self.tree.column("nom_salle", width=150, anchor="center")
        self.tree.column("capacite", width=150, anchor="center")
        self.tree.column("id_bloc", width=150, anchor="center")



        # Ajout d'une barre de défilement verticale
        scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Placement du Treeview et de la barre de défilement
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)

        # Définition des styles pour les lignes
        self.tree.tag_configure("evenrow", background="#ffffff")
        self.tree.tag_configure("oddrow", background="#f0f0f0")

        # Placement dans un canvas si nécessaire
        if self.canvas:
            self.canvas.create_window(280.0, 330.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            salle_data = item_data["values"]
            salle_id = salle_data[0]
            salle = self.controller.getSalleById(salle_id)
            print("Salle sélectionné :", salle_data)
            self.fillForm(salle)






