import psycopg2


def get_connection():
    """
    Cria e retorna uma conexão com o banco PostgreSQL
    """
    conn = psycopg2.connect(
        host="localhost",
        database="iqvia",
        user="postgres",
        password="elefante321"
    )
    return conn
