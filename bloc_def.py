
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, END, ttk
from tkinter.ttk import Combobox

import Menu
from bloc import blocC


class blocUI :
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\bloc")
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

    def setup_ui(self):
        # Adding images
        self.add_image("image_1.png", 300.0, 326.0)
        self.add_image("image_2.png", 739.0, 287.0)
        self.add_image("image_3.png", 505.0, 59.0)
        # Adding entries

        self.barreRechercheF = self.add_entry(115.0, 141.0, 676.0, 22.0, "entry_1.png", 453.0, 153.0)
        self.nbr_salleF = self.add_entry(733.0, 317.0, 136.0, 19.0, "entry_2.png", 801.0, 327.5)
        self.nom_blocF = self.add_entry(733.0, 281.0, 136.0, 20.0, "entry_3.png", 801.0, 292.0)
        self.id_blocF = self.add_entry(733.0, 246.0, 136.0, 18.0, "entry_4.png", 801.0, 256.0)


        # Adding buttons
        self.rechercher = self.add_button(796.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.id = self.add_button(18.0, 141.0, 94.0, 23.0, "button_2.png", "button_2 clicked")
        self.ajouter = self.add_button(791.0, 414.0, 87.0, 22.0, "button_3.png", self.addBloc)
        self.modifier = self.add_button(595.0, 414.0, 87.0, 22.0, "button_4.png", self.updateBloc)
        self.supprimer = self.add_button(693.0, 414.0, 87.0, 22.0, "button_5.png", self.deleteBloc)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_6.png", self.open_menu)



    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")


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


    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def displaydata(self):
        self.loadBlocs()

    def loadBlocs(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        blocs = self.controller.getAllBlocs()
        for bloc in blocs:
            self.tree.insert("", "end", values=bloc)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addBloc(self):
        print("Ajouter un étudiant")
        # Code pour ajouter un étudiant, par exemple :
        bloc = blocC(None, self.nom_blocF.get(), self.nbr_salleF.get())
        self.controller.addBloc(bloc)
        self.loadBlocs()
        self.clearForm()

    def updateBloc(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun Bloc sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_bloc = values[0]

            bloc = blocC(
                id_bloc=int(id_bloc),
                nom_bloc=self.nom_blocF.get(),
                nbr_salle=int(self.nbr_salleF.get()),

            )

            self.controller.updateBloc(bloc)
            self.loadBlocs()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteBloc(self):
        print("delete bloc")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_bloc = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteStudent(id_bloc)
            self.loadBlocs()
            self.clearForm()



        else:
            print("No student selected")
            messagebox.showinfo("Error", "No student selected")

    def fillForm(self, bloc):
        self.clearForm()
        self.nom_blocF.insert(0, bloc.nom_bloc)
        self.nbr_salleF.insert(0, bloc.nbr_salle)

    def clearForm(self):
        widgets = [self.nom_blocF, self.nbr_salleF]

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
        self.tree = ttk.Treeview(self.window, columns=(
            "id_bloc", "nom_bloc", "nbr_salle"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_bloc", text="ID Bloc")
        self.tree.heading("nom_bloc", text="Nom Bloc")
        self.tree.heading("nbr_salle", text="Nombre de salle")


        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_bloc", width=200, anchor="center")
        self.tree.column("nom_bloc", width=200, anchor="center")
        self.tree.column("nbr_salle", width=200, anchor="center")



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
            self.canvas.create_window(285.0, 330.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            bloc_data = item_data["values"]
            id_bloc = bloc_data[0]
            bloc = self.controller.getBlocById(id_bloc)
            print("Bloc sélectionné :", bloc_data)
            self.fillForm(bloc)




