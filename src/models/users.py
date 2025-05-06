from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.core.database import Base
    
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    age = Column(Integer)
    