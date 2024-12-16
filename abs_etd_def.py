from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, ttk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from abs_etd_base import *
from abs_etd import *
import Menu
class abs_etdUI :
    def __init__(self, window, controller):
        self.root = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\abs_etd")

        self.root.geometry("900x500")
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
        self.add_image("image_1.png", 302.0, 329.0)
        self.add_image("image_2.png", 749.0, 311.0)
        self.add_image("image_3.png", 505.0, 59.0)

        # Adding buttons
        self.rechercher = self.add_button(791.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.ajouter = self.add_button(801.0, 444.0, 87.0, 22.0, "button_2.png", self.addAbs_etd)
        self.modifier = self.add_button(605.0, 444.0, 87.0, 22.0, "button_3.png", self.updateAbs_etd)
        self.supprimer = self.add_button(703.0, 444.0, 87.0, 22.0, "button_4.png", self.deleteAbs_etd)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_5.png", self.open_menu)
        self.id = self.add_button(13.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        self.choices = ["Matin", "Apres Midi"]

        # Adding entries

        self.barreRechercheF = self.add_entry(110.0, 141.0, 676.0, 22.0, "entry_1.png", 448.0, 153.0)
        self.id_seanceF = self.add_entry(739.0, 355.0, 134.0, 16.0, "entry_2.png", 806.0, 364.0)
        self.motifF = self.add_entry(739.0, 320.0, 134.0, 17.0, "entry_3.png", 806.0, 329.5)
        self.periode_absF = self.add_combobox(739.0, 286.0, 134.0, 18.0, "entry_4.png", 806.0, 296.0,self.choices)
        self.date_absF = self.add_date_entry(739.0, 252.0, 134.0, 17.0, "entry_5.png", 806.0, 261.5)
        self.id_etdF = self.add_entry(739.0, 393.0, 134.0, 16.0, "entry_6.png", 806.0, 402.0)
        self.id_abs_etdF = self.add_entry(739.0, 218.0, 134.0, 17.0, "entry_7.png", 806.0, 227.5)

        # self.root.resizable(False, False)
        self.Table()
        self.loadAbs_etds()
    def open_menu(self):
        self.root.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def displaydata(self):
        self.loadAbs_etds()

    def loadAbs_etds(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        abs_etds = self.controller.getAllAbs_etds()
        for abs_etd in abs_etds:
            self.tree.insert("", "end", values=abs_etd)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addAbs_etd(self):
        print("Ajouter un absence")
        # Code pour ajouter un étudiant, par exemple :
        abs_etd = abs_etdC(None, self.date_absF.get(), self.periode_absF.get(), self.motifF.get(), self.id_seanceF.get(),
                           self.id_etdF.get())
        self.controller.addAbs_etd(abs_etd)
        self.loadAbs_etds()
        self.clearForm()


    def updateAbs_etd(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun absence sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_abs_etd = values[0]

            abs_etd = abs_etdC(
                id_abs_etd=int(id_abs_etd),
                date_abs_etd=self.date_absF.get(),
                periode_abs_etd=self.periode_absF.get(),
                motif_etd=self.motifF.get(),
                id_seance=self.id_seanceF.get(),
                id_etd=self.id_etdF.get(),

            )

            self.controller.updateAbs_etd(abs_etd)
            self.loadAbs_etds()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteAbs_etd(self):
        print("delete abcencet")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_abs_etd = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteAbs_etd(id_abs_etd)
            self.loadAbs_etds()
            self.clearForm()



        else:
            print("No absence selected")
            messagebox.showinfo("Error", "No absence selected")

    def fillForm(self, abs_etd):
        self.clearForm()
        self.date_absF.insert(0, abs_etd.date_abs_etd)
        self.periode_absF.insert(0, abs_etd.periode_abs_etd)
        self.motifF.insert(0, abs_etd.motif_etd)
        self.id_seanceF.insert(0, abs_etd.id_seance)
        self.id_etdF.insert(0, abs_etd.id_etd)


    def clearForm(self):
        widgets = [self.date_absF, self.periode_absF, self.motifF, self.id_seanceF, self.id_etdF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_abs_etdFF = None


    def Table(self):
        """
        Initialise le tableau des absences avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_abs_etd", "date_abs_etd", "periode_abs_etd", "motif_etd", "id_seance", "id_etd"
        ), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_abs_etd", text="ID de l'absence")
        self.tree.heading("date_abs_etd", text="Date de l'absence")
        self.tree.heading("periode_abs_etd", text="Période de l'absence")
        self.tree.heading("motif_etd", text="Motif")
        self.tree.heading("id_seance", text="ID de la séance ")
        self.tree.heading("id_etd", text="ID de l'étudiant")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_abs_etd", width=100, anchor="center")
        self.tree.column("date_abs_etd", width=100, anchor="center")
        self.tree.column("periode_abs_etd", width=100, anchor="center")
        self.tree.column("motif_etd", width=100, anchor="center")
        self.tree.column("id_seance", width=100, anchor="center")
        self.tree.column("id_etd", width=100, anchor="center")



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
            abs_etd_data = item_data["values"]
            abs_etd_id = abs_etd_data[0]
            abs_etd = self.controller.getAbs_etdById(abs_etd_id)
            print("Absence sélectionné :", abs_etd_data)
            self.fillForm(abs_etd)



























