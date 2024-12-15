from tkinter import messagebox

from seance import seanceC


class seanceController:
    def __init__(self, connection):
        self.connection = connection

    def addSeance(self, seance):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO seance VALUES (%s, %s, %s, %s, %s, %s, %s)", seance.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getSeanceById(self, id_seance):
        cursor = self.connection.cursor()
        query = ("""SELECT id_seance, date_seance, h_debut_seance, h_fin_seance, type_seance,
         id_salle, id_ens FROM seance WHERE id_seance = %s""")
        cursor.execute(query, (id_seance,))
        result = cursor.fetchone()
        cursor.close()
        return seanceC(*result)


    def getAllSeances(self):
        cursor = self.connection.cursor()
        query = """SELECT id_seance, date_seance, h_debut_seance, h_fin_seance, type_seance, id_salle, id_ens
                 FROM seance"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateSeance(self, seance):
        cursor = self.connection.cursor()
        query = """
        UPDATE seance
        SET date_seance = %s, h_debut_seance = %s, h_fin_seance = %s,
         type_seance = %s, id_salle = %s, id_ens = %s
        WHERE id_seance = %s
        """
        cursor.execute(query, (seance.date_seance, seance.h_debut_seance, seance.h_fin_seance,
                               seance.type_seance, seance.id_salle, seance.id_ens, seance.id_seance))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteSeance(self, id_seance):
        cursor = self.connection.cursor()
        query = "DELETE FROM seance WHERE id_seance = %s"
        cursor.execute(query, (id_seance,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

