
from fastapi import APIRouter, Depends
from schemas.users import UserRequest, UserResponse
from services.users import UserService
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(r: UserRequest, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    response = UserService(db).create_user(r)
    
    return response

@router.delete("/names/{username}", response_model=UserResponse)
def delete_user(username: str, db: Session = Depends(get_db)):
    """
    Delete a user by username.
    """
    response = UserService(db).delete_user_by_username(username)
    
    return response

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    """
    List all users.
    """
    response = UserService(db).get_all_users()
    
    return response