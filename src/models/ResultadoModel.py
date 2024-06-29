from database.db import get_connection
from .entities.Resultado import Resultado
import json

class ResultadoModel():

    @classmethod
    def save_resultado(self, resultado):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO resultados (id_usuario, id_test, respuestas, resultado)
                    VALUES (%s, %s, %s, %s)
                """, (resultado.id_usuario, resultado.id_test, json.dumps(resultado.respuestas), resultado.resultado))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_resultados_by_usuario(self, id_usuario):
        try:
            connection = get_connection()
            resultados = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT r.id_resultado, r.id_usuario, r.id_test, r.respuestas, r.resultado, t.nombre
                    FROM resultados r
                    JOIN tests t ON r.id_test = t.id_test
                    WHERE r.id_usuario = %s
                """, (id_usuario,))
                resultset = cursor.fetchall()

                for row in resultset:
                    resultado = {
                        'id_resultado': row[0],
                        'id_usuario': row[1],
                        'id_test': row[2],
                        'respuestas': row[3],
                        'resultado': row[4],
                        'nombre_test': row[5]
                    }
                    resultados.append(resultado)

            connection.close()
            return resultados
        except Exception as ex:
            raise Exception(ex)
