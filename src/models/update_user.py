from pydantic import BaseModel

class UpdateUser(BaseModel):
    name: str | None = ''
    login: str | None = ''
    email: str | None = ''
    password: str | None = ''
    verified: bool | None = ''
    admin: bool | None = ''