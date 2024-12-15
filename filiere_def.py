from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, messagebox, ttk, END
import Menu
from filiere import filiereC


class filiereUI:
    def __init__(self, window, controller ):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\filiere")
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


    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def setup_ui(self):
            # Adding images
        self.add_image("image_1.png", 505.0, 59.0)
        self.add_image("image_2.png", 297.0, 323.0)
        self.add_image("image_3.png", 739.0, 290.0)
            # Adding entries

        self.rechercheF = self.add_entry(795.0, 141.0, 87.0, 23.0, "entry_1.png", 452.0, 153.0)
        self.nom_filiereF = self.add_entry(734.0, 302.0, 134.0, 19.0, "entry_2.png", 801.0, 312.5)
        self.id_filiereF = self.add_entry(734.0, 267.0, 134.0, 19.0, "entry_3.png", 801.0, 277.5)

            # Adding buttons
        self.rechercher = self.add_button(795.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")  # rechercher
        self.ajouter = self.add_button(793.0, 379.0, 87.0, 22.0, "button_2.png", self.addFiliere)  # ajouter
        self.modifier = self.add_button(597.0, 379.0, 87.0, 22.0, "button_3.png", self.updateFiliere)  # modifier
        self.supprimer = self.add_button(695.0, 379.0, 87.0, 22.0, "button_4.png", self.deleteFiliere)  # supprimer
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png",self.open_menu )  # menu
        self.id = self.add_button(17.0, 141.0, 94.0, 24.0, "button_6.png", "button_6 clicked")  # id

    def add_image (self, file_name, x, y):
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
        self.loadFilieres()

    def loadFilieres(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        filieres = self.controller.getAllFilieres()
        for filiere in filieres:
            self.tree.insert("", "end", values=filiere)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addFiliere(self):
        print("Ajouter un niveau")
        # Code pour ajouter un étudiant, par exemple :
        filiere = filiereC(None, self.nom_filiereF.get())

        self.controller.addFiliere(filiere)
        self.loadFilieres()
        self.clearForm()

    def updateFiliere(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun niveau sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_filiere = values[0]

            filiere = filiereC(
                id_filiere = int(id_filiere),
                nom_filiere = self.nom_filiereF.get()
            )

            self.controller.updateFiliere(filiere)
            self.loadFilieres()
            self.clearForm()
            messagebox.showinfo("Succès", "niveau modifié avec succès.")
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteFiliere(self):
        print("delete niveau")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_filiere = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteFiliere(id_filiere)
            self.loadFilieres()
            self.clearForm()



        else:
            print("No filiere selected")
            messagebox.showinfo("Error", "No filiere selected")

    def fillForm(self, filiere):
        self.clearForm()
        self.nom_filiereF.insert(0, filiere.nom_filiere)

    def clearForm(self):
        widgets = [self.nom_filiereF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_filiereF = None


    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.window, columns=(
            "id_filiere", "nom_filiere"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_filiere", text="ID Filiere")
        self.tree.heading("nom_filiere", text="Filiere")


        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_filiere", width=300, anchor="center")
        self.tree.column("nom_filiere", width=300, anchor="center")



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
            self.canvas.create_window(285.0, 328.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            filiere_data = item_data["values"]
            id_filiere = filiere_data[0]
            filiere = self.controller.getFiliereById(id_filiere)
            print("niveau sélectionné :", filiere_data)
            self.fillForm(filiere)


    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()





