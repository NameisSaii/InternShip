from fastapi import FastAPI
app=FastAPI()
books=[
        {"title":"sai","author":"saikumar","category":'science'},
        {"title":"sai","author":"saikumar","category":'histor'},
        {"title":"sai","author":"saikumar","category":'civics'},
        {"title":"sai","author":"saikumar","category":'maths'},
        {"title":"sai","author":"saikumar","category":'science'}
]
@app.get("/books/mybook")
async def read_all_mybooks():
        return {'book_title':'my favorite book'}

@app.get("/books/{dynamic_param}")
async def first_api():
    return books

async def read_all_books(dynamic_param:str):
        return {'dynamic_param':dynamic_param}
"""
@app.get("/books/mybook")
async def read_all_mybooks():
        return {'book_title':'my favorite book'} 
      if we put this below the dynamic parameter fast api assumes this('mybooks')as dynamic 
      so we have to put this on the above of dynamic parameter funciton  
        """