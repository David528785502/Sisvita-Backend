import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host='dpg-cptnkf88fa8c738ng680-a.oregon-postgres.render.com',
            user='postgresqlsisvita_user',
            password='dNx8NpHxSOQ1EkIa1kU7RR94Yc3GEQkR',
            database='postgresqlsisvita'
        )
    except DatabaseError as ex:
        raise ex