from fastapi import FastAPI,HTTPException,Query,Path
from typing import List,Literal,Optional,Dict,Annotated
import json
from fastapi import APIRouter
from .schemas import StudentsData,update_stud_data,StudentCreated


app = FastAPI()

student_router = APIRouter()

# try:
#   def load_students():
#     with open("data.json","r") as file:
#       return json.load(file)

# except Exception as e:
#   print(e)
# data = load_students()


db : list[StudentsData] = []


## --------------- GET -----------------
@student_router.get("/total_students",tags=['READ'])
async def get_total():
  return db

@student_router.get("/particular_students/{id}",tags=['READ'])
async def particular_stu(id:int=Path(ge=0,le=100,description="provide me student id eg:1, or 2 ")):
  for stu in db:
    if stu.id == id:
      return stu
    else: 
      return {"message":"no student_with this id is present"}

## ------------- POST -----------
@student_router.post("/create",response_model = StudentCreated,tags=['CREATE'])
async def posting_stud(student1:StudentsData) -> StudentCreated:
  db.append(student1)
  return StudentCreated(student=student1,msg="Student inserted")


@student_router.put("/update/{stu_id}",response_model = update_stud_data,tags=['UPDATE'])
try:
  async def updating_stud(stud_id:int,stud:StudentsData) -> update_stud_data:
    for i in db:
      if i.id == stud.id:
        i.name = stud.name
        i.age = stud.age
        i.course = stud.course
        i.email = stud.email
        return StudentCreated(stud=i,msg="student updated")
except Exception as e:
  print(e)

      
      





# try:
#   @app.get("/get_all_students",tags=['READ'])
#   async def getting_all_stud():
#     return db
# except Exception as e:
#   print(e)

# try:
#   @app.get("/one_studetns/{stu_id}",tags=['READ'])
#   async def getting_one_students(stu_id:int=Path(ge=1,le=10,description="give me the students id you want to show")):
#     for s in db:
#         if s.idd == stu_id:
#           return s
#     raise HTTPException(status_code=404,detail="no students with these id found")
# except TypeError  as e:
#   print(e)



# @app.post("/task_create",tags=['STORE'])
# async def task_creating(task:Students):
#     # return {
#     #   "total_task": task,
#     #   "resutl" : {"task is created succesfuuly","status_code=200"}
#     # }
#     try:
#       db.append(task)
#       return db
#     except Exception as e:
#       raise HTTPException(status_code=500,detail=str(e))



# @app.put("/update_details/{stud_id}",tags=['UPDATE'])
# async def updating_details(stud:Students,stud_id:int=Path(description="provide me any id")):
#     try:
#       for idx,s in enumerate(db):
#         if s.idd == stud_id:
#           db[idx] = stud
#           # print(db[s.idd])
#           return db[idx]
#       raise HTTPException(status_code=404,detail='Sorry this is not present')
    
#     except Exception as e:
#       raise HTTPException(status_code=500, detail=str(e))
    

# @app.delete("/delete_data/{stud_id}")
# async def deleting_data(stud_id:int=Path(description="give me id to delete")):
#     for s in db:
#       if s.idd == stud_id:
#         db.remove(s)
#         return {"message":"deleted succefully"}
  
#     raise HTTPException(status_code=404,detail="no id is there with this ")
