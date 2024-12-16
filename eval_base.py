from tkinter import messagebox

from eval import evalC


class EvalController:
    def __init__(self, connection):
        self.connection = connection

    def addEval(self, eval):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO eval VALUES (%s, %s, %s, %s, %s, %s)", eval.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getEvalById(self, eval_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_eval, date_eval, type_eval, h_debut_eval, h_fin_eval, id_module
                  FROM eval WHERE id_eval = %s""")
        cursor.execute(query, (eval_id,))
        result = cursor.fetchone()
        cursor.close()
        return evalC(*result)


    def getAllEvals(self):
        cursor = self.connection.cursor()
        query = """SELECT id_eval, date_eval, type_eval, h_debut_eval, h_fin_eval, id_module
                 FROM eval"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateEval(self, eval):
        cursor = self.connection.cursor()
        query = """
        UPDATE eval
        SET date_eval = %s, type_eval = %s, h_debut_eval = %s, h_fin_eval = %s, id_module = %s
        WHERE id_eval = %s
        """
        print(eval)
        cursor.execute(query, (eval.date_eval, eval.type_eval, eval.h_debut_eval,
                               eval.h_fin_eval, eval.id_module, eval.id_eval))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteEval(self, id_eval):
        cursor = self.connection.cursor()
        query = "DELETE FROM eval WHERE id_eval = %s"
        cursor.execute(query, (id_eval,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

