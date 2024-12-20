from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fpdf import FPDF

import Menu
from resultat_base import *
from resultat import *
class resultatUI :
    def __init__(self, window, controller):
        self.root= window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\resultat")


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
        self.add_image("image_1.png", 299.0, 335.0)
        self.add_image("image_2.png", 498.0, 59.0)
        self.add_image("image_3.png", 741.0, 309.0)

        # Adding entries

        self.barreRechercheF = self.add_entry(103.0, 141.0, 676.0, 22.0, "entry_1.png",  441.0, 153.0)
        self.id_etudiantF = self.add_entry(733.0, 358.0, 134.0, 18.0, "entry_2.png", 800.0, 368.0)
        self.mentionF = self.add_entry(733.0, 322.0, 134.0, 18.0, "entry_3.png", 800.0, 332.0)
        self.notesF = self.add_entry(733.0, 287.0, 134.0, 18.0, "entry_4.png", 800.0, 297.0)
        self.id_resultatF = self.add_entry(733.0, 251.0, 134.0, 18.0, "entry_5.png", 800.0, 261.0)

        # Adding buttons
        self.rechercher = self.add_button(784.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.id = self.add_button(5.0, 141.0, 94.0, 24.0, "button_2.png", "button_2 clicked")
        self.ajouter = self.add_button(798.0, 422.0, 87.0, 22.0, "button_3.png", self.addResultat)
        self.modifier = self.add_button(602.0, 422.0, 87.0, 22.0, "button_4.png", self.updateResultat)
        self.supprimer = self.add_button(700.0, 422.0, 87.0, 22.0, "button_5.png", self.deleteResultat)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_6.png", self.open_menu)
        self.pdf = self.add_button(137.0, 12.0, 116.0, 25.0, "btn_pdf.png", self.export_pdf)
        self.re = self.add_button(280.0, 12.0, 112.0, 25.0, "btn_statistique.png", self.showStatistiquesGraph)

        self.Table()
        self.loadResultats()

    def open_menu(self):
        self.root.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()

    def displaydata(self):
        self.loadResultats()

    def loadResultats(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        resultats = self.controller.getAllResultats()
        for resultat in resultats:
            self.tree.insert("", "end", values=resultat)

    # Fonction d'ajout d'un résultat (à personnaliser selon votre logique)
    def addResultat(self):
        print("Ajouter un résultat")
        # Code pour ajouter un résultat, par exemple :
        resultat = resultatC(None, self.notesF.get(), self.mentionF.get(), self.id_etudiantF.get())
        self.controller.addResultat(resultat)
        self.loadResultats()
        self.clearForm()


    def updateResultat(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun résultat sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_resultat = values[0]

            resultat = resultatC(
                id_resultat=int(id_resultat),
                notes=self.notesF.get(),
                mention=self.mentionF.get(),
                id_etd=self.id_etudiantF.get(),

            )

            self.controller.updateResultat(resultat)
            self.loadResultats()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deleteResultat(self):
        print("delete result")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_resultat = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteResultat(id_resultat)
            self.loadResultats()
            self.clearForm()



        else:
            print("No result selected")
            messagebox.showinfo("Error", "No result selected")

    def fillForm(self, resultat):
        self.clearForm()
        self.id_resultatF.insert(0, resultat.id_resultat)
        self.mentionF.insert(0, resultat.mention)
        self.notesF.insert(0, resultat.notes)
        self.id_etudiantF.insert(0, resultat.id_etd)


    def clearForm(self):
        widgets = [self.id_resultatF, self.notesF, self.mentionF, self.id_etudiantF]

        for widget in widgets:
            if widget and hasattr(widget, 'delete'):
                widget.delete(0, END)
            elif widget and hasattr(widget, 'set'):
                widget.set('')  # For DateEntry and Combobox widgets

        self.idF = None


    def Table(self):
        """
        Initialise le tableau des résultats avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_resultat", "notes", "mention", "id_etd"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_resultat", text="ID Résultat")
        self.tree.heading("notes", text="Notes")
        self.tree.heading("mention", text="Mention")
        self.tree.heading("id_etd", text="ID Etudiant")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_resultat", width=150, anchor="center")
        self.tree.column("notes", width=150, anchor="center")
        self.tree.column("mention", width=150, anchor="center")
        self.tree.column("id_etd", width=150, anchor="center")



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
            resultat_data = item_data["values"]
            resultat_id = resultat_data[0]
            resultat = self.controller.getResultatById(resultat_id)
            print("Étudiant sélectionné :", resultat_data)
            self.fillForm(resultat)


    def export_pdf(self):
        """
        Exporte les données d'une ligne sélectionnée dans le tableau sous forme de bulletin au format PDF.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucune ligne sélectionnée dans le tableau.")
            return

        try:
            # Récupérer les données de la ligne sélectionnée
            values = self.tree.item(selected_item[0], 'values')
            print(values)  # Affichage pour vérifier les valeurs

            # Vérification du nombre d'éléments
            if not values or len(values) < 4:
                messagebox.showerror("Erreur", "La ligne sélectionnée ne contient pas assez de données.")
                return

            # Création du fichier PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Ajouter le titre
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(200, 10, txt="Bulletin de Résultats", ln=True, align="C")
            pdf.ln(10)

            # Ajouter les informations
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"ID Résultat : {values[0]}", ln=True)
            pdf.cell(200, 10, txt=f"Notes : {values[1]}", ln=True)
            pdf.cell(200, 10, txt=f"Mention : {values[2]}", ln=True)
            pdf.cell(200, 10, txt=f"ID Étudiant : {values[3]}", ln=True)
            pdf.ln(10)

            # Message final
            pdf.set_font("Arial", style="I", size=12)
            pdf.cell(200, 10, txt="Félicitations pour votre résultat !", ln=True)
            pdf.cell(200, 10, txt="Pour toute assistance, contactez le service étudiant.", ln=True)

            # Dialogue de sauvegarde
            fichier = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("Fichiers PDF", "*.pdf")],
                title="Enregistrer le bulletin PDF"
            )
            if fichier:
                pdf.output(fichier)
                messagebox.showinfo("Succès", "Le bulletin a été exporté avec succès en PDF.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'exportation : {str(e)}")

    def showStatistiquesGraphs(self):
        # Appel à la méthode SQL pour obtenir les statistiques
        statistiques = self.controller.getStatistiquesNotes()
        plus_de_10 = statistiques["plus_de_10"]
        moins_de_10 = statistiques["moins_de_10"]

        # Créer le graphique avec matplotlib
        fig, ax = plt.subplots()
        categories = ["Notes >= 10", "Notes < 10"]
        valeurs = [plus_de_10, moins_de_10]

        # Créer un graphique en barres
        ax.bar(categories, valeurs, color=['green', 'red'])
        ax.set_title("Statistiques des Notes")
        ax.set_ylabel("Nombre d'Étudiants")
        ax.set_xlabel("Catégories")

        # Afficher le graphique dans Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=100, y=10)  # Positionnement du graphe



    def closeGraph(self):
        """
        Ferme le graphique affiché et supprime les widgets associés.
        """
        if hasattr(self, "graph_widget") and self.graph_widget:
            self.graph_widget.destroy()  # Supprimer le widget du graphe
            self.graph_widget = None

        if hasattr(self, "close_button") and self.close_button:
            self.close_button.destroy()  # Supprimer le bouton de fermeture
            self.close_button = None

        if hasattr(self, "canvas_graph") and self.canvas_graph:
            self.canvas_graph.get_tk_widget().destroy()  # Supprimer le canvas matplotlib
            self.canvas_graph = None



    def showStatistiquesGraph(self):
        # Appel à la méthode SQL pour obtenir les statistiques
        statistiques = self.controller.getStatistiquesNotes()
        plus_de_10 = statistiques["plus_de_10"]
        moins_de_10 = statistiques["moins_de_10"]

        # Créer le graphique avec matplotlib
        fig, ax = plt.subplots()
        categories = ["Notes >= 10", "Notes < 10"]
        valeurs = [plus_de_10, moins_de_10]

        # Créer un graphique en barres
        ax.bar(categories, valeurs, color=['green', 'red'])
        ax.set_title("Statistiques des Notes")
        ax.set_ylabel("Nombre d'Étudiants")
        ax.set_xlabel("Catégories")

        # Afficher le graphique dans Tkinter
        self.canvas_graph = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas_graph.draw()
        self.graph_widget = self.canvas_graph.get_tk_widget()
        self.graph_widget.place(x=100, y=10)  # Positionnement du graphe

        # Ajouter un bouton "Fermer" pour supprimer le graphique
        self.close_button = Button(
            self.root, text="Fermer", command=self.closeGraph, bg="red", fg="white"
        )
        self.close_button.place(x=680, y=50)  # Positionnement du bouton










