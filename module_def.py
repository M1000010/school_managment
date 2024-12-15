from locale import windows_locale
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, END, ttk
import Menu
from module_base import *
from module import *
class moduleUI :
    def __init__(self,root, controller):
        self.window = root
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\module")

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

        self.add_image("image_1.png", 299.0, 323.0)
        self.add_image("image_2.png", 738.0, 300.0)
        self.add_image("image_3.png", 497.0, 59.0)

        # Adding entries

        self.barreRechercheF = self.add_entry(110.0, 141.0, 676.0, 22.0, "entry_1.png", 448.0, 153.0)
        self.id_enseignF = self.add_entry(734.0, 363.0, 134.0, 17.0, "entry_2.png", 801.0, 372.5)
        self.id_niveauF = self.add_entry(734.0, 328.0, 134.0, 18.0, "entry_3.png", 801.0, 338.0)
        self.coefficientF = self.add_entry(734.0, 294.0, 134.0, 17.0, "entry_4.png", 801.0, 303.5)
        self.nom_moduleF = self.add_entry(734.0, 259.0, 134.0, 18.0, "entry_5.png", 801.0, 269.0)
        self.id_moduleF = self.add_entry(734.0, 225.0, 134.0, 17.0, "entry_6.png", 801.0, 234.5)

        # Adding buttons
        self.rechercher = self.add_button(791.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.id = self.add_button(13.0, 141.0, 94.0, 24.0, "button_2.png", "button_2 clicked")
        self.ajouter = self.add_button(798.0, 425.0, 87.0, 22.0, "button_3.png", self.addModule)
        self.modifier = self.add_button(602.0, 425.0, 87.0, 22.0, "button_4.png", self.updateModule)
        self.supprimer = self.add_button(700.0, 425.0, 87.0, 22.0, "button_5.png", self.deleteModule)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_6.png", self.open_menu)

        # self.root.resizable(False, False)
        self.Table()
        self.loadModules()

    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def displaydata(self):
        self.loadModules()

    def loadModules(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        modules = self.controller.getAllModules()
        for module in modules:
            self.tree.insert("", "end", values=module)

    # Fonction d'ajout d'un module (à personnaliser selon votre logique)
    def addModule(self):
        print("Ajouter un module")
        # Code pour ajouter un module, par exemple :
        module = moduleC(None, self.nom_moduleF.get(), self.coefficientF.get(), self.id_niveauF.get(), self.id_enseignF.get())
        self.controller.addModule(module)
        self.loadModules()
        self.clearForm()


    def updateModule(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun module sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_module = values[0]

            module = moduleC(
                id_module=int(id_module),
                nom_module=self.nom_moduleF.get(),
                coef=self.coefficientF.get(),
                id_niv=self.id_niveauF.get(),
                id_ens=self.id_enseignF.get(),

            )

            self.controller.updateModule(module)
            self.loadModules()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteModule(self):
        print("delete module")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_module = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteModule(id_module)
            self.loadModules()
            self.clearForm()



        else:
            print("No module selected")
            messagebox.showinfo("Error", "No module selected")

    def fillForm(self, module):
        self.clearForm()
        self.nom_moduleF.insert(0, module.nom_module)
        self.coefficientF.insert(0, module.coef)
        self.id_niveauF.insert(0, module.id_niv)
        self.id_enseignF.insert(0, module.id_ens)


    def clearForm(self):
        widgets = [self.nom_moduleF, self.coefficientF, self.id_niveauF, self.id_enseignF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_moduleF = None


    def Table(self):
        """
        Initialise le tableau des modules avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.window, columns=(
            "id_module", "nom_module", "coef", "id_niv", "id_ens"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_module", text="ID Module")
        self.tree.heading("nom_module", text="No de Module")
        self.tree.heading("coef", text="Coefficient")
        self.tree.heading("id_niv", text="Id Niveau")
        self.tree.heading("id_ens", text="Id Enseignant")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_module", width=120, anchor="center")
        self.tree.column("nom_module", width=120, anchor="center")
        self.tree.column("coef", width=120, anchor="center")
        self.tree.column("id_niv", width=120, anchor="center")
        self.tree.column("id_ens", width=120, anchor="center")



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
            module_data = item_data["values"]
            module_id = module_data[0]
            module = self.controller.getModuleById(module_id)
            print("Module sélectionné :", module_data)
            self.fillForm(module)













