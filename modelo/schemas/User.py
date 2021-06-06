from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel): 
    email:EmailStr = Field(...) 
    name:Optional[str] = "UserTest"
    password:str = Field(...)
    role:str = Field(...)
    