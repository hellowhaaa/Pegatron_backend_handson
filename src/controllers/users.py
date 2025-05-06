
from fastapi import APIRouter, Depends, UploadFile, UploadFile
from schemas.users import UserRequest, UserResponse, AverageAgeResponse, CSVUserResponse
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
    
@router.post("/upload-csv", response_model=CSVUserResponse)
def upload_csv(file: UploadFile, db: Session = Depends(get_db)):
    """
    Upload and parse a CSV file.
    """
    resp = UserService(db).create_user_via_csv(file)
    return resp

@router.get("/average-age", response_model=list[AverageAgeResponse])
def list_users(db: Session = Depends(get_db)):
    """
    Get all users' average ages.
    """
    response = UserService(db).get_average_age_grouped_by_first_char()
    return response
    
@router.post("/upload-csv/")
def upload_csv(file: UploadFile, db: Session = Depends(get_db)):
    """
    Upload and parse a CSV file.
    """
    resp = UserService(db).create_user_via_csv(file)
    
     
    return resp