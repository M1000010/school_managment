from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, END, ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

import Menu
from ens import ensC


class ensUI:
    def __init__(self, window, controller):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\enseign")
        self.window = window
        self.controller = controller
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
        self.add_image("image_1.png", 450.0, 251.0)
        self.add_image("image_2.png", 407.0, 410.0)
        self.add_image("image_3.png", 505.0, 59.0)

        # Adding entries

        self.date_n_ensF = self.add_date_entry(223.0, 463.0, 135.0, 20.0, "entry_1.png", 292.0, 471.5)
        self.id_moduleF = self.add_entry(572.0, 453.0, 135.0, 16.0, "entry_2.png", 639.5, 462.0)
        self.id_specialiteF = self.add_entry(572.0, 420.0, 135.0, 16.0, "entry_3.png", 639.5, 429.0)
        self.mail_ensF = self.add_entry(572.0, 386.0, 135.0, 16.0, "entry_4.png", 639.5, 395.0)
        self.num_ensF = self.add_entry(572.0, 353.0, 135.0, 16.0, "entry_5.png", 639.5, 362.0)
        self.prenom_ensF = self.add_entry(225.0, 434.0, 134.0, 14.0, "entry_6.png", 292.0, 442.0)
        self.nom_ensF = self.add_entry(225.0, 404.0, 134.0, 15.0, "entry_7.png", 292.0, 412.5)
        self.cin_ensF = self.add_entry(225.0, 375.0, 134.0, 14.0, "entry_8.png", 292.0, 383.0)
        self.id_ensF = self.add_entry(225.0, 345.0, 134.0, 15.0, "entry_9.png", 292.0, 353.5)
        self.barre_rechercheF = self.add_entry(109.0, 141.0, 676.0, 22.0, "entry_10.png", 447.0, 153.0)

        # Adding buttons
        self.ajouter = self.add_button(790.0, 346.0, 87.0, 22.0, "button_1.png", self.addEns)
        self.modifier = self.add_button(790.0, 399.0, 87.0, 22.0, "button_2.png", self.updateEns)
        self.supprimer = self.add_button(790.0, 452.0, 87.0, 22.0, "button_3.png", self.deleteEns)
        self.rechercher = self.add_button(790.0, 141.0, 87.0, 23.0, "button_4.png", "button_4 clicked")
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id = self.add_button(12.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        self.Table()
        self.loadEnss()

    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()
    def displaydata(self):
        self.loadEnss()

    def loadEnss(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        enss = self.controller.getAllEnss()
        for ens in enss:
            self.tree.insert("", "end", values=ens)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addEns(self):
        print("Ajouter un étudiant")
        # Code pour ajouter un étudiant, par exemple :
        ens = ensC(None, self.cin_ensF.get(), self.nom_ensF.get(), self.prenom_ensF.get(),
                   self.date_n_ensF.get(), self.num_ensF.get(), self.mail_ensF.get(),
                   self.id_specialiteF.get(), self.id_moduleF.get())
        self.controller.addEns(ens)
        self.loadEnss()
        self.clearForm()


    def updateEns(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun enseignant sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_ens = values[0]

            ens = ensC(
                id_ens=int(id_ens),
                cin_ens=self.cin_ensF.get(),
                nom_ens=self.nom_ensF.get(),
                prenom_ens=self.prenom_ensF.get(),
                date_n_ens=self.date_n_ensF.get(),
                num_ens= self.num_ensF.get(),
                mail_ens=self.mail_ensF.get(),
                id_specialite=self.id_specialiteF.get(),
                id_module=self.id_moduleF.get()
            )

            self.controller.updateEns(ens)
            self.loadEnss()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteEns(self):
        print("delete enseignant")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_ens = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteEns(id_ens)
            self.loadEnss()
            self.clearForm()



        else:
            messagebox.showinfo("Error", "No enseignant selected")

    def fillForm(self, ens):
        self.clearForm()
        self.cin_ensF.insert(0, ens.cin_ens)
        self.nom_ensF.insert(0, ens.nom_ens)
        self.prenom_ensF.insert(0, ens.prenom_ens)
        self.date_n_ensF.insert(0, ens.date_n_ens)
        self.num_ensF.insert(0, ens.num_ens)
        self.mail_ensF.insert(0, ens.mail_ens)
        self.id_specialiteF.insert(0, ens.id_specialite)
        self.id_moduleF.insert(0, ens.id_module)

    def clearForm(self):
        widgets = [self.cin_ensF, self.nom_ensF, self.prenom_ensF, self.date_n_ensF,
                   self.num_ensF, self.mail_ensF, self.id_specialiteF, self.id_moduleF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_ensF = None


    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.window, columns=(
            "id_ens", "cin_ens", "nom_ens", "prenom_ens", "date_n_ens",
            "num_ens", "mail_ens", "id_specialite", "id_module"
        ), show="headings", height=5)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_ens", text="ID enseignant")
        self.tree.heading("cin_ens", text="CIN")
        self.tree.heading("nom_ens", text="Nom")
        self.tree.heading("prenom_ens", text="Prénom")
        self.tree.heading("date_n_ens", text="Date de naissance")
        self.tree.heading("num_ens", text="Numéro Tel")
        self.tree.heading("mail_ens", text="Mail")
        self.tree.heading("id_specialite", text="ID Specialite")
        self.tree.heading("id_module", text="ID Module")


        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_ens", width=90, anchor="center")
        self.tree.column("cin_ens", width=100, anchor="center")
        self.tree.column("nom_ens", width=100, anchor="center")
        self.tree.column("prenom_ens", width=110, anchor="center")
        self.tree.column("date_n_ens", width=110, anchor="center")
        self.tree.column("num_ens", width=110, anchor="center")
        self.tree.column("mail_ens", width=110, anchor="center")
        self.tree.column("id_specialite", width=90, anchor="center")
        self.tree.column("id_module", width=80, anchor="center")


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
            self.canvas.create_window(450.0, 250.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            ens_data = item_data["values"]
            id_ens = ens_data[0]
            ens = self.controller.getEnsById(id_ens)
            print("Étudiant sélectionné :", ens_data)
            self.fillForm(ens)









