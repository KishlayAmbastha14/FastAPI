from fastapi import FastAPI,HTTPException
from typing import List,Union
from enum import Enum

app = FastAPI()

students_db = {
    1: {"name": "Rohan", "age": 21, "course": "DS"},
    2: {"name": "Kishlay", "age": 22, "course": "AI"},
    3: {"name": "Rahul", "age": 23, "course": "Big Data"},
    4: {"name": "Aman", "age": 21, "course": "AI"},
}


@app.get("/")
async def call():
  for key,value in students_db.items():
    return key,value
    # for key,value in i.items():
    #   return value


# Q1

# Design a route to get student with ID = 3
# @app.get("/single_student/{student_id}")
# async def stud_id(student_id:int):
#   if student_id not in students_db:
#     raise HTTPException(status_code=404 ,detail="no students id is founded")
#   return students_db[student_id]


# 👉 URL only (no code)

# Q2

# Design a route to get all students


# Q3

# Design a route to get all students whose course is AI

#  ---------- WRONG HAI 
# @app.get("/student_course/{course}")
# async def course(course:str):
#   for key,value in students_db.items():
#     if course == value['course']:
#       print(course)
#       print(value['course'])
#       return students_db
#     else:
#       return course
#   raise HTTPException(status_code=404,detail="no course name is there")

# for key,value in students_db.items():
#   print(value['course'] == "AI")

@app.get("/student_course")
async def courses(course:str):
  result = []
  
  for student in students_db.values():
    # print(course)
    if student['course'].lower() == course.lower():
      # return students_db[course]
      result.append(student)
      
  if not result:
      raise HTTPException(status_code=404,detail="no course name is there")
  return result
 

# Q4

# Is this PATH or QUERY?

# /students/2

# Q5

# Is this PATH or QUERY?

# /students?course=AI

# 🟡 LEVEL 2 — THINK & DESIGN (MOST IMPORTANT)
# Q6

# Design a route to:

# “Get student 1 details”