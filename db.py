import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def get_con():
    cur = conn.cursor()
    cur.execute('SELECT version()')
    return "Postgres with version " + cur.fetchone()
