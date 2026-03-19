from fastapi import APIRouter

router = APIRouter()

users = []

@router.get("/users")
def get_users():
    return users

@router.post("/users")
def create_user(name: str, age: int):
    user = {"name": name, "age": age}
    users.append(user)
    return {"message": "User created", "user": user}