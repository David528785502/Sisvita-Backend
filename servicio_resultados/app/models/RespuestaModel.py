from database.db import get_connection
from models.entities.Respuesta import Respuesta

class RespuestaModel:

    @classmethod
    def get_all_respuestas(cls):
        connection = get_connection()
        respuestas = []

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.respuesta")
                resultset = cursor.fetchall()
                for row in resultset:
                    respuesta = Respuesta(*row)
                    respuestas.append(respuesta.to_JSON())
            return respuestas
        finally:
            connection.close()

    @classmethod
    def get_respuesta_by_id(cls, id_respuesta):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.respuesta WHERE id_respuesta = %s", (id_respuesta,))
                row = cursor.fetchone()
                if row:
                    respuesta = Respuesta(*row)
                    return respuesta.to_JSON()
        finally:
            connection.close()

    @classmethod
    def get_respuesta_by_id_test_tomado_temporal(cls, id_test_tomado_temporal):
        connection = get_connection()
        respuestas = []

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.respuesta WHERE id_test_tomado_temporal = %s", (id_test_tomado_temporal,))
                resultset = cursor.fetchall()
                for row in resultset:
                    respuesta = Respuesta(*row)
                    respuestas.append(respuesta.to_JSON())
            return respuestas
        finally:
            connection.close()

    @classmethod
    def add_respuesta(cls, respuesta):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO public.respuesta (id_usuario, id_test_tomado_temporal, id_pregunta, id_test, valor) VALUES (%s, %s, %s, %s, %s)", (respuesta.id_usuario, respuesta.id_test_tomado_temporal, respuesta.id_pregunta, respuesta.id_test, respuesta.valor))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()

    @classmethod
    def delete_respuesta(cls, id_respuesta):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM public.respuesta WHERE id_respuesta = %s", (id_respuesta,))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()