from pydantic import BaseModel
from uuid import uuid4

class Addres(BaseModel):
    id: str = uuid4().hex
    user_id: str = uuid4().hex
    cep: str
    document: str
    local: str
    city: str
    state: str
    country: str

    class Config:
        orm_mode = True


