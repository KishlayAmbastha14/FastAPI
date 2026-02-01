from fastapi import FastAPI,HTTPException,Query,Path
import json
from fastapi import APIRouter
from .schemas import StudentsData,update_stud_data,StudentCreated


app = FastAPI()

student_router = APIRouter()

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
    
  raise HTTPException(status_code = 404, detail = "no students id is found ")

## ------------- POST -----------
@student_router.post("/create",response_model = StudentCreated,tags=['CREATE'])
async def posting_stud(student1:StudentsData) -> StudentCreated:
  db.append(student1)
  return StudentCreated(student=student1,msg="Student inserted")


@student_router.put("/update/{stu_id}",response_model = StudentCreated,tags=['UPDATE'])
async def updating_stud(stu_id:int,stud:update_stud_data):
    try:
      for i in db:
        if i.id == stu_id:
          i.name = stud.name
          i.age = stud.age
          i.course = stud.course
          i.email = stud.email
          # return {"stu":i,"msg":"student updated"}
          return StudentCreated(student=i,msg="student updated")
      
      raise HTTPException(status_code = 404, detail = "student not found")
    except Exception as e:
      print(f"Error{e}")
      raise HTTPException(status_code=500, detail="Internal Server Error")
    
@student_router.delete("/delete_student/{id}",response_model = StudentCreated, tags=["DELETE"])
async def student_delete(id:int=Path(ge=0,le=100,summary="Delete a student by ID",
    description="Removes a student from the database and returns the deleted data.")):
  for stud in db:
    if stud.id == id:
      deleted_student = stud
      db.remove(stud)
      return StudentCreated(student=deleted_student,msg="this students is deleted")
    
  raise HTTPException(status_code=404, detail=f"student with {id}  is not there")



      





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
