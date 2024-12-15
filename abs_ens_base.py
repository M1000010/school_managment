from tkinter import messagebox

from abs_ens import abs_ensC


class abs_ensController:
    def __init__(self, connection):
        self.connection = connection

    def addAbs_ens(self, abs_ens):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO abs_ens VALUES (%s, %s, %s, %s, %s)", abs_ens.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getAbs_ensById(self, abs_ens_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_abs_ens, date_abs_ens, periode_abs_ens, motif_ens, id_ens
                 FROM abs_ens WHERE id_abs_ens = %s""")
        cursor.execute(query, (abs_ens_id,))
        result = cursor.fetchone()
        cursor.close()
        return abs_ensC(*result)


    def getAllabs_enss(self):
        cursor = self.connection.cursor()
        query = """SELECT id_abs_ens, date_abs_ens, periode_abs_ens, motif_ens, id_ens
                 FROM abs_ens"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateAbs_ens(self, abs_ens):
        cursor = self.connection.cursor()
        query = """
        UPDATE abs_ens
        SET date_abs_ens = %s, periode_abs_ens = %s, motif_ens = %s, id_ens = %s
        
        WHERE id_abs_ens = %s
        """
        print(abs_ens)
        cursor.execute(query, (abs_ens.date_abs_ens, abs_ens.periode_abs_ens, abs_ens.motif_ens,
                               abs_ens.id_ens, abs_ens.id_abs_ens))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteAbs_ens(self, id_abs_ens):
        cursor = self.connection.cursor()
        query = "DELETE FROM abs_ens WHERE id_abs_ens = %s"
        cursor.execute(query, (id_abs_ens,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

