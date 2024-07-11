from database.db import get_connection
from .entities.Pregunta import Pregunta

class PreguntaModel:

    @classmethod
    def get_preguntas(cls):
        try:
            connection = get_connection()
            preguntas = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_pregunta, id_test, texto FROM public."pregunta" """)
                resultset = cursor.fetchall()

                for row in resultset:
                    pregunta = Pregunta(row[0], row[1], row[2])
                    preguntas.append(pregunta.to_JSON())

            connection.close()
            return preguntas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_pregunta(cls, id_pregunta):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_pregunta, id_test, texto FROM public."pregunta" WHERE id_pregunta = %s""", (id_pregunta,))
                row = cursor.fetchone()

                pregunta = None
                if row is not None:
                    pregunta = Pregunta(row[0], row[1], row[2])
                    pregunta = pregunta.to_JSON()

            connection.close()
            return pregunta
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_preguntas_by_id_test(cls, id_test):
        try:
            connection = get_connection()
            preguntas = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_pregunta, id_test, texto FROM public."pregunta" WHERE id_test = %s""", (id_test,))
                resultset = cursor.fetchall()

                for row in resultset:
                    pregunta = Pregunta(row[0], row[1], row[2])
                    preguntas.append(pregunta.to_JSON())

            connection.close()
            return preguntas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_pregunta(cls, pregunta):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."pregunta" (id_test, texto) VALUES (%s, %s)""", (pregunta.id_test, pregunta.texto))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_pregunta(cls, id_pregunta):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."pregunta" WHERE id_pregunta = %s""", (id_pregunta,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_preguntas_by_test(cls, id_test):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."pregunta" WHERE id_test = %s""", (id_test,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
