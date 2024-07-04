from database.db import get_connection
from .entities.TestTomadoTemporal import TestTomadoTemporal

class TestTomadoTemporalModel:

    @classmethod
    def get_all_tests(cls):
        try:
            connection = get_connection()
            tests = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_test_tomado_temporal FROM public.test_tomado_temporal")
                resultset = cursor.fetchall()

                for row in resultset:
                    test = TestTomadoTemporal(row[0])
                    tests.append(test.to_JSON())

            connection.close()
            return tests
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_test(cls, id_test_tomado_temporal):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_test_tomado_temporal FROM public.test_tomado_temporal WHERE id_test_tomado_temporal = %s", (id_test_tomado_temporal,))
                row = cursor.fetchone()

                test = None
                if row is not None:
                    test = TestTomadoTemporal(row[0])
                    test = test.to_JSON()

            connection.close()
            return test
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_test(cls, test):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO public.test_tomado_temporal DEFAULT VALUES")
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_test(cls, id_test_tomado_temporal):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM public.test_tomado_temporal WHERE id_test_tomado_temporal = %s", (id_test_tomado_temporal,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_last_test(cls):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_test_tomado_temporal FROM public.test_tomado_temporal ORDER BY id_test_tomado_temporal DESC LIMIT 1")
                row = cursor.fetchone()

                test = None
                if row is not None:
                    test = TestTomadoTemporal(row[0])
                    test = test.to_JSON()

            connection.close()
            return test
        except Exception as ex:
            raise Exception(ex)
