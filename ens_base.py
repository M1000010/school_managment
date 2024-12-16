from tkinter import messagebox, filedialog

import mysql.connector
from fpdf import FPDF

from ens import ensC


class ensController:
    def __init__(self, connection):
        self.connection = connection

    def addEns(self, ens):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO enseignant VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", ens.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getEnsById(self, id_ens):
        cursor = self.connection.cursor()
        query = ("""SELECT id_ens, cin_ens, nom_ens, prenom_ens, date_n_ens, num_ens,
                 mail_ens, id_specialite, id_module FROM enseignant WHERE id_ens = %s""")
        cursor.execute(query, (id_ens,))
        result = cursor.fetchone()
        cursor.close()
        return ensC(*result)


    def getAllEnss(self):
        cursor = self.connection.cursor()
        query = """SELECT id_ens, cin_ens, nom_ens, prenom_ens, date_n_ens, num_ens, mail_ens, id_specialite, id_module
                 FROM enseignant"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateEns(self, ens):
        cursor = self.connection.cursor()
        query = """
        UPDATE enseignant
        SET cin_ens = %s, nom_ens = %s, prenom_ens = %s, date_n_ens = %s,
        num_ens = %s, mail_ens = %s, id_specialite = %s, id_module = %s
        WHERE id_ens = %s
        """
        cursor.execute(query, (ens.cin_ens, ens.nom_ens,
                               ens.prenom_ens, ens.date_n_ens,
                               ens.num_ens, ens.mail_ens,
                               ens.id_specialite, ens.id_module, ens.id_ens))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteEns(self, id_ens):
        cursor = self.connection.cursor()
        query = "DELETE FROM enseignant WHERE id_ens = %s"
        cursor.execute(query, (id_ens,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been deleted successfully.")

    def exporter_pdf(self):
        """Exporte les données des enseignants dans un fichier PDF."""
        cursor = self.connection.cursor()
        try:
            # Exécuter la requête pour récupérer les données des enseignants
            query = """SELECT id_ens, cin_ens, nom_ens, prenom_ens, date_n_ens, num_ens, mail_ens, id_specialite, id_module FROM enseignant"""
            cursor.execute(query)
            results = cursor.fetchall()
            headers = [i[0] for i in cursor.description]

            # Vérifier si des données ont été récupérées
            if not results:
                messagebox.showinfo("Information", "Aucun enseignant trouvé pour l'exportation.")
                return

            # Créer un fichier PDF
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Ajouter un titre
            pdf.set_font("Arial", style="B", size=16)
            pdf.cell(200, 10, txt="Liste des Enseignants", ln=True, align="C")

            # Ajouter les en-têtes de colonnes
            pdf.set_font("Arial", style="B", size=12)
            for header in headers:
                pdf.cell(40, 10, txt=str(header), border=1)
            pdf.ln()

            # Ajouter les données des enseignants
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
                messagebox.showinfo("Succès", "Les données des enseignants ont été exportées avec succès dans le fichier PDF.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la requête : {err}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
        finally:
            cursor.close()

