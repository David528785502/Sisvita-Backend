from database.db import get_connection
from .entities.Test import Test

class TestModel():

    @classmethod
    def get_tests(cls):
        try:
            connection = get_connection()
            tests = []
            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_test, nombre, descripcion FROM public."test" """)
                resultset = cursor.fetchall()
                for row in resultset:
                    test = Test(row[0], row[1], row[2])
                    tests.append(test.to_JSON())
            connection.close()
            return tests
        except Exception as ex:
            raise Exception("Failed to fetch tests: " + str(ex))

    @classmethod
    def get_test(cls, id_test):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_test, nombre, descripcion FROM public."test" WHERE id_test = %s""", (id_test,))
                row = cursor.fetchone()
                if row:
                    test = Test(row[0], row[1], row[2])
                    return test.to_JSON()
            connection.close()
            return None
        except Exception as ex:
            raise Exception("Failed to fetch test: " + str(ex))

    @classmethod
    def add_test(cls, test):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."test" (nombre, descripcion) VALUES (%s, %s)""", (test.nombre, test.descripcion))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows == 1
        except Exception as ex:
            raise Exception("Failed to add test: " + str(ex))

    @classmethod
    def delete_test(cls, id_test):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."test" WHERE id_test = %s""", (id_test,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows == 1
        except Exception as ex:
            raise Exception("Failed to delete test: " + str(ex))