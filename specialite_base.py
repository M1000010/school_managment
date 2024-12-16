from tkinter import messagebox

from filiere import filiereC
from niveau import niveauC
from specialite import specialiteC


class specialiteController:
    def __init__(self, connection):
        self.connection = connection

    def addSpecialite(self, specialite):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO specialite VALUES (%s, %s)", specialite.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getSpecialiteById(self, id_specialite):
        cursor = self.connection.cursor()
        query = ("""SELECT id_specialite, nom_specialite FROM specialite WHERE id_specialite = %s""")
        cursor.execute(query, (id_specialite,))
        result = cursor.fetchone()
        cursor.close()
        return specialiteC(*result)


    def getAllSpecialites(self):
        cursor = self.connection.cursor()
        query = """SELECT id_specialite, nom_specialite FROM specialite"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateSpecialite(self, specialite):
        cursor = self.connection.cursor()
        query = """UPDATE specialite SET nom_specialite = %s WHERE id_specialite = %s"""
        cursor.execute(query, (specialite.nom_specialite, specialite.id_specialite))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteSpecialite(self, id_specialite):
        cursor = self.connection.cursor()
        query = "DELETE FROM specialite WHERE id_specialite = %s"
        cursor.execute(query, (id_specialite,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been deleted successfully.")

