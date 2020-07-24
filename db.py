import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# conn = psycopg2.connect(database='rent_tracker', user='rupal', password='postgres')


def get_con():
    cur = conn.cursor()
    cur.execute('SELECT version()')
    return "Postgres with version " + str(cur.fetchone())


def create_table():
    commands = ["create schema home_schema;",
                "create table home_schema.rent_tracker ( id serial, house_link text not null); "
                "create unique index rent_tracker_id_uindex on home_schema.rent_tracker (id);"
                "alter table home_schema.rent_tracker add constraint rent_tracker_pk primary key (id);"]
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    cur.close()
    conn.commit()
    return "create table success"


def get_all_homes():
    cur = conn.cursor()
    cur.execute("SELECT * FROM home_schema.rent_tracker")
    result = cur.fetchall()
    return {'homes': result}


def add_home(house_link):
    cur = conn.cursor()
    cur.execute("INSERT INTO home_schema.rent_tracker(house_link) VALUES('" + house_link + "')")
    conn.commit()
    return {'msg': 'Success'}
