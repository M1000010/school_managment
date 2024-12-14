from tkinter import messagebox

from filiere import filiereC
from niveau import niveauC


class filiereController:
    def __init__(self, connection):
        self.connection = connection

    def addFiliere(self, filiere):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO filiere VALUES (%s, %s)", filiere.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getFiliereById(self, id_filiere):
        cursor = self.connection.cursor()
        query = ("""SELECT id_niveau, nom_niveau FROM niveau WHERE id_niveau = %s""")
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
        query = """UPDATE niveau SET nom_niveau = %s WHERE id_etd = %s"""
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

