import os
from db import get_con, create_table, get_all_homes, add_home
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def get_connection_controller():
    return get_con()


@app.route('/createTable')
def create_table_controller():
    return create_table()


@app.route('/getHomes')
def get_all_homes_controller():
    return get_all_homes()


@app.route('/add', methods=['POST'])
def add_homes_controller():
    if 'link' not in request.form:
        return {'msg': 'Give link as form input'}
    else:
        return add_home(request.form['link'])


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
