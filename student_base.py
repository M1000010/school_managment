from tkinter import messagebox

from student import etudiant


class StudentController:
    def __init__(self, connection):
        self.connection = connection

    def addStudent(self, student):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", student.getValues())
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been added successfully.")

    def getStudentById(self, student_id):
        cursor = self.connection.cursor()
        query = ("""SELECT id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd,
                 mail_etd, filiere, id_niv FROM student WHERE id_etd = %s""")
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        cursor.close()
        return etudiant(*result)


    def getAllStudents(self):
        cursor = self.connection.cursor()
        query = """SELECT id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd, mail_etd, filiere, id_niv
                 FROM student"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateStudent(self, student):
        cursor = self.connection.cursor()
        query = """
        UPDATE student
        SET cin_etd = %s, cne_etd = %s, nom_etd = %s, prenom_etd = %s, date_n_etd = %s,
        num_etd = %s, mail_etd = %s, filiere = %s, id_niv = %s
        WHERE id_etd = %s
        """
        print(student)
        cursor.execute(query, (student.cin_etd, student.cne_etd, student.nom_etd,
                               student.prenom_etd, student.date_n_etd,
                               student.num_etd, student.mail_etd,
                               student.filiere, student.id_niv, student.id_etd))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success", "Record has been updated successfully.")

    def deleteStudent(self, id_etd):
        cursor = self.connection.cursor()
        query = "DELETE FROM student WHERE id_etd = %s"
        cursor.execute(query, (id_etd,))
        self.connection.commit()
        cursor.close()
        messagebox.showinfo("Success","Record has been deleted successfully.")

