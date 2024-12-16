from tkinter import messagebox

import bcrypt

from authentication import authentication

class authController:
    def __init__(self, connection):
        self.connection = connection

    def getAllauth(self):
        cursor = self.connection.cursor()
        query = """SELECT id_auth, username, password
                 FROM authentication"""
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def authenticate(self, username, password):
        try:
            cursor = self.connection.cursor()
            query = "SELECT password FROM user WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                stored_password = result[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
            cursor.close()

            return False
        except Exception as e:
            print(f"Erreur lors de l'authentification : {e}")
            return False




    def register(self, username, password):
        try:
            cursor = self.connection.cursor()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            query = "INSERT INTO authentication (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, hashed_password))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de l'enregistrement : {e}")
            return False
        finally:
            cursor.close()

