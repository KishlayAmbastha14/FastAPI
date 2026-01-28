from fastapi import FastAPI
from src.students.routes import student_router 


app = FastAPI()

app.include_router(student_router,prefix=f"/api/students")