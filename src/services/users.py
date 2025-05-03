from schemas.users import UserRequest
from models.users import User as UserModel
from core.database import get_db
class UserService:
    def __init__(self):
        self.db = get_db()
        
    def create_user(self, r: UserRequest):
        new_user = UserModel(**r.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
