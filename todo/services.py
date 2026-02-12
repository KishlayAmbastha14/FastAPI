from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,desc

from schemas.schemas import BookBase,BookCreate,BookUpdate,BookModel
from models.models import Book





class BookService:
  async def get_all_books(self,db:AsyncSession):
    statement = select(Book).order_by(desc(Book.created_at))
    result = await db.execute(statement)
    books = result.scalars().all()
    return books
  
  async def get_particular_books(self,book_id:str,db:AsyncSession):
    statement = select(Book).where(Book.uid == book_id)
    result = await db.execute(statement)
    book =  result.scalars().first()
    return book
  
  
  async def create_book(self,book_data:BookCreate,db:AsyncSession):
    book_data_dict = book_data.model_dump()
    new_book = Book(**book_data_dict)
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book
  
