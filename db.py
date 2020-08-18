import os
import json
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# conn = psycopg2.connect(database='test_rent', user='rupal', password='postgres')


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
            'link': row[0],
            'title': row[1],
            'property_overview': row[2],
            'lease': row[3],
            'description': row[4],
            'facilities': json.loads(row[5]),
            'phones': json.loads(row[6]),
            'rent': row[7],
            'latitude': row[8],
            'longitude': row[9],
            'stores': json.loads(row[10])
        })
    return ans


def add_home(link, title, prop_over, lease, description, facilities, phone, rent, latitude, longitude, stores):
    cur = conn.cursor()
    query = """ INSERT INTO home_schema.rent_tracker (link, title, prop_over, lease, description, facilities,
     phone, rent, latitude, longitude, stores) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)"""
    record = (link, title, prop_over, lease, description, facilities, phone, rent, latitude, longitude, stores)
    cur.execute(query, record)
    conn.commit()
    return {'msg': 'Success'}
