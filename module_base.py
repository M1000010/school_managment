from tkinter import messagebox

from module import moduleC


class ModuleController:
    def __init__(self, connection):
        self.connection = connection

    def addModule(self, module):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO module VALUES (%s, %s, %s, %s, %s)", module.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getModuleById(self, module_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_module, nom_module, coef, id_niv, id_ens
                    FROM module WHERE id_module = %s""")
        cursor.execute(query, (module_id,))
        result = cursor.fetchone()
        cursor.close()
        return moduleC(*result)


    def getAllModules(self):
        cursor = self.connection.cursor()
        query = """SELECT id_module, nom_module, coef, id_niv, id_ens
                 FROM module"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateModule(self, module):
        cursor = self.connection.cursor()
        query = """
        UPDATE module
        SET nom_module = %s, coef = %s, id_niv = %s, id_ens = %s
        WHERE id_module = %s
        """
        print(module)
        cursor.execute(query, (module.nom_module, module.coef, module.id_niv,
                               module.id_ens, module.id_module))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteModule(self, id_module):
        cursor = self.connection.cursor()
        query = "DELETE FROM module WHERE id_module = %s"
        cursor.execute(query, (id_module,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

