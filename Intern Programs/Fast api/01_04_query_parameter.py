from fastapi import FastAPI
app=FastAPI()
books=[
        {"title":"title one","author":"sai","category":'science'},
        {"title":"title two","author":"sai","category":'maths'},
        {"title":"title three","author":"sai","category":'civics'},
        {"title":"title four","author":"ganesh","category":'maths'},
        {"title":"title five","author":"narsi","category":'FastAPI'}
]

@app.get("/books")
async def read_all_books():
    return books

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in books:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return=[]
    for book in books:
        if book.get('author').casefold()==book_author.casefold() and \
            book.get('category').casefold()==category.casefold():
            books_to_return.append(book)

    return books_to_return