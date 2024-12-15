from tkinter import messagebox

from niveau import niveauC
from student import etudiant


class niveauController:
    def __init__(self, connection):
        self.connection = connection

    def addNiveau(self, niveau):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO niveau VALUES (%s, %s)", niveau.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getNiveauById(self, id_niveau):
        cursor = self.connection.cursor()
        query = ("""SELECT id_niveau, nom_niveau FROM niveau WHERE id_niveau = %s""")
        cursor.execute(query, (id_niveau,))
        result = cursor.fetchone()
        cursor.close()
        return niveauC(*result)


    def getAllNiveaux(self):
        cursor = self.connection.cursor()
        query = """SELECT id_niveau, nom_niveau FROM niveau"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateNiveau(self, niveau):
        cursor = self.connection.cursor()
        query = """UPDATE niveau SET nom_niveau = %s WHERE id_niveau = %s"""
        cursor.execute(query, (niveau.nom_niveau, niveau.id_niveau))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteNiveau(self, id_niveau):
        cursor = self.connection.cursor()
        query = "DELETE FROM niveau WHERE id_niveau = %s"
        cursor.execute(query, (id_niveau,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

