from schemas.users import UserRequest, UserResponse
from sqlalchemy.exc import IntegrityError
from models.users import User as UserModel
from fastapi import HTTPException, UploadFile
from loguru import logger
import pandas as pd

class UserService:
    def __init__(self, db):
        self.db = db
        
    def create_user(self, r: UserRequest) -> UserResponse:
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
    
    def delete_user_by_username(self, username: str) -> UserResponse:
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
    
    def create_user_via_csv(self, file: UploadFile) -> UserResponse:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are accepted.")

        try:
            df = pd.read_csv(file.file)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Can not parse CSV: {e}")

        created_users = []
        skipped_users = []

        for index, row in df.iterrows():
            name = row.get("Name", "").strip()
            age = row.get("Age")

            if not name:
                logger.warning(f"Row {index} has empty name, skipping.")
                skipped_users.append({"row": index, "reason": "Empty name"})
                continue

            try:
                new_user = UserModel(name=name, age=age)
                self.db.add(new_user)
                self.db.commit()
                self.db.refresh(new_user)
                logger.info(f"User created: {new_user.name}, {new_user.age}")
                created_users.append(name)
            except IntegrityError:
                self.db.rollback()
                logger.warning(f"User already exists: {name}, skipping.")
                skipped_users.append({"name": name, "reason": "Duplicate name"})
            except Exception as e:
                self.db.rollback()
                logger.error(f"Error creating user {name}: {e}")
                skipped_users.append({"name": name, "reason": str(e)})

        return {
            "created": created_users,
            "skipped": skipped_users,
            "message": f"{len(created_users)} users created, {len(skipped_users)} skipped."
        }