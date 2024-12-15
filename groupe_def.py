from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, END, ttk
import Menu
from groupe import *
from groupe_base import *
class groupeUI :
    def __init__(self,window, controller):
        self.root = window
        self.controller= controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\groupe")


        self.root.geometry("900x500+180+100")
        self.root.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.root,
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
        self.add_image("image_1.png", 305.0, 316.0)
        self.add_image("image_2.png", 505.0, 59.0)
        self.add_image("image_3.png", 747.0, 283.0)

        # Adding entries

        self.barreRechercheF = self.add_entry(109.0, 141.0, 676.0, 22.0, "entry_1.png", 447.0, 153.0)
        self.id_niveauF = self.add_entry(743.0, 314.0, 134.0, 19.0, "entry_2.png", 810.0, 324.5)
        self.nom_groupeF = self.add_entry(743.0, 277.0, 134.0, 19.0, "entry_3.png", 810.0, 287.5)
        self.id_groupeF = self.add_entry(743.0, 240.0, 134.0, 19.0, "entry_4.png", 810.0, 250.5)

        # Adding buttons
        self.rechercher = self.add_button(790.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.id= self.add_button(12.0, 141.0, 94.0, 23.0, "button_2.png","button_2 clicked" )
        self.ajouter = self.add_button(801.0, 377.0, 87.0, 22.0, "button_3.png", self.addGroup)
        self.modifier = self.add_button(605.0, 377.0, 87.0, 22.0, "button_4.png", self.updateGroupe)
        self.supprimer = self.add_button(703.0, 377.0, 87.0, 22.0, "button_5.png", self.deleteGroupe)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_6.png", self.open_menu)

        # self.root.resizable(False, False)
        self.Table()
        self.loadGroups()




    def open_menu(self):
        self.root.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()
    def displaydata(self):
        self.loadGroups()

    def loadGroups(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        groups = self.controller.getAllGroups()
        for groupe in groups:
            self.tree.insert("", "end", values=groupe)

    # Fonction d'ajout d'un groupe (à personnaliser selon votre logique)
    def addGroup(self):
        print("Ajouter un groupe")
        # Code pour ajouter un groupe, par exemple :
        group = groupeC(None, self.nom_groupeF.get(), self.id_niveauF.get())
        self.controller.addGroup(group)
        self.loadGroups()
        self.clearForm()

    def updateGroupe(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun groupe sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_grp = values[0]

            group = groupeC(
                id_grp=int(id_grp),
                nom_grp=self.nom_groupeF.get(),
                id_niv=self.id_niveauF.get(),

            )

            self.controller.updateGroupe(group)
            self.loadGroups()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteGroupe(self):
        print("delete groupe")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_grp = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteGroupe(id_grp)
            self.loadGroups()
            self.clearForm()



        else:
            print("No group selected")
            messagebox.showinfo("Error", "No group selected")

    def fillForm(self, group):
        self.clearForm()
        self.nom_groupeF.insert(0, group.nom_grp)
        self.id_niveauF.insert(0, group.id_niv)


    def clearForm(self):
        widgets = [self.nom_groupeF, self.id_niveauF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.idF = None

    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_grp", "nom_grp","id_niv"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_grp", text="ID groupe")
        self.tree.heading("nom_grp", text="Nom groupe")
        self.tree.heading("id_niv", text="ID niveau")

        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_grp", width=200, anchor="center")
        self.tree.column("nom_grp", width=200, anchor="center")
        self.tree.column("id_niv", width=200, anchor="center")

        # Ajout d'une barre de défilement verticale
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Placement du Treeview et de la barre de défilement
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)

        # Définition des styles pour les lignes
        self.tree.tag_configure("evenrow", background="#ffffff")
        self.tree.tag_configure("oddrow", background="#f0f0f0")

        # Placement dans un canvas si nécessaire
        if self.canvas:
            self.canvas.create_window(287.0, 320.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            group_data = item_data["values"]
            group_id = group_data[0]
            group = self.controller.getGroupeById(group_id)
            print("Groupe sélectionné :", group_data)
            self.fillForm(group)
