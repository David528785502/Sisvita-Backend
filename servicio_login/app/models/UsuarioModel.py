from database.db import get_connection
from .entities.Usuario import Usuario
from .entities.Login import Login
from .LoginModel import LoginModel

class UsuarioModel():

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_usuario, nombre_perfil, contrasenna, correo, numero, fecha_nacimiento, ubigeo FROM public."usuario" """)
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_usuario(self, id_usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_usuario, nombre_perfil, contrasenna, correo, numero, fecha_nacimiento, ubigeo FROM public."usuario" WHERE id_usuario = %s""", (id_usuario,))
                row = cursor.fetchone()

                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    usuario = usuario.to_JSON()

            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_usuario_by_correo(cls, correo):
        try:
            connection = get_connection()
            usuario = None

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_usuario, nombre_perfil, contrasenna, correo, numero, fecha_nacimiento, ubigeo FROM public."usuario" WHERE correo = %s""", (correo,))
                row = cursor.fetchone()

                if row is not None:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    usuario = usuario.to_JSON()

            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."usuario" (nombre_perfil, contrasenna, correo, numero, fecha_nacimiento, ubigeo)
                            VALUES (%s, %s, %s, %s, %s, %s)""", (usuario.nombre_perfil, usuario.contrasenna, usuario.correo, usuario.numero, usuario.fecha_nacimiento, usuario.ubigeo))
                affected_rows = cursor.rowcount
                connection.commit()

                if affected_rows == 1:
                    login_entry = Login(None, usuario.correo, usuario.contrasenna, 3)
                    LoginModel.add_login(login_entry)

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."usuario" WHERE id_usuario = %s""", (usuario.id_usuario,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)