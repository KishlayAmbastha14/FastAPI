from fastapi import FastAPI,Query,Path,HTTPException
from typing import List,Optional

from pydantic import BaseModel,Field

app = FastAPI()

class Students(BaseModel):
  idd: int = Field(...,json_schema_extra={"description": "provide me your age"})
  title : str = Field(...,min_length=3,max_length=50)
  description : Optional[str] = None
  is_completed : bool = False
  priority : int = Field(...,ge=1,le=5,json_schema_extra={"description":"provide me your priority"})

db : List[Students] = []

try:
  @app.get("/get_all_students",tags=['READ'])
  async def getting_all_stud():
    return db
except Exception as e:
  print(e)

try:
  @app.get("/one_studetns/{stu_id}",tags=['READ'])
  async def getting_one_students(stu_id:int=Path(ge=1,le=10,description="give me the students id you want to show")):
    for s in db:
        if s.idd == stu_id:
          return s
    raise HTTPException(status_code=404,detail="no students with these id found")
except TypeError  as e:
  print(e)



@app.post("/task_create",tags=['STORE'])
async def task_creating(task:Students):
    # return {
    #   "total_task": task,
    #   "resutl" : {"task is created succesfuuly","status_code=200"}
    # }
    try:
      db.append(task)
      return db
    except Exception as e:
      raise HTTPException(status_code=500,detail=str(e))



@app.put("/update_details/{stud_id}",tags=['UPDATE'])
async def updating_details(stud:Students,stud_id:int=Path(description="provide me any id")):
    try:
      for idx,s in enumerate(db):
        if s.idd == stud_id:
          db[idx] = stud
          # print(db[s.idd])
          return db[idx]
      raise HTTPException(status_code=404,detail='Sorry this is not present')
    
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))
    

@app.delete("/delete_data/{stud_id}")
async def deleting_data(stud_id:int=Path(description="give me id to delete")):
    for s in db:
      if s.idd == stud_id:
        db.remove(s)
        return {"message":"deleted succefully"}
  
    raise HTTPException(status_code=404,detail="no id is there with this ")
