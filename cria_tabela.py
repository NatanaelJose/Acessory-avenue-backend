from src.database.dbconfig import Base, engine
from src.models.user_db import User


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
