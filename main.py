from fastapi import FastAPI
from src.routes import user, addres

app = FastAPI()
app.include_router(user.api_router)
app.include_router(addres.api_router)

