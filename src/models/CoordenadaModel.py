from database.db import get_connection
from .entities.Coordenada import Coordenada
import pandas as pd

class CoordenadaModel:

    @classmethod
    def get_all_coordenadas(cls):
        try:
            connection = get_connection()
            coordenadas = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_coordenada, y, x FROM coordenada""")
                resultset = cursor.fetchall()

                for row in resultset:
                    coordenada = Coordenada(row[0], row[1], row[2])
                    coordenadas.append(coordenada.to_json())

            connection.close()
            return coordenadas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_coordenada(cls, ubigeo):
        try:
            # Cargar el archivo Excel
            df = pd.read_excel('C:/Users/David/OneDrive/Escritorio/back/src/models/geodir-ubigeo-reniec.xlsx')  # Cargamos como cadenas para manejar los ceros a la izquierda

            # Buscar las coordenadas para el ubigeo dado
            row = df[df['Ubigeo'] == ubigeo]

            if row.empty:
                raise Exception(f"No se encontraron coordenadas para el ubigeo {ubigeo}")

            # Obtener y convertir las coordenadas a números decimales
            y = float(row['Y'].iloc[0])
            x = float(row['X'].iloc[0])

            connection = get_connection()

            with connection.cursor() as cursor:
                # Insertar las coordenadas en la base de datos
                cursor.execute("""INSERT INTO coordenada (y, x) VALUES (%s, %s) RETURNING id_coordenada""", (y, x))
                id_coordenada = cursor.fetchone()[0]
                connection.commit()

            connection.close()
            return id_coordenada
        except Exception as ex:
            raise Exception(ex)
