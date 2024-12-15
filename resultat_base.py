from tkinter import messagebox

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

