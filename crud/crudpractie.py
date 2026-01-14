from fastapi import FastAPI,HTTPException,Query,Path
from typing import List,Literal,Optional,Dict,Annotated
import json

from pydantic import BaseModel,Field

app = FastAPI()

def load_students():
  with open("data.json","r") as file:
    return json.load(file)

data = load_students()



@app.get("/total_students")
async def get_total():
  return data

@app.get("/total_students/{ids}")
async def get_particular_students(ids:Annotated[int,Path(title="enter the integer number",ge=1,le=7)]):
  student_id = str(ids)
  if student_id not in data:
    raise HTTPException(status_code=404,detail="no data is found")
  return data[student_id]


# ------------------- 
class stud_data(BaseModel):
    idss: int = Field(ge=1,le=100)
    name: str = Field("give me the name")
    age: int = Field(ge=10,le=100)
    course: str 
    email: str


# @app.get("/stud",response_model=List[stud_data])
@app.get("/stud",response_model=Dict[str,stud_data])
async def fetching_all_stud():
  # return list(data.values())
  return data


#-------- ppp----
store = []
@app.post("/post_stud")
async def posting_stud(student:stud_data):
  st_data = student.model_dump()
  # **data.model_dump(st_data)
  store.append(st_data)
  return st_data


#---- second way ----------------------------------------------------------

def load_student():
  with open("student.json","r") as f:
    return json.load(f)


student_datas = load_student()

@app.get("/stu")
async def rest():
  return student_datas

@app.post("/post_stu")
async def posting_stue(stud:stud_data):
  current_data = stud.model_dump()
  student_datas.append(current_data)
  return current_data

# ----- studetn.json-------
@app.get("/get_stu/{student_id}")
async def getting_student(student_id:Annotated[int,Path(title="provide me student id",ge=1,le=10)]):
  for student in student_datas:
    if student['idss'] == student_id:
      return student
  raise HTTPException(status_code=404,detail="nothing is found")

# ---- data.json -----
@app.get("/g_stu/{stud_id}")
async def getting_stu(stud_id:Annotated[int,Path(title="provide me id")]):
  student_id = str(stud_id)
  if student_id in data:
    return data[student_id]
  raise HTTPException(status_code = 404, detail="sorry this is not present")