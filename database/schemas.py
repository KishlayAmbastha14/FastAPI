from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
  email : EmailStr
  password : str

class UserResponse(BaseModel):
  id : int
  email : EmailStr

  class Config:
    from_attributes = True
  
class Login_user(BaseModel):
  email: str
  password: str


class delete_user(BaseModel):
  id : int
  # email : str

class DeleteResponse(BaseModel):
  message: str
  delete_user_id : int 