from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class CarSchema(BaseModel): 
    model:Optional[str]
    color:Optional[str]
    id:Optional[int]
    class Config():
        orm_mode = True