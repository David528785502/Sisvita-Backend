from database.db import get_connection
from models.entities.Test import Test
from models.entities.Pregunta import Pregunta

class TestModel:

    @classmethod
    def get_tests(cls):
        try:
            connection = get_connection()
            tests = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_test, nombre, descripcion FROM tests""")
                resultset = cursor.fetchall()

                for row in resultset:
                    test = Test(row[0], row[1], row[2])
                    test.preguntas = cls.get_preguntas(test.id_test)
                    tests.append(test)  # Append the test instance

            connection.close()
            return [test.to_JSON() for test in tests]  # Convert to JSON here
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_preguntas(cls, test_id):
        try:
            connection = get_connection()
            preguntas = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_pregunta, texto, opciones FROM preguntas WHERE id_test = %s""", (test_id,))
                resultset = cursor.fetchall()

                for row in resultset:
                    pregunta = Pregunta(row[0], row[1], row[2], test_id)
                    preguntas.append(pregunta)  # Append the pregunta instance

            connection.close()
            return preguntas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_test(cls, test):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO tests (nombre, descripcion) VALUES (%s, %s) RETURNING id_test""", (test.nombre, test.descripcion))
                test_id = cursor.fetchone()[0]
                connection.commit()

            connection.close()
            return test_id
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_pregunta(cls, pregunta):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO preguntas (texto, opciones, id_test) VALUES (%s, %s, %s)""", (pregunta.texto, pregunta.opciones, pregunta.id_test))
                connection.commit()

            connection.close()
            return True
        except Exception as ex:
            raise Exception(ex)
