from fastapi import FastAPI,Body

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

@app.get("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)