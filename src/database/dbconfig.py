from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine(
    "postgresql+psycopg://wwoufozh:ra6NUcbcFuLOpE9siKnJi8FUDOF674ZD@isabelle.db.elephantsql.com/wwoufozh"
)

Base = declarative_base()
session = Session(engine)