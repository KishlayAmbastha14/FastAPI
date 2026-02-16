from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,desc
from sqlalchemy import text
from .schemas.schemas import BookBase,BookCreate,BookUpdate,BookModel
from .models.models import Book





class BookService:
  async def get_all_books(self,db:AsyncSession):
#     sql_st = text(""" SELECT * 
#                   FROM books
#     ORDER BY created_at DESC
# """)
#     sql_result = await db.execute(sql_st)
#     books = sql_result.fetchall()
#     return books
  
    statement = select(Book).order_by(desc(Book.created_at))
    result = await db.execute(statement)
    books = result.scalars().all()
    return books

  
  async def get_particular_books(self,book_id:str,db:AsyncSession):
    statement = select(Book).where(Book.uid == book_id)
    result = await db.execute(statement)
    book =  result.scalars().first()
    return book if book is not None else None
  
  
  async def create_book(self,book_data:BookCreate,db:AsyncSession):
    book_data_dict = book_data.model_dump()
    new_book = Book(**book_data_dict)
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book
  
  async def update_book(self,book_id:str,book_update:BookUpdate,db:AsyncSession):
    book_to_update = await self.get_particular_books(book_id,db)
    if book_to_update is not None:
      update_data_dict = book_update.model_dump()
      for k,v in update_data_dict.items():
        setattr(book_to_update,k,v)
      await db.commit()
      await db.refresh(book_to_update)
      return book_to_update
    else:
      return None

  async def delete_book(self,book_id:str,db:AsyncSession):
    book_to_delete = await self.get_particular_books(book_id,db)
    if book_to_delete is not None:
      await db.delete(book_to_delete)
      await db.commit()
      return {}
    else: 
      return None
      

