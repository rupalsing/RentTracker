import os
from db import get_con, get_all_homes, add_home
from web_scrape import scrape_for_me
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def get_connection_controller():
    return get_con()


@app.route('/getHomes')
def get_all_homes_controller():
    return get_all_homes()


@app.route('/addHome', methods=['POST'])
def add_homes_controller():
    if 'link' not in request.form:
        return {'msg': 'Give link as form input'}
    else:
        title, rent, property_overview, lease, latitude, longitude, description, list_of_facilities, phone = \
            scrape_for_me(request.form['link'])
        return add_home(request.form['link'], title, property_overview, lease, description, list_of_facilities,
                        phone, rent, latitude, longitude)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
