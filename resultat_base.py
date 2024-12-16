from tkinter import messagebox, filedialog

import mysql.connector
from fpdf import FPDF

from resultat import resultatC


class ResultatController:
    def __init__(self, connection):
        self.connection = connection

    def addResultat(self, resultat):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO resultat VALUES (%s, %s, %s, %s)", resultat.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getResultatById(self, resultat_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_resultat, notes, mention, id_etd
                 FROM resultat WHERE id_resultat = %s""")
        cursor.execute(query, (resultat_id,))
        result = cursor.fetchone()
        cursor.close()
        return resultatC(*result)


    def getAllResultats(self):
        cursor = self.connection.cursor()
        query = """SELECT id_resultat, notes, mention, id_etd
                 FROM resultat"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateResultat(self, resultat):
        cursor = self.connection.cursor()
        query = """
        UPDATE resultat
        SET notes = %s, mention = %s, id_etd = %s
        WHERE id_resultat = %s
        """
        print(resultat)
        cursor.execute(query, (resultat.notes, resultat.mention, resultat.id_etd, resultat.id_resultat))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteResultat(self, id_resultat):
        cursor = self.connection.cursor()
        query = "DELETE FROM resultat WHERE id_resultat = %s"
        cursor.execute(query, (id_resultat,))
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

    def getStatistiquesNotes(self):
        """
        Récupère les statistiques des notes depuis la base de données.
        """
        try:
            cursor = self.connection.cursor()

            # Requête pour compter les notes >= 10
            cursor.execute("SELECT COUNT(*) FROM resultat WHERE notes >= 10")
            plus_de_10 = cursor.fetchone()[0]

            # Requête pour compter les notes < 10
            cursor.execute("SELECT COUNT(*) FROM resultat WHERE notes < 10")
            moins_de_10 = cursor.fetchone()[0]

            # Retourner les résultats sous forme de dictionnaire
            return {"plus_de_10": plus_de_10, "moins_de_10": moins_de_10}
        except Exception as e:
            print("Erreur SQL :", str(e))
            return {"plus_de_10": 0, "moins_de_10": 0}