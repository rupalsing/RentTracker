import os
import json
import psycopg2
from mapbox_helper import get_stores_location

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def update_nav_links():
    cur = conn.cursor()
    cur.execute("SELECT * FROM home_schema.rent_tracker")
    result = cur.fetchall()
    for row in result:
        lat = row[8]
        long = row[9]
        stores = get_stores_location(lat, long)
        cur = conn.cursor()
        query = """ UPDATE home_schema.rent_tracker SET stores = %s WHERE link=%s"""
        record = (json.dumps(stores), row[0])
        cur.execute(query, record)
        conn.commit()


update_nav_links()
