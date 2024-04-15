from sqlalchemy import Boolean, Column, String, UUID
from bcrypt import hashpw, checkpw, gensalt
from src.database.dbconfig import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True)
    name = Column(String(40), nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    verified = Column(Boolean, nullable=False)
    admin = Column(Boolean, nullable=False)


    @staticmethod
    def hash_password(password: str):
        password = password.encode("utf-8")
        return hashpw(password, gensalt(8))

    @staticmethod
    def check_password(password: str):
        return checkpw(
            password=password.encode("utf-8"),
            hashed_password=self.password.encode("utf8"),
        )