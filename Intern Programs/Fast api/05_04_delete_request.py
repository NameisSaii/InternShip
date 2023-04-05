from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    class Config:
        schema_extra = {
            'example': {
                'title': 'A new Book',
                'author': 'sai',
                'description': 'a new desc',
                'rating': 5
            }
        }


BOOKS = [
    Book(1, 'Computer Science', 'Sai', 'Nice Book', 5),
    Book(2, 'Fast api', 'Sai', 'Great Book', 5),
    Book(3, 'Master Endpoints', 'Sai', 'Awesome Book', 5),
    Book(4, 'HP1', 'Sai', 'Book Description', 2),
    Book(5, 'HP2', 'Sai', 'Book Description', 3),
    Book(6, 'HP3', 'Sai', 'Book Description', 1)

]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(Book_id: int):
    for book in BOOKS:
        if book.id == Book_id:
            return book


@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_retrun = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_retrun.append(book)
    return books_to_retrun


@app.post("/create-book")
async def create_book(book_request: BookRequest):  # passing book_request of type BookRequest
    new_book = Book(
        **book_request.dict())  # BookRequest matches Book,so we create new varaible of new_book which is equal to book

    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/book/{book_id}")
async def delete_book(book_id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            break 