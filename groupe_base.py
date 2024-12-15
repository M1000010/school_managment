from tkinter import messagebox

from groupe import groupeC


class GroupController:
    def __init__(self, connection):
        self.connection = connection

    def addGroup(self, groupe):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO groupe VALUES (%s, %s, %s)", groupe.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getGroupeById(self, groupe_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_grp, nom_grp, id_niv FROM groupe WHERE id_grp = %s""")
        cursor.execute(query, (groupe_id,))
        result = cursor.fetchone()
        cursor.close()
        return groupeC(*result)


    def getAllGroups(self):
        cursor = self.connection.cursor()
        query = """SELECT id_grp, nom_grp, id_niv
                 FROM groupe"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateGroupe(self, groupe):
        cursor = self.connection.cursor()
        query = """
        UPDATE groupe
        SET nom_grp = %s, id_niv = %s
        WHERE id_grp = %s
        """
        print(groupe)
        cursor.execute(query, (groupe.nom_grp, groupe.id_niv, groupe.id_grp))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteGroupe(self, id_grp):
        cursor = self.connection.cursor()
        query = "DELETE FROM groupe WHERE id_grp = %s"
        cursor.execute(query, (id_grp,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

