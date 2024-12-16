from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, messagebox, ttk
import Menu
from specialite import specialiteC


class specialiteUI:
    def __init__(self, window, controller):

        self.window = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\specialite")

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
        self.add_image("image_1.png", 505.0, 59.0)
        self.add_image("image_2.png", 738.0, 300.0)
        self.add_image("image_3.png", 299.0, 320.0)

        # Adding entries
        self.barre_rechercheF = self.add_entry(111.0, 141.0, 676.0, 22.0, "entry_1.png", 449.0, 153.0)
        self.nom_specialiteF = self.add_entry(731.0, 306.0, 134.0, 15.0, "entry_2.png", 798.0, 314.5)
        self.id_specialiteF = self.add_entry(731.0, 276.0, 134.0, 15.0, "entry_3.png", 798.0, 284.5)

        # Adding buttons
        self.rechercher = self.add_button(792.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.ajouter= self.add_button(792.0, 375.0, 87.0, 22.0, "button_2.png", self.addSpecialite)
        self.supprimer = self.add_button(694.0, 375.0, 87.0, 22.0, "button_3.png", self.deleteSpecialite)
        self.modifier = self.add_button(596.0, 375.0, 87.0, 22.0, "button_4.png", self.updateSpecialite)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id= self.add_button(14.0, 141.0, 98.0, 23.0, "button_6.png", "button_6 clicked")

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
        self.loadSpecialites()

    def loadSpecialites(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        specialites = self.controller.getAllSpecialites()
        for specialite in specialites:
            self.tree.insert("", "end", values=specialite)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addSpecialite(self):
        # Code pour ajouter un étudiant, par exemple :
        specialite = specialiteC(None, self.nom_specialiteF.get())

        self.controller.addSpecialite(specialite)
        self.loadSpecialites()
        self.clearForm()

    def updateSpecialite(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun specialite sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_specialite = values[0]

            specialite = specialiteC(
                id_specialite = int(id_specialite),
                nom_specialite = self.nom_specialiteF.get()
            )

            self.controller.updateSpecialite(specialite)
            self.loadSpecialites()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteSpecialite(self):
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_specialite = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteSpecialite(id_specialite)
            self.loadSpecialites()
            self.clearForm()


        else:
            messagebox.showinfo("Error", "No specialite selected")

    def fillForm(self, specialite):
        self.clearForm()
        self.nom_specialiteF.insert(0, specialite.nom_specialite)

    def clearForm(self):
        widgets = [self.nom_specialiteF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_specialiteF = None


    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.window, columns=(
            "id_specialite", "nom_specialite"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_specialite", text="ID Specialite")
        self.tree.heading("nom_specialite", text="Specialite")


        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_specialite", width=300, anchor="center")
        self.tree.column("nom_specialite", width=300, anchor="center")



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
            self.canvas.create_window(285.0, 326.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            specialite_data = item_data["values"]
            id_specialite = specialite_data[0]
            specialite = self.controller.getSpecialiteById(id_specialite)
            print("niveau sélectionné :", specialite_data)
            self.fillForm(specialite)


    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()














