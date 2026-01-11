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
  

@app.get("/single_student/{student_id}")
async def stud_id(student_id:int):
  if student_id not in students_db:
    raise HTTPException(status_code=404 ,detail="no students id is founded")
  return students_db[student_id]


@app.get("/student_course")
async def courses(course:str):
  result = []
  
  for student in students_db.values():
    if student['course'].lower() == course.lower():
      result.append(student)
      
  if not result:
      raise HTTPException(status_code=404,detail="no course name is there")
  return result

# Write a route that:
# Uses query param course
# Returns matching students
# If no course → return all students
 





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


# esign a route to:

# “Get student 1 details”

@app.get("/details/{ids}")
async def detail(ids:int):
  if ids in students_db:
    return students_db[ids]

# Q7

# Design a route to:

# “Get students older than 21”

# students_db = {
#     1: {"name": "Rohan", "age": 21, "course": "DS"},
#     2: {"name": "Kishlay", "age": 22, "course": "AI"},
#     3: {"name": "Rahul", "age": 23, "course": "Big Data"},
#     4: {"name": "Aman", "age": 21, "course": "AI"},
# }

@app.get("/age")
async def agess(ages:int):
  result = []
  for student in students_db.values():
    # print(student)
    if student['age'] > 21:
      result.append(student)
  
  return result
    

# Q8

# Design a route to:

# “Get all students sorted by age”

@app.get("/students/sorted_age")
async def get_students_sorted(order:str='asc'):

  reverse = True if order == "desc" else False

  return sorted (
    students_db.values(),
    key= lambda student:student["age"],
    reverse=reverse
  )
 

@app.get("/ai_students/sorted_by_age")
async def get_ai_students():
  # return students_db
  # return sorted(
  #   students_db.values(),
  #   key = lambda student:student['course'] == 'AI'
  #         )
  reslt = []
  for students in students_db.values():
    if students['course'] == 'AI':
      reslt.append(students)
      # return reslt

  reslt = sorted(
    reslt,
    key = lambda students : students['age'],
    reverse=True
  )

  return reslt


# “Get students age > 21, course = AI, sorted by age asc”

@app.get("/studentss/greater21/course_AI")
async def answer(age:int,course=str):
  result = []
  for student in students_db.values():
    # if student['age'] > age and student['course'] == course:
    if student['age'] > age and student['course'] == course:
      result.append(student)

  return result 


# 11
# Write a route that:

# Uses path param for student_id
@app.get("/all_students1234/{student_id}")
async def all_studdnets_data(student_id:int):
  if student_id not in students_db:
    raise HTTPException(status_code=404, detail="no students present")
  return students_db[student_id]

@app.get("/allstudents/{student_id}")
async def stud_id(student_id:int):
  if student_id not in students_db:
    raise HTTPException(status_code=404 ,detail="no students id is founded")
  return students_db[student_id]

  
  

# Returns student data

# Returns 404 if not found

# Q12

# Write a route that:

# Uses query param course

# Returns matching students

# If no course → return all students

# Q13

# Write a route that:

# Uses query param min_age

# Filters students older than min_age

# @app.get("/minimum_age")
# async def mini(age:int)

# Q14

# Make course optional query param.

# Q15

# Make course mandatory query param.

# 🔴 LEVEL 4 — CONFUSION KILLER QUESTIONS 🔥
# Q16