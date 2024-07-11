from database.db import get_connection
from .entities.Resultado import Resultado
from datetime import datetime
from utils.DateFormat import DateFormat

class ResultadoModel:
    @classmethod
    def get_all_resultados(cls):
        try:
            connection = get_connection()
            resultados = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.resultado")
                for row in cursor.fetchall():
                    resultado = Resultado(*row)
                    resultados.append(resultado.to_JSON())
            return resultados
        finally:
            connection.close()

    @classmethod
    def get_resultado_by_id(cls, id_resultado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.resultado WHERE id_resultado = %s", (id_resultado,))
                row = cursor.fetchone()
                if row:
                    resultado = Resultado(*row)
                    return resultado.to_JSON()
        finally:
            connection.close()

    @classmethod
    def get_resultados_by_id_usuario(cls, id_usuario):
        try:
            connection = get_connection()
            resultados = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.resultado WHERE id_usuario = %s", (id_usuario,))
                for row in cursor.fetchall():
                    resultado = Resultado(*row)
                    resultados.append(resultado.to_JSON())
            return resultados
        finally:
            connection.close()

    @classmethod
    def get_resultados_by_id_test(cls, id_test):
        try:
            connection = get_connection()
            resultados = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.resultado WHERE id_test = %s", (id_test,))
                for row in cursor.fetchall():
                    resultado = Resultado(*row)
                    resultados.append(resultado.to_JSON())
            return resultados
        finally:
            connection.close()
            
    @classmethod
    def add_resultado(cls, id_usuario, id_test, id_test_tomado_temporal):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                # Fetch user profile name and ubigeo
                cursor.execute("SELECT nombre_perfil, ubigeo FROM public.usuario WHERE id_usuario = %s", (id_usuario,))
                user_details = cursor.fetchone()

                # Fetch test name
                cursor.execute("SELECT nombre FROM public.test WHERE id_test = %s", (id_test,))
                test_name = cursor.fetchone()[0]

                # Compute diagnostic value from responses
                cursor.execute("SELECT SUM(valor) FROM public.respuesta WHERE id_test_tomado_temporal = %s", (id_test_tomado_temporal,))
                diagnostic_sum = cursor.fetchone()[0] or 0

                # Determine color based on diagnostic sum
                if diagnostic_sum < 30:
                    color = 1
                elif 30 <= diagnostic_sum < 60:
                    color = 2
                elif 60 <= diagnostic_sum < 80:
                    color = 3
                else:
                    color = 4  # Assuming a default value for sums >= 80

                # Current date
                current_date = datetime.now()

                # Insert new result
                cursor.execute("""
                    INSERT INTO public.resultado 
                    (id_usuario, nombre_perfil, ubigeo, id_test, test, diagnostico, color, fecha, id_test_tomado_temporal) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (id_usuario, user_details[0], user_details[1], id_test, test_name, diagnostic_sum, color, current_date, id_test_tomado_temporal))
                connection.commit()

                return cursor.rowcount == 1
        finally:
            connection.close()

    @classmethod
    def delete_resultado(cls, id_resultado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM public.resultado WHERE id_resultado = %s", (id_resultado,))
                connection.commit()
                return cursor.rowcount == 1
        finally:
            connection.close()