from pathlib import Path
from tkinter.ttk import Combobox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, ttk
import Menu

from tkcalendar import DateEntry
from abs_ens_base import *
from abs_ens import *
class abs_ensUI :
    def __init__(self, window, controller):
        self.root = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\abs_ens")


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
        #combobox.current(default_index)  # Définit la sélection par défaut
        return combobox



    def setup_ui(self):
            # Adding images

            self.add_image("image_1.png", 299.0, 324.0)
            self.add_image("image_2.png", 505.0, 59.0)
            self.add_image("image_3.png", 738.0, 305.0)

            self.choices = ["Matinée", "Après-midi", "Journée entière"]

            # Adding buttons
            self.rechercher = self.add_button(795.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
            self.ajouter = self.add_button(798.0,430.0, 87.0, 22.0, "button_2.png", self.addAbs_ens)
            self.modifier = self.add_button(602.0, 430.0, 87.0, 22.0, "button_3.png", self.updateAbs_ens)
            self.supprimer = self.add_button(700.0, 430.0, 87.0, 22.0, "button_4.png", self.deleteAbs_ens)
            self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
            self.id = self.add_button(17.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

            # Adding entries

            self.barreRechercheF = self.add_entry(114.0, 141.0, 676.0, 22.0, "entry_1.png", 452.0, 153.0)
            self.id_enseignF = self.add_entry(738.0, 366.0, 134.0, 17.0, "entry_2.png", 805.0, 375.5)
            self.motifF = self.add_entry(738.0, 334.0, 134.0, 16.0, "entry_3.png", 805.0, 343.0)
            self.periode_absenceF = self.add_combobox(736.0, 301.0, 134.0, 19.0, "entry_4.png", 805.0, 310.0,self.choices)
            self.date_absenceF = self.add_date_entry(736.0, 268.0, 134.0, 19.0, "entry_5.png", 805.0, 277.0)
            self.id_absenceF = self.add_entry(738.0, 235.0, 134.0, 17.0, "entry_6.png", 805.0, 244.5)

            self.Table()
            self.loadAbs_enss()

    def open_menu(self):
        self.root.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def displaydata(self):
        self.loadAbs_enss()

    def loadAbs_enss(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        abs_enss = self.controller.getAllabs_enss()
        for abs_ens in abs_enss:
            self.tree.insert("", "end", values=abs_ens)

    # Fonction d'ajout d'un absence (à personnaliser selon votre logique)
    def addAbs_ens(self):
        print("Ajouter un absence")
        # Code pour ajouter un absence, par exemple :
        abs_ens = abs_ensC(None, self.date_absenceF.get(), self.periode_absenceF.get(),
                           self.motifF.get(), self.id_enseignF.get())
        self.controller.addAbs_ens(abs_ens)
        self.loadAbs_enss()
        self.clearForm()


    def updateAbs_ens(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun absence sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_abs_ens = values[0]

            abs_ens = abs_ensC(
                id_abs_ens=int(id_abs_ens),
                date_abs_ens=self.date_absenceF.get(),
                periode_abs_ens=self.periode_absenceF.get(),
                motif_ens=self.motifF.get(),
                id_ens=self.id_absenceF.get(),

            )

            self.controller.updateAbs_ens(abs_ens)
            self.loadAbs_enss()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteAbs_ens(self):
        print("delete absence")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_abs_ens = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteAbs_ens(id_abs_ens)
            self.loadAbs_enss()
            self.clearForm()



        else:
            print("No absence selected")
            messagebox.showinfo("Error", "No absence selected")

    def fillForm(self, abs_ens):
        self.clearForm()
        self.date_absenceF.insert(0,abs_ens.date_abs_ens)
        self.periode_absenceF.insert(0, abs_ens.periode_abs_ens)
        self.motifF.insert(0, abs_ens.motif_ens)
        self.id_enseignF.insert(0, abs_ens.id_ens)


    def clearForm(self):
        widgets = [self.date_absenceF, self.periode_absenceF, self.motifF, self.id_enseignF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_abs_ensF = None


    def Table(self):
        """
        Initialise le tableau des absences avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_abs_ens", "date_abs_ens", "periode_abs_ens", "motif_ens", "id_ens"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_abs_ens", text="ID Absence")
        self.tree.heading("date_abs_ens", text="Date d'absence")
        self.tree.heading("periode_abs_ens", text="Période de l'absence")
        self.tree.heading("motif_ens", text="Motif")
        self.tree.heading("id_ens", text="Id Enseignant")


        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_abs_ens", width=120, anchor="center")
        self.tree.column("date_abs_ens", width=120, anchor="center")
        self.tree.column("periode_abs_ens", width=120, anchor="center")
        self.tree.column("motif_ens", width=120, anchor="center")
        self.tree.column("id_ens", width=120, anchor="center")



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
            self.canvas.create_window(285.0, 330.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            abs_ens_data = item_data["values"]
            abs_ens_id = abs_ens_data[0]
            abs_ens = self.controller.getAbs_ensById(abs_ens_id)
            print("Absence sélectionné :", abs_ens_data)
            self.fillForm(abs_ens)





