from tkinter import messagebox

from bloc import blocC


class blocController:
    def __init__(self, connection):
        self.connection = connection

    def addBloc(self, bloc):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO bloc VALUES (%s, %s, %s)", bloc.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getBlocById(self, id_bloc):
        cursor = self.connection.cursor()
        query = ("""SELECT id_bloc, nom_bloc, nbr_salle FROM bloc WHERE id_bloc = %s""")
        cursor.execute(query, (id_bloc,))
        result = cursor.fetchone()
        cursor.close()
        return blocC(*result)


    def getAllBlocs(self):
        cursor = self.connection.cursor()
        query = """SELECT id_bloc, nom_bloc, nbr_salle FROM bloc"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateBloc(self, bloc):
        cursor = self.connection.cursor()
        query = """
        UPDATE bloc
        SET nom_bloc = %s, nbr_salle = %s WHERE id_bloc = %s"""
        cursor.execute(query, (bloc.nom_bloc, bloc.nbr_salle, bloc.id_bloc))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteBloc(self, id_Bloc):
        cursor = self.connection.cursor()
        query = "DELETE FROM bloc WHERE id_bloc = %s"
        cursor.execute(query, (id_Bloc,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

