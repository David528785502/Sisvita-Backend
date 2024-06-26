from database.db import get_connection
from .entities.Especialista import Especialista
from .entities.Login import Login
from .LoginModel import LoginModel

class EspecialistaModel():

    @classmethod
    def get_especialistas(self):
        try:
            connection = get_connection()
            especialistas = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_especialista, nombre_perfil, correo, contrasenna, dni, nombres, apellidos, numero_colegiatura FROM public."especialista" """)
                resultset = cursor.fetchall()

                for row in resultset:
                    especialista = Especialista(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    especialistas.append(especialista.to_JSON())

            connection.close()
            return especialistas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_especialista(self, id_especialista):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_especialista, nombre_perfil, correo, contrasenna, dni, nombres, apellidos, numero_colegiatura FROM public."especialista" WHERE id_especialista = %s""", (id_especialista,))
                row = cursor.fetchone()

                especialista = None
                if row != None:
                    especialista = Especialista(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    especialista = especialista.to_JSON()

            connection.close()
            return especialista
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_especialista(self, especialista):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."especialista" (nombre_perfil, correo, contrasenna, dni, nombres, apellidos, numero_colegiatura)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", (especialista.nombre_perfil, especialista.correo, especialista.contrasenna, especialista.dni, especialista.nombres, especialista.apellidos, especialista.numero_colegiatura))
                affected_rows = cursor.rowcount
                connection.commit()

                if affected_rows == 1:
                    login_entry = Login(None, especialista.correo, especialista.contrasenna, 2)
                    LoginModel.add_login(login_entry)

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_especialista_by_correo(cls, correo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_especialista, nombre_perfil, correo, contrasenna, dni, nombres, apellidos, numero_colegiatura 
                                FROM public."especialista" WHERE correo = %s""", (correo,))
                row = cursor.fetchone()

                especialista = None
                if row:
                    especialista = Especialista(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

            connection.close()
            return especialista

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_especialista(self, especialista):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public."especialista" SET nombre_perfil = %s, correo = %s, contrasenna = %s, dni = %s, nombres = %s, apellidos = %s, numero_colegiatura = %s  
                                WHERE id_especialista = %s""", (especialista.nombre_perfil, especialista.correo, especialista.contrasenna, especialista.dni, especialista.nombres, especialista.apellidos, especialista.numero_colegiatura, especialista.id_especialista))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_especialista(self, especialista):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."especialista" WHERE id_especialista = %s""", (especialista.id_especialista,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)