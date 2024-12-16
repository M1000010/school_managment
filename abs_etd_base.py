from tkinter import messagebox

from abs_etd import abs_etdC


class Abs_etdController:
    def __init__(self, connection):
        self.connection = connection

    def addAbs_etd(self, abs_etd):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO abs_etd VALUES (%s, %s, %s, %s, %s, %s)", abs_etd.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getAbs_etdById(self, abs_etd_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_abs_etd, date_abs_etd, periode_abs_etd, motif_etd, id_seance, id_etd
                  FROM abs_etd WHERE id_abs_etd = %s""")
        cursor.execute(query, (abs_etd_id,))
        result = cursor.fetchone()
        cursor.close()
        return abs_etdC(*result)


    def getAllAbs_etds(self):
        cursor = self.connection.cursor()
        query = """SELECT id_abs_etd, date_abs_etd, periode_abs_etd, motif_etd, id_seance, id_etd
                 FROM abs_etd"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateAbs_etd(self, abs_etd):
        cursor = self.connection.cursor()
        query = """
        UPDATE abs_etd
        SET date_abs_etd = %s, periode_abs_etd = %s, motif_etd = %s, id_seance = %s, id_etd = %s
        WHERE id_abs_etd = %s
        """
        print(abs_etd)
        cursor.execute(query, (abs_etd.date_abs_etd, abs_etd.periode_abs_etd, abs_etd.motif_etd,
                               abs_etd.id_seance, abs_etd.id_etd, abs_etd.id_abs_etd))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteAbs_etd(self, id_abs_etd):
        cursor = self.connection.cursor()
        query = "DELETE FROM abs_etd WHERE id_abs_etd = %s"
        cursor.execute(query, (id_abs_etd,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

