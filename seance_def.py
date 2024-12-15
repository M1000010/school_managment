from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk, END
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

import Menu
from seance import seanceC


class seanceUI :
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\seance")

        self.window.geometry("900x500+180+100")
        self.window.configure(bg="#FFFFFF")

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

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def add_time_entry(self, x, y, width, height, image_file, bg_x, bg_y):
        """
        Ajoute un champ de saisie d'heure avec un arrière-plan et un format spécifique.
        """
        # Ajout de l'image d'arrière-plan
        self.add_image(image_file, bg_x, bg_y)

        # Création du champ de saisie pour l'heure
        time_entry = Entry(
            self.window,
            width=int(width / 10),  # Ajuste la largeur
            bg='white',
            fg='black',
            borderwidth=0,
            justify='center'  # Aligne le texte au centre
        )

        # Placement du champ dans la fenêtre
        time_entry.place(x=x, y=y, width=width, height=height)

        # Définition d'un format d'exemple "hh:mm" par défaut
        time_entry.insert(0, "hh:mm")

        return time_entry
    def add_date_entry(self, x, y, width, height, image_file, bg_x, bg_y):
        """
        Ajoute un champ de saisie de date avec un arrière-plan et un format de date.
        """
        self.add_image(image_file, bg_x, bg_y)
        date_entry = DateEntry(
            self.window,
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
            self.window,
            values=values
        )
        combobox.place(x=x, y=y, width=width, height=height)
        #combobox.current(default_index)  # Définit la sélection par défaut
        return combobox
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


    def setup_ui(self):
        # Adding images

        self.add_image("image_1.png", 297.0, 317.0)
        self.add_image("image_2.png", 736.0, 296.0)
        self.add_image("image_3.png", 505.0, 59.0)

        self.typeSE = ["Cours", "TD", "TP"]

        # Adding entries

        self.barreRechercheF = self.add_entry(110.0, 141.0, 676.0, 22.0, "entry_1.png", 448.0, 153.0)
        self.type_seanceF = self.add_combobox(725.0, 318.0, 134.0, 18.0, "entry_2.png", 794.0, 326.5, self.typeSE)
        self.h_fin_seanceF = self.add_time_entry(727.0, 288.0, 134.0, 15.0, "entry_3.png", 794.0, 296.5)
        self.id_ensF = self.add_entry(727.0, 379.0, 134.0, 15.0, "entry_4.png", 794.0, 387.5)
        self.id_salleF = self.add_entry(727.0, 349.0, 134.0, 15.0, "entry_5.png", 794.0, 357.5)
        self.h_debut_seanceF = self.add_time_entry(727.0, 258.0, 134.0, 15.0, "entry_6.png", 794.0, 266.5)
        self.date_seanceF = self.add_date_entry(725.0, 228.0, 134.0, 18.0, "entry_7.png", 794.0, 236.5)
        self.id_seanceF = self.add_entry(727.0, 198.0, 134.0, 15.0, "entry_8.png", 794.0, 206.5)

        # Adding buttons

        self.rechercher = self.add_button(791.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.ajouter = self.add_button(790.0, 430.0, 87.0, 22.0, "button_2.png", self.addSeance)
        self.modifier = self.add_button(594.0, 430.0, 87.0, 22.0, "button_3.png", self.updateSeance)
        self.supprimer = self.add_button(692.0, 430.0, 87.0, 22.0, "button_4.png", self.deleteSeance)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id = self.add_button(13.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        self.Table()
        self.loadSeances()


    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()
    def displaydata(self):
        self.loadSeances()

    def loadSeances(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        seances = self.controller.getAllSeances()
        for seance in seances:
            self.tree.insert("", "end", values=seance)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addSeance(self):
        # Code pour ajouter un étudiant, par exemple :
        seance = seanceC(None, self.date_seanceF.get(), self.h_debut_seanceF.get(), self.h_fin_seanceF.get(),
                         self.type_seanceF.get(),self.id_salleF.get(), self.id_ensF.get(),)
        self.controller.addSeance(seance)
        self.loadSeances()
        self.clearForm()


    def updateSeance(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun seance sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_seance = values[0]

            seance = seanceC(
                id_seance = int(id_seance),
                date_seance = self.date_seanceF.get(),
                h_debut_seance = self.h_debut_seanceF.get(),
                h_fin_seance = self.h_fin_seanceF.get(),
                type_seance = self.type_seanceF.get(),
                id_salle = self.id_salleF.get(),
                id_ens = self.id_ensF.get()
            )

            self.controller.updateSeance(seance)
            self.loadSeances()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteSeance(self):
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_seance = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteSeance(id_seance)
            self.loadSeances()
            self.clearForm()



        else:
            print("No student selected")
            messagebox.showinfo("Error", "No student selected")

    def fillForm(self, seance):
        self.clearForm()
        self.date_seanceF.insert(0, seance.date_seance)
        self.h_debut_seanceF.insert(0, seance.h_debut_seance)
        self.h_fin_seanceF.insert(0, seance.h_fin_seance)
        self.type_seanceF.insert(0, seance.type_seance)
        self.id_salleF.insert(0, seance.id_salle)
        self.id_ensF.insert(0, seance.id_ens)


    def clearForm(self):
        widgets = [self.date_seanceF, self.h_debut_seanceF, self.h_fin_seanceF,
                   self.type_seanceF, self.id_salleF, self.id_ensF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_seanceF = None


    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.window, columns=(
            "id_seance", "date_seance", "h_debut_seance", "h_fin_seance",
            "type_seance", "id_salle", "id_ens"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_seance", text="ID Seance")
        self.tree.heading("date_seance", text="Date Seance")
        self.tree.heading("h_debut_seance", text="Debut Seance")
        self.tree.heading("h_fin_seance", text="Fin Seance")
        self.tree.heading("type_seance", text="Type Seance")
        self.tree.heading("id_salle", text="ID Salle")
        self.tree.heading("id_ens", text="ID Enseignant")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_seance", width=80, anchor="center")
        self.tree.column("date_seance", width=90, anchor="center")
        self.tree.column("h_debut_seance", width=90, anchor="center")
        self.tree.column("h_fin_seance", width=90, anchor="center")
        self.tree.column("type_seance", width=80, anchor="center")
        self.tree.column("id_salle", width=80, anchor="center")
        self.tree.column("id_ens", width=80, anchor="center")



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
            self.canvas.create_window(285.0, 322.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            seance_data = item_data["values"]
            id_seance = seance_data[0]
            student = self.controller.getSeanceById(id_seance)
            print("Étudiant sélectionné :", seance_data)
            self.fillForm(student)







