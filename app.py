import os
from db import get_con, create_table
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return get_con()


@app.route('/createTable')
def create_table_controller():
    return create_table()


create_table()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
