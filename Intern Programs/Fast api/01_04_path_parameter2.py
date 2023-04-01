from fastapi import FastAPI
app=FastAPI()
books=[
        {"title":"title one","author1":"saikumar","category":'science'},
        {"title":"title two","author2":"saikumar","category":'histor'},
        {"title":"title three","author3":"saikumar","category":'civics'},
        {"title":"title four","author4":"saikumar","category":'maths'},
        {"title":"title five","author5":"saikumar","category":'science'}
]

@app.get("/books")
async def read_all_books():
    return books

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book

