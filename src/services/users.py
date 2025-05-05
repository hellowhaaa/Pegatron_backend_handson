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
    
    def delete_user_by_username(self, username: str):
        user = self.db.query(UserModel).filter(UserModel.name == username).first()
        
        # Check if user exists
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        try:
            self.db.delete(user)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error deleting user: {e}")
        
        resp = UserResponse(
            name=user.name,
            age=user.age
        )
        
        return resp
    
    def get_all_users(self) -> list[UserResponse]:
        try:
            users = self.db.query(UserModel).all()
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error retrieving users: {e}")
            raise HTTPException(status_code=500, detail="Error retrieving users")
        
        resp = [UserResponse(name=user.name, age=user.age) for user in users]
        return resp