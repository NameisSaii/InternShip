from fastapi import FastAPI
app=FastAPI()
books=[
        {"title":"sai","author":"saikumar","category":'science'},
        {"title":"sai","author":"saikumar","category":'histor'},
        {"title":"sai","author":"saikumar","category":'civics'},
        {"title":"sai","author":"saikumar","category":'maths'},
        {"title":"sai","author":"saikumar","category":'science'}
]
@app.get("/")
async def first_api():
    return books
#URL : 127.0.0.1:8000/docs to get all the API endpoints we use docs after the url genereated by terminal

