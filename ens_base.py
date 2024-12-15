from tkinter import messagebox

from ens import ensC


class ensController:
    def __init__(self, connection):
        self.connection = connection

    def addEns(self, ens):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO enseignant VALUES (%s, %s, %s, %s, %s, %s, %s, %s, s%)", ens.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getEnsById(self, id_ens):
        cursor = self.connection.cursor()
        query = ("""SELECT id_ens, cin_ens, nom_ens, prenom_ens, date_n_ens, num_ens,
                 mail_ens, id_specilite, id_module FROM enseignant WHERE id_ens = %s""")
        cursor.execute(query, (id_ens,))
        result = cursor.fetchone()
        cursor.close()
        return ensC(*result)


    def getAllStudents(self):
        cursor = self.connection.cursor()
        query = """SELECT id_ens, cin_ens, nom_ens, prenom_ens, date_n_ens, num_ens, mail_ens, id_specialite, id_module
                 FROM enseignant"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateEns(self, ens):
        cursor = self.connection.cursor()
        query = """
        UPDATE enseignant
        SET cin_ens = %s, nom_ens = %s, prenom_ens = %s, date_n_ens = %s,
        num_ens = %s, mail_ens = %s, id_specialite = %s, id_module = %s
        WHERE id_ens = %s
        """
        cursor.execute(query, (ens.cin_ens, ens.nom_ens,
                               ens.prenom_ens, ens.date_n_ens,
                               ens.num_ens, ens.mail_ens,
                               ens.id_specialite, ens.id_module, ens.id_ens))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteStudent(self, id_ens):
        cursor = self.connection.cursor()
        query = "DELETE FROM enseignant WHERE id_ens = %s"
        cursor.execute(query, (id_ens,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been deleted successfully.")

