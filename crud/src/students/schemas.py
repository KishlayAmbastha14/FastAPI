from pydantic import BaseModel,Field
from typing import Optional,List


# ------------------- 

class StudentsData(BaseModel):
    id: int = Field(ge=1,le=100)
    name: str = Field("give me the name")
    age: int = Field(ge=10,le=100)
    course: str 
    email: str



# PATCH -- partial updte hoga iha to hame optional dena hoga
class update_stud_data(BaseModel):
  name:Optional[str] = None
  age:Optional[int] = None
  course:Optional[str] = None
  email:Optional[str] = None


class StudentCreated(BaseModel):
   student : StudentsData
   msg : str