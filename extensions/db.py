import time
from typing import Optional

import psycopg2
import psycopg2.extras
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool

engine: Optional[sqlalchemy.engine.Engine] = None
Base = declarative_base()


def init_db_connection(connect_str):
    """Initializes database connection using the specified Flask app.

    Configuration file must contain `SQLALCHEMY_DATABASE_URI` key. See
    https://pythonhosted.org/Flask-SQLAlchemy/config.html#configuration-keys
    for more info.
    """
    global engine
    while True:
        try:
            print("Connecting to db...", connect_str)
            engine = create_engine(connect_str, poolclass=NullPool)
            Base.metadata.create_all(engine)
            print(engine)
            break
        except psycopg2.OperationalError as e:
            print("Couldn't establish connection to db: {}".format(str(e)))
            print("Sleeping 2 seconds and trying again...")
            time.sleep(2)


def get_engine() -> sqlalchemy.engine.Engine:
    return engine
