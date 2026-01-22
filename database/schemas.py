from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
  email : EmailStr
  password : str

class UserResponse(BaseModel):
  ids : int
  email : EmailStr

  class Config:
    from_attributes = True
  
class Login_user(BaseModel):
  email: str
  password: str


