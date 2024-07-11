from database.db import get_connection
from .entities.Login import Login

class LoginModel():

    @classmethod
    def get_login_by_correo(cls, correo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_login, correo, contrasenna, tipo 
                                FROM public."login" WHERE correo = %s""", (correo,))
                row = cursor.fetchone()

                login_entry = None
                if row:
                    login_entry = Login(row[0], row[1], row[2], row[3])

            connection.close()
            return login_entry

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_login(cls, login_entry):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."login" (correo, contrasenna, tipo)
                            VALUES (%s, %s, %s)""", (login_entry.correo, login_entry.contrasenna, login_entry.tipo))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_login_by_correo(self, correo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."login" WHERE correo = %s""", (correo,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)