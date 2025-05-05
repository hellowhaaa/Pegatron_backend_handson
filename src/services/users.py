from schemas.users import UserRequest, UserResponse
from sqlalchemy.exc import IntegrityError
from models.users import User as UserModel
from fastapi import HTTPException
from loguru import logger

class UserService:
    def __init__(self, db):
        self.db = db
        
    def create_user(self, r: UserRequest):
        new_user = UserModel(**r.model_dump())
        try:
            
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
        
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(
                status_code=400,
                detail="User already exists",
        )
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error creating user: {e}")

        resp = UserResponse(**r.model_dump())
        
        return resp