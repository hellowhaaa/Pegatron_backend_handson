from src.controllers import users, root 
from fastapi import APIRouter
router = APIRouter()
router.include_router(root.router, tags=["root"])
router.include_router(users.router, prefix="/users", tags=["users"])
