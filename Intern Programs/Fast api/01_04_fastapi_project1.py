from fastapi import FastAPI
app= FastAPI()
data = {
    "lead_id": 'LD123',
    "parties": [
       {
           "UID": 123123,
           "CustName": "JOhn Doe",
       }]}
@app.get("/api-endpoint")
async def first_api():
    return data
#to run it 'uvicorn fastapi_project1:app --reload