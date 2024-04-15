from src.database.dbconfig import Base, engine
from src.models.user_db import User
from src.models.addres_db import Addres


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
