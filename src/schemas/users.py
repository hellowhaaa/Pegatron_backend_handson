from pydantic import BaseModel, Field, field_validator


class UserRequest(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user")
    
    @field_validator("name")
    def name_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty or blank")
        return v
    
    @field_validator("age")
    def age_limitation(cls, v):
        if v < 0 or v > 150:
            raise ValueError("Age must be in normal range (0-150)")
        return v
    
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