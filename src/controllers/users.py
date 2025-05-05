
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

