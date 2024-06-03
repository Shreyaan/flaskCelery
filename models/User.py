from sqlalchemy import Column, UUID, VARCHAR, func
from sqlalchemy.dialects.postgresql import JSONB

from extensions.db import Base


class User(Base):
    __tablename__ = "users"
    # __table_args__ = dict(schema="auth")

    id = Column(UUID, primary_key=True, server_default=func.gen_random_uuid())
    email = Column(VARCHAR(255), nullable=False)
    raw_user_meta_data = Column(JSONB)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "raw_user_meta_data": self.raw_user_meta_data,
        }
