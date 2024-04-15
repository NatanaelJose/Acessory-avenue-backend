from fastapi import APIRouter, Response, status
from src.errors.user_not_found_exception import UserNotFoundException
from src.static.messages import NOT_FOUND, INTERNAL_ERROR


api_router = APIRouter(prefix="/adress")

@api_router.get("", status_code=status.HTTP_200_OK)
def list_adress():
    return 'ok'