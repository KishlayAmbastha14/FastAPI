from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas.schemas import BookBase,BookUpdate,BookModel

from todo.core.database import get_db
from typing import List
from .services import BookService

book_router = APIRouter()
book_service = BookService()

@book_router.get("/",response_model=List[BookModel])
async def get_all_books(db:AsyncSession = Depends(get_db)):
  books = await book_service.get_all_books(db)
  return books

@book_router.post("/",status_code = status.HTTP_201_CREATED,response_model=BookModel)
async def create_a_book(book_data:BookBase,db:AsyncSession = Depends(get_db)):
  try:
    new_book = await book_service.create_book(book_data,db)
    return new_book
  except Exception as e:
    raise HTTPException(
      status_code = 500,
      detail = f"Failed to create book : {str(e)}"
    )

@book_router.get("/{book_uid}")
async def get_particular_book(book_uid:str,db:AsyncSession = Depends(get_db)):
  book = await book_service.get_particular_books(book_uid,db)
  if book:
    return book
  else : 
    raise HTTPException(status_code = 404,detail="book not found")
  
@book_router.patch("/{book_uid}")
async def update_particular_book(book_uid:str,book_update_data:BookUpdate,db:AsyncSession = Depends(get_db)):
  try:
    updated_books = await book_service.update_book(book_uid,book_update_data,db)
    return updated_books
  # if updated_books:
  except Exception as e:
    raise HTTPException(
      status_code = 500,
      detail = f"Failed to create book : {str(e)}"
    )
    
@book_router.delete("/{book_uid}"
                    # status_code=status.HTTP_204_NO_CONTENT
                    )
async def delete_book(book_uid:str,db:AsyncSession = Depends(get_db)):
    deleted_books = await book_service.delete_book(book_uid,db)
    if not deleted_books:
        return {"message": "User not found"}

    return {
        "message": "User deleted successfully",
        "deleted_user_id": deleted_books.book_uid
    }
    # if not deleted_books:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="Book not found"
    #     )

    # # SUCCESS → no exception, no return body
    # return