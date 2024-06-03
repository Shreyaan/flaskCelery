from .User import User

tables = [User]


def init_tables():
    from extensions.db import Base, engine

    Base.metadata.create_all(engine)
    print("Tables initialized")
