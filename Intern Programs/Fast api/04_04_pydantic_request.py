from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id:int
    title:str
    author:str
    description:str
    rating:int
BOOKS=[
    Book(1,'Computer Scinece','Sai','Nice Book',5),
    Book(1, 'Fast api', 'Sai', 'Great Book', 5),
    Book(1, 'Master Endpoints', 'Sai', 'Awesome Book', 5),
    Book(1, 'HP1', 'Sai', 'Book Description', 2),
    Book(1, 'HP2', 'Sai', 'Book Description', 3),
    Book(1, 'HP3', 'Sai', 'Book Description',1)

]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request:BookRequest):#passing book_request of type BookRequest
    new_book=Book(**book_request.dict())#BookRequest matches Book,so we create new varaible of new_book which is equal to book
    #** is the way to expand this dictionary..so which is going to retrun all of the variabels into dictionary format
    #this allows us to expand those dictionary keys and values into keyment arguments are needed ..so we're saying create a new book inside our book,inside our book constructor
    print(type(new_book))
    BOOKS.append(new_book)

