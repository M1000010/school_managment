from tkinter import messagebox, filedialog

import mysql.connector
from fpdf import FPDF

from student import etudiant


class StudentController:
    def __init__(self, connection):
        self.connection = connection

    def addStudent(self, student):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", student.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getStudentById(self, student_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd,
                 mail_etd, filiere, id_niv FROM student WHERE id_etd = %s""")
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        cursor.close()
        return etudiant(*result)


    def getAllStudents(self):
        cursor = self.connection.cursor()
        query = """SELECT id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd, mail_etd, filiere, id_niv
                 FROM student"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateStudent(self, student):
        cursor = self.connection.cursor()
        query = """
        UPDATE student
        SET cin_etd = %s, cne_etd = %s, nom_etd = %s, prenom_etd = %s, date_n_etd = %s,
        num_etd = %s, mail_etd = %s, filiere = %s, id_niv = %s
        WHERE id_etd = %s
        """
        print(student)
        cursor.execute(query, (student.cin_etd, student.cne_etd, student.nom_etd,
                               student.prenom_etd, student.date_n_etd,
                               student.num_etd, student.mail_etd,
                               student.filiere, student.id_niv, student.id_etd))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteStudent(self, id_etd):
        cursor = self.connection.cursor()
        query = "DELETE FROM student WHERE id_etd = %s"
        cursor.execute(query, (id_etd,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

    def exporter_pdf(self):
        """Exporte les données des étudiants dans un fichier PDF."""
        cursor = self.connection.cursor()
        try:
            # Exécuter la requête pour récupérer les données
            query = """SELECT id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd, mail_etd, filiere, id_niv FROM student"""
            cursor.execute(query)
            results = cursor.fetchall()
            headers = [i[0] for i in cursor.description]

            # Vérifier si des données ont été récupérées
            if not results:
                messagebox.showinfo("Information", "Aucun étudiant trouvé pour l'exportation.")
                return

            # Créer un fichier PDF
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Ajouter un titre
            pdf.set_font("Arial", style="B", size=16)
            pdf.cell(200, 10, txt="Liste des Étudiants", ln=True, align="C")

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
                messagebox.showinfo("Succès", "Les données des étudiants ont été exportées avec succès dans le fichier PDF.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la requête : {err}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
        finally:
            cursor.close()