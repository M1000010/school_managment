from tkinter import messagebox

from filiere import filiereC
from niveau import niveauC


class specialiteController:
    def __init__(self, connection):
        self.connection = connection

    def addSpecialite(self, specialite):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO specialite VALUES (%s, %s)", specialite.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getFiliereById(self, id_filiere):
        cursor = self.connection.cursor()
        query = ("""SELECT id_filiere, nom_filiere FROM filiere WHERE id_filiere = %s""")
        cursor.execute(query, (id_filiere,))
        result = cursor.fetchone()
        cursor.close()
        return filiereC(*result)


    def getAllFilieres(self):
        cursor = self.connection.cursor()
        query = """SELECT id_filiere, nom_filiere FROM filiere"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateFiliere(self, filiere):
        cursor = self.connection.cursor()
        query = """UPDATE filiere SET nom_filiere = %s WHERE id_filiere = %s"""
        cursor.execute(query, (filiere.nom_filiere, filiere.id_filiere))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteFiliere(self, id_filiere):
        cursor = self.connection.cursor()
        query = "DELETE FROM filiere WHERE id_filiere = %s"
        cursor.execute(query, (id_filiere,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

