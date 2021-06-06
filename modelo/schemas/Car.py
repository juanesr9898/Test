from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class CarSchema(BaseModel): 
    model:str = Field(...) 
    color:str = Field(...)
    class Config():
        orm_mode = True
