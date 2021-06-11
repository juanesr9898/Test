from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel): 
    email:EmailStr = Field(...) 
    name:str = Field(...)
    password:str = Field(...)
    role:str = Field(...)
    class Config():
        orm_mode = True

class UserLoginSchema(BaseModel):
    email:EmailStr = Field(...) 
    password:str = Field(...)
    class Config():
        orm_mode = True


