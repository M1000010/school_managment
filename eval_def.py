from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
from eval_base import *
from eval import *
import Menu
class evalUI :
    def __init__(self, window, controller):
        self.root = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\evaluation")

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
        # combobox.current(default_index)  # Définit la sélection par défaut
        return combobox

    def setup_ui(self):
        # Adding images

        self.add_image("image_1.png",  300.0, 327.0)
        self.add_image("image_2.png", 497.0, 59.0)
        self.add_image("image_3.png", 742.0, 302.0)
        # Adding buttons
        self.rechercher = self.add_button(795.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_2.png", self.open_menu)
        self.ajouter = self.add_button(797.0, 427.0, 87.0, 22.0, "button_3.png", self.addEval)
        self.modifier = self.add_button(601.0, 427.0, 87.0, 22.0, "button_4.png", self.updateEval)
        self.supprimer = self.add_button(699.0, 427.0, 87.0, 22.0, "button_5.png", self.deleteEval)
        self.id = self.add_button(17.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        # Adding entries

        self.barreRechercheF = self.add_entry(114.0, 141.0, 676.0, 22.0, "entry_1.png",  452.0, 153.0)
        self.heure_finF = self.add_entry(737.0, 337.0, 134.0, 14.0, "entry_2.png", 804.0, 345.0)
        self.heure_debutF = self.add_entry(737.0, 307.0, 134.0, 15.0, "entry_3.png",  804.0, 315.5)
        self.date_evaluationF = self.add_date_entry(737.0, 277.0, 134.0, 15.0, "entry_4.png", 804.0, 285.5)
        self.type_evaluationF = self.add_entry(737.0, 247.0, 134.0, 22.0, "entry_5.png", 804.0, 255.5)
        self.id_moduleF = self.add_entry(737.0, 370.0, 134.0, 15.0, "entry_6.png", 804.0, 378.5)
        self.id_evaluationF = self.add_entry(737.0, 217.0, 134.0, 15.0,"entry_7.png", 804.0, 225.5)


    def open_menu(self):
        self.root.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def displaydata(self):
        self.loadEvals()

    def loadEvals(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        evals = self.controller.getAllEvals()
        for eval in evals:
            self.tree.insert("", "end", values=eval)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addEval(self):
        print("Ajouter un evaluation")
        # Code pour ajouter une evaluation , par exemple :
        eval = evalC(None, self.date_evaluationF.get(), self.type_evaluationF.get(), self.heure_debutF.get(),
                           self.heure_finF.get(), self.id_moduleF.get())
        self.controller.addEval(eval)
        self.loadEvals()
        self.clearForm()


    def updateEval(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucune évaluation sélectionnée")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_eval = values[0]

            eval = evalC(
                id_eval=int(id_eval),
                date_eval=self.date_evaluationF.get(),
                type_eval=self.type_evaluationF.get(),
                h_debut_eval=self.heure_debutF.get(),
                h_fin_eval=self.heure_finF.get(),
                id_module=self.id_moduleF.get()
            )


            self.controller.updateEval(eval)
            self.loadEvals()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteEval(self):
        print("delete evaluation")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_eval = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteEval(id_eval)
            self.loadEvals()
            self.clearForm()



        else:
            print("No evaluation selected")
            messagebox.showinfo("Error", "No evaluation selected")

    def fillForm(self, eval):
        self.clearForm()
        self.date_evaluationF.insert(0, eval.date_eval)
        self.type_evaluationF.insert(0, eval.type_eval)
        self.heure_debutF.insert(0, eval.h_debut_eval)
        self.heure_finF.insert(0, eval.h_fin_eval)
        self.id_moduleF.insert(0, eval.id_module)

    def clearForm(self):
        widgets = [self.date_evaluationF, self.type_evaluationF, self.heure_debutF, self.heure_finF, self.id_moduleF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.id_evaluationF = None

    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_eval", "date_eval", "type_eval", "h_debut_eval", "h_fin_eval", "id_module"
        ), show="headings", height=14)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_eval", text="ID évaluation")
        self.tree.heading("date_eval", text="Date de l'évaluation")
        self.tree.heading("type_eval", text="Type de l'évaluation")
        self.tree.heading("h_debut_eval", text="Heure de début")
        self.tree.heading("h_fin_eval", text="Heure de fin")
        self.tree.heading("id_module", text="ID du module")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_eval", width=100, anchor="center")
        self.tree.column("date_eval", width=100, anchor="center")
        self.tree.column("type_eval", width=100, anchor="center")
        self.tree.column("h_debut_eval", width=100, anchor="center")
        self.tree.column("h_fin_eval", width=100, anchor="center")
        self.tree.column("id_module", width=100, anchor="center")



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
            self.canvas.create_window(292.0, 330.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            eval_data = item_data["values"]
            eval_id = eval_data[0]
            eval = self.controller.getEvalById(eval_id)
            print("Évaluation sélectionné :", eval_data)
            self.fillForm(eval)










