
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox, END, filedialog
from tkinter.ttk import Combobox

from fpdf import FPDF
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry

import Menu
from paiement import paiementC


class paiementUI :
    def __init__(self, window, controller):
        self.controller = controller
        self.window = window

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\paiement")

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
        self.add_image("image_1.png", 297.0, 327.0)
        self.add_image("image_2.png", 498.0, 59.0)
        self.add_image("image_3.png", 736.0, 308.0)

        self.statutCH = ["En attente", "Effectué", "Partiel"]

        # Adding entries
        self.barre_rechercheF = self.add_entry(110.0, 141.0, 676.0, 22.0, "entry_1.png", 448.0, 153.0)
        self.id_etdF = self.add_entry(731.0, 362.0, 134.0, 15.0, "entry_2.png", 798.0, 370.5)
        self.statutF = self.add_combobox(728.0, 332.0, 136.0, 18.0, "entry_3.png", 798.0,  340.5, self.statutCH)
        self.date_paiementF = self.add_date_entry(728.0, 302.0, 136.0, 18.0, "entry_4.png", 798.0, 310.5)
        self.montantF = self.add_entry(731.0, 272.0, 134.0, 15.0, "entry_5.png", 798.0, 280.5)
        self.id_paiementF = self.add_entry(731.0, 242.0, 134.0, 15.0, "entry_6.png", 798.0, 250.5)


        # Adding buttons
        self.rechercher = self.add_button(791.0, 141.0, 87.0, 23.0, "button_1.png", "button_1 clicked")
        self.id = self.add_button(13.0, 141.0, 94.0, 23.0, "button_2.png", "button_2 clicked")
        self.ajouter = self.add_button(796.0, 433.0, 87.0, 22.0, "button_3.png", self.addPaiement)
        self.modifier = self.add_button(600.0, 433.0, 87.0, 22.0, "button_4.png", self.updatePaiement)
        self.supprimer = self.add_button(698.0, 433.0, 87.0, 22.0, "button_5.png", self.deletePaiement)
        self.menu = self.add_button(13.0, 12.0, 80.0, 25.02392578125, "button_6.png", self.open_menu)
        self.pdf = self.add_button(137.0, 12.0, 116.0, 25.0, "btn_pdf.png", self.export_pdf)
        self.pai = self.add_button(280.0, 12.0, 112.0, 25.0, "btn_statistique.png", self.showStatistiquesPaiementGraph)

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

    def open_menu(self):
        self.window.destroy()
        menu_window = Menu.Menu()
        menu_window.window.mainloop()
    def displaydata(self):
        self.loadPaiements()

    def loadPaiements(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        paiements = self.controller.getAllPaiements()
        for paiement in paiements:
            self.tree.insert("", "end", values=paiement)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addPaiement(self):
        print("Ajouter un paiement")
        # Code pour ajouter un étudiant, par exemple :
        paiement = paiementC(None, self.montantF.get(), self.date_paiementF.get(),
                             self.statutF.get(), self.id_etdF.get())
        self.controller.addPaiement(paiement)
        self.loadPaiements()
        self.clearForm()


    def updatePaiement(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucun Paiement sélectionné")
            return

        try:
            values = self.tree.item(selected_item, 'values')
            id_paiement = values[0]

            paiement = paiementC(
                id_paiement=int(id_paiement),
                montant=self.montantF.get(),
                date_paiement=self.date_paiementF.get(),
                statut=self.statutF.get(),
                id_etd=self.id_etdF.get()
            )

            self.controller.updatePaiement(paiement)
            self.loadPaiements()
            self.clearForm()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur de saisie : {str(e)}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def deletePaiement(self):
        print("delete student")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_paiement = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deletePaiement(id_paiement)
            self.loadPaiements()
            self.clearForm()



        else:
            messagebox.showinfo("Error", "No Paiement selected")

    def fillForm(self, paiement):
        self.clearForm()
        self.montantF.insert(0, paiement.montant)
        self.date_paiementF.insert(0, paiement.date_paiement)
        self.statutF.insert(0, paiement.statut)
        self.id_etdF.insert(0, paiement.id_etd)


    def clearForm(self):
        widgets = [self.montantF, self.date_paiementF, self.statutF, self.id_etdF]

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
            "id_paiement", "montant", "date_paiement", "statut", "id_etd"), show="headings", height=13)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_paiement", text="ID Paiement")
        self.tree.heading("montant", text="Montant")
        self.tree.heading("date_paiement", text="Date De Paiement")
        self.tree.heading("statut", text="Statut")
        self.tree.heading("id_etd", text="ID Etudiant")



        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_paiement", width=110, anchor="center")
        self.tree.column("montant", width=120, anchor="center")
        self.tree.column("date_paiement", width=140, anchor="center")
        self.tree.column("statut", width=120, anchor="center")
        self.tree.column("id_etd", width=110, anchor="center")



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
            paiement_data = item_data["values"]
            id_paiement = paiement_data[0]
            paiement = self.controller.getPaiementById(id_paiement)
            print("paiement sélectionné :", paiement_data)
            self.fillForm(paiement)

    def export_pdf(self):
        """
        Exporte les données d'une ligne sélectionnée dans le tableau sous forme de reçu au format PDF.
        """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Erreur", "Aucune ligne sélectionnée dans le tableau.")
            return

        try:
            # Récupérer les données de la ligne sélectionnée
            values = self.tree.item(selected_item[0], 'values')
            if not values:
                messagebox.showinfo("Erreur", "Impossible de récupérer les données sélectionnées.")
                return

            # Créer un fichier PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Ajouter le titre
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(200, 10, txt="Reçu de Paiement", ln=True, align="C")
            pdf.ln(10)

            # Ajouter les informations du paiement
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"ID Paiement : {values[0]}", ln=True)
            pdf.cell(200, 10, txt=f"Montant : {values[1]} DH", ln=True)
            pdf.cell(200, 10, txt=f"Date de Paiement : {values[2]}", ln=True)
            pdf.cell(200, 10, txt=f"Statut : {values[3]}", ln=True)
            pdf.cell(200, 10, txt=f"ID Étudiant : {values[4]}", ln=True)
            pdf.ln(10)

            # Ajouter un message de remerciement
            pdf.set_font("Arial", style="I", size=12)
            pdf.cell(200, 10, txt="Merci pour votre paiement.", ln=True)
            pdf.cell(200, 10, txt="Pour toute assistance, veuillez contacter le service administratif.", ln=True)

            # Sauvegarder le fichier PDF
            fichier = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                title="Enregistrer le reçu PDF"
            )
            if fichier:
                pdf.output(fichier)
                messagebox.showinfo("Succès", "Le reçu a été exporté avec succès en PDF.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'exportation : {str(e)}")


    def closeGraph(self):
        """
        Ferme le graphique et supprime les widgets associés.
        """
        if hasattr(self, "canvas_graph") and self.canvas_graph:
            self.canvas_graph.get_tk_widget().destroy()
            self.canvas_graph = None  # Supprimer la référence au graphe

        if hasattr(self, "btn_close_graph") and self.btn_close_graph:
            self.btn_close_graph.destroy()


    def showStatistiquesPaiementGraph(self):
        """
        Affiche un graphique circulaire des paiements divisés par statut avec un bouton pour fermer le graphe.
        """
        # Récupérer les statistiques depuis le contrôleur
        stats = self.controller.getStatistiquesPaiement()
        labels = ["Effectué", "En attente", "Partiel"]
        values = [stats["Effectué"], stats["En attente"], stats["Partiel"]]

        # Créer le graphique circulaire
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=["green", "orange", "red"])
        ax.set_title("Répartition des Paiements par Statut")

        # Intégrer le graphe dans l'interface Tkinter
        self.canvas_graph = FigureCanvasTkAgg(fig, master=self.window)
        self.canvas_graph.draw()
        graph_widget = self.canvas_graph.get_tk_widget()
        graph_widget.place(x=100, y=20)

        # Ajouter un bouton pour fermer le graphe
        self.btn_close_graph = Button(
            self.window, text="Fermer", command=self.closeGraph, bg="red", fg="white"
        )
        self.btn_close_graph.place(x=650, y=70)  # Positionnement du bouton




