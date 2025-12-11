from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import create_engine, String, INTEGER, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session, Mapped, mapped_column
from pydantic import BaseModel
from typing import Optional, List


# ---------------------- DATABASE ----------------------
class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///books.db", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ---------------------- MODELS ------------------------
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    year: Mapped[Optional[int]] = mapped_column(INTEGER)

# ---------------------- SCHEMAS -----------------------
class BookBase(BaseModel):
    title: str
    author: str
    year: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True

# ---------------------- FASTAPI -----------------------
app = FastAPI()

# создаём таблицы
Base.metadata.create_all(bind=engine)

# зависимость для БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------- ENDPOINTS ---------------------
@app.post("/books/", response_model=BookOut)
def post_book(book: BookBase, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books", response_model=List[BookOut])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, new_book: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = new_book.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)
    return book

@app.get("/books/search/", response_model=List[BookOut])
def search_book(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[str] = Query(None),
    db: Session = Depends(get_db)):
    query = db.query(Book)
    
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)

    if query.all() == [] or (not title and not author and not year):
        raise HTTPException(status_code=404, detail="Book not found")

    return query.all()

    