from pydantic import BaseModel
from uuid import uuid4

class User(BaseModel):
    id: str = uuid4().hex
    name: str
    email: str
    password: str
    verified: bool
    admin: bool


    class Config:
        orm_mode = True
