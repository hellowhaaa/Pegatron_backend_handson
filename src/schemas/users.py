from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user")
    
class UserResponse(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user")

class CSVUser(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user")
    detail: str = Field(..., description="The detail of the user")
    
class CSVUserResponse(BaseModel):
    createdUsers: list[CSVUser] = Field(..., description="The user created from csv")
    skippedUsers: list[CSVUser] = Field(..., description="The user skipped from csv")
    
class AverageAgeResponse(BaseModel):
    firstCharacter: str = Field(..., description="the first character of the usernames")
    age: int = Field(..., description="The average age of same first character username")