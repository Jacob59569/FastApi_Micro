from fastapi import APIRouter
from app.models import User
from app.services import greet_user

router = APIRouter()

@router.get("/")
def root():
    return {"message": "FastAPI is working"}

@router.post("/greet")
def greet(user: User):
    return {"message": greet_user(user.name)}