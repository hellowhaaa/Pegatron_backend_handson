from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    id: int = Field(..., description="The unique identifier for each user")
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user")