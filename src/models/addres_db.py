from sqlalchemy import Column, String, UUID, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.database.dbconfig import Base
from src.models.user import User
from datetime import datetime


class Addres(Base):
    __tablename__ = "addresses"

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey('users.id'))
    cep = Column(String(9), nullable=False)
    document = Column(String, unique=True)
    local = Column(String)
    city = Column(String(25))
    state = Column(String(25))
    country = Column(String(25))
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="addresses", cascade="all, delete-orphan")
