import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# conn = psycopg2.connect(database='rent_tracker', user='rupal', password='postgres')


def get_con():
    cur = conn.cursor()
    cur.execute('SELECT version()')
    return "Postgres with version " + str(cur.fetchone())


def get_all_homes():
    cur = conn.cursor()
    cur.execute("SELECT * FROM home_schema.rent_tracker")
    result = cur.fetchall()
    ans = {'homes': []}
    for row in result:
        ans['homes'].append({
            'id': row[0],
            'link': row[1],
            'title': row[2],
            'property_overview': row[3],
            'lease': row[4],
            'description': row[5],
            'facilities': row[6],
            'phone': row[7],
        })
    return ans


def add_home(link, title, prop_over, lease, description, facilities, phone, rent, latitute, longitude):
    cur = conn.cursor()
    query = """ INSERT INTO home_schema.rent_tracker (link, title, prop_over, lease, description, facilities,
     phone, rent, latitute, longitude) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record = (link, title, prop_over, lease, description, facilities, phone, rent, latitute, longitude)
    cur.execute(query, record)
    conn.commit()
    return {'msg': 'Success'}
