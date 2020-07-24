import os
from db import get_con, create_table, get_all_homes
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return get_con()


@app.route('/createTable')
def create_table_controller():
    return create_table()


@app.route('/getHomes')
def get_all_homes_controller():
    return get_all_homes()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
