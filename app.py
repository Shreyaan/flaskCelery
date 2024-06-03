import os

from flask import Flask

from extensions import db
from models import init_tables
from routes.user import user

app = Flask(__name__)
app.register_blueprint(user)

pg_url = os.getenv("pg_url")
db.init_db_connection(pg_url)
init_tables()


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


if __name__ == "__main__":
    app.debug = 1
    app.run(debug=True, port=5000)
