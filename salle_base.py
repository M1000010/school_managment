from tkinter import messagebox

from salle import salleC


class salleController:
    def __init__(self, connection):
        self.connection = connection

    def addSalle(self, salle):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO salle VALUES (%s, %s, %s, %s)", salle.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getSalleById(self, salle_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_salle, nom_salle, capacite, id_bloc FROM salle WHERE id_salle = %s""")
        cursor.execute(query, (salle_id,))
        result = cursor.fetchone()
        cursor.close()
        return salleC(*result)


    def getAllSalles(self):
        cursor = self.connection.cursor()
        query = """SELECT id_salle, nom_salle, capacite, id_bloc FROM salle"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateSalle(self, salle):
        cursor = self.connection.cursor()
        query = """
        UPDATE salle
        SET nom_salle = %s, capacite = %s, id_bloc = %sWHERE id_salle = %s"""
        cursor.execute(query, (salle.nom_salle, salle.capacite, salle.id_bloc, salle.id_salle))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteSalle(self, id_salle):
        cursor = self.connection.cursor()
        query = "DELETE FROM salle WHERE id_salle = %s"
        cursor.execute(query, (id_salle,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

