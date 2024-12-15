from tkinter import messagebox

from paiement import paiementC


class paiementController:
    def __init__(self, connection):
        self.connection = connection

    def addPaiement(self, paiement):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO paiement VALUES (%s, %s, %s, %s, %s)", paiement.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getPaiementById(self, id_paiement):
        cursor = self.connection.cursor()
        query = ("""SELECT id_paiement, montant, date_paiement, statut, id_etd FROM paiement WHERE id_paiement = %s""")
        cursor.execute(query, (id_paiement,))
        result = cursor.fetchone()
        cursor.close()
        return paiementC(*result)


    def getAllPaiements(self):
        cursor = self.connection.cursor()
        query = """SELECT id_paiement, montant, date_paiement, statut, id_etd  FROM paiement"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updatePaiement(self, paiement):
        cursor = self.connection.cursor()
        query = """
        UPDATE paiement
        SET montant = %s, date_paiement = %s, statut = %s, id_etd = %s WHERE id_paiement = %s"""
        cursor.execute(query, (paiement.montant, paiement.date_paiement, paiement.statut,
                               paiement.id_etd, paiement.id_paiement))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deletePaiement(self, id_paiement):
        cursor = self.connection.cursor()
        query = "DELETE FROM paiement WHERE id_paiement = %s"
        cursor.execute(query, (id_paiement,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

