
from fastapi import APIRouter
from schemas.users import UserRequest
from services.users import UserService

router = APIRouter()


@router.post("/")
def create_user(r: UserRequest):
    """
    Create a new user.
    """
    response = UserService().create_user(r)
    
    return response

