from tkinter import messagebox

import mysql.connector
from fpdf import FPDF
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

from paiement import paiementC


class paiementController:
    def __init__(self, connection):
        self.connection = connection

    def addPaiement(self, paiement):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO paiement VALUES (%s, %s, %s, %s, %s)", paiement.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getPaiementById(self, id_paiement):
        cursor = self.connection.cursor()
        query = ("""SELECT id_paiement, montant, date_paiement, statut, id_etd FROM paiement WHERE id_paiement = %s""")
        cursor.execute(query, (id_paiement,))
        result = cursor.fetchone()
        cursor.close()
        return paiementC(*result)


    def getAllPaiements(self):
        cursor = self.connection.cursor()
        query = """SELECT id_paiement, montant, date_paiement, statut, id_etd  FROM paiement"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updatePaiement(self, paiement):
        cursor = self.connection.cursor()
        query = """
        UPDATE paiement
        SET montant = %s, date_paiement = %s, statut = %s, id_etd = %s WHERE id_paiement = %s"""
        cursor.execute(query, (paiement.montant, paiement.date_paiement, paiement.statut,
                               paiement.id_etd, paiement.id_paiement))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deletePaiement(self, id_paiement):
        cursor = self.connection.cursor()
        query = "DELETE FROM paiement WHERE id_paiement = %s"
        cursor.execute(query, (id_paiement,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

    def exporter_pdf(self):
        """Exporte les données de la base de données dans un fichier PDF."""
        cursor = self.connection.cursor()
        try:
            # Exécuter la requête pour récupérer les données
            query = """SELECT id_paiement, montant, date_paiement, statut, id_etd FROM paiement"""
            cursor.execute(query)
            results = cursor.fetchall()
            headers = [i[0] for i in cursor.description]

            # Vérifier si des données ont été récupérées
            if not results:
                messagebox.showinfo("Information", "Aucun paiement trouvé pour l'exportation.")
                return

            # Créer un fichier PDF
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Ajouter un titre
            pdf.set_font("Arial", style="B", size=16)
            pdf.cell(200, 10, txt="Liste des Paiements", ln=True, align="C")

            # Ajouter les en-têtes de colonnes
            pdf.set_font("Arial", style="B", size=12)
            for header in headers:
                pdf.cell(40, 10, txt=str(header), border=1)
            pdf.ln()

            # Ajouter les données
            pdf.set_font("Arial", size=12)
            for row in results:
                for value in row:
                    pdf.cell(40, 10, txt=str(value), border=1)
                pdf.ln()

            # Sauvegarder le fichier PDF
            fichier = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                title="Enregistrer le fichier PDF"
            )
            if fichier:
                pdf.output(fichier)
                messagebox.showinfo("Succès", "Les données ont été exportées avec succès dans le fichier PDF.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la requête : {err}")
        finally:
            cursor.close()
        messagebox.showinfo("Success","PDF created successfully.")
    def getStatistiquesPaiement(self):
        """
        Retourne le nombre de paiements pour chaque statut (Effectué, En attente, Partiel).
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT statut, COUNT(*) 
                FROM paiement 
                GROUP BY statut
            """)
            result = cursor.fetchall()

            # Transformer les résultats en dictionnaire
            stats = {"Effectué": 0, "En attente": 0, "Partiel": 0}
            for row in result:
                statut, count = row
                if statut in stats:
                    stats[statut] = count

            return stats
        except Exception as e:
            print(f"Erreur SQL : {e}")
            return {"Effectué": 0, "En attente": 0, "Partiel": 0}