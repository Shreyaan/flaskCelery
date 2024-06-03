from typing import Optional, Type

from sqlalchemy.orm import sessionmaker

from extensions.db import get_engine
from models.User import User

# from sqlalchemy import func

tables = [User]


def get_user_by_id(user_id) -> Optional[Type[User]]:
    engine = get_engine()
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user


def get_user_by_email(email) -> Optional[Type[User]]:
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter(User.email == email).first()
    session.close()
    return user


def create_user(email, raw_user_meta_data) -> User:
    engine = get_engine()
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    user = User(email=email, raw_user_meta_data=raw_user_meta_data)
    with Session.begin() as session:
        session.add(user)
        return user
