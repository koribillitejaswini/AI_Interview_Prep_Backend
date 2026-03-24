from fastapi import APIRouter
from database import users_collection
from models import User

router = APIRouter()

@router.post("/register")
def register(user: User):
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(email: str, password: str):
    user = users_collection.find_one({"email": email, "password": password})
    if user:
        return {"message": "Login successful"}
    return {"error": "Invalid credentials"}