
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException,status
from pydantic import BaseModel, Field
import models
import pandas as pd
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
# db = SessionLocal()
# print(db)    checking db session


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
class InternData(BaseModel):
    ID : str
    Name : str 
    DOB_as_per_certificate: str
    DOB_Original : Optional[str]
    Fang_Mail_Id : str
    Personal_Email_Id :str
    Contact : Optional[int]
    Education : str
    Branch : Optional[str]
    College : str
    Year_of_Passing_Out : int
class EmpData(BaseModel):
    Fang_Email_Id :str
    Personal_Email_Id :str
    DOB_as_per_certificate: str
    DOB_Original :str
    Contact : Optional[int]
    Experience :str
    Education :str
    Branch : Optional[str]  
    Passed_out_Year :int
    College : str
    Current_Employer: str
    Role : str
    Previous_Employers : str
class TrainingData(BaseModel):
    ID : int
    Name : str 
    DOB_as_per_certificate: str
    DOB_Original : Optional[int]
    Fang_Mail_Id : str
    Personal_Email_Id :str
    Contact : Optional[int]
    Education : str
    Branch : Optional[str]
    College : str
    Year_of_Passing_Out : int



# class SearchRequest(BaseModel):
#     search_data: str = Field(description= "enter data to search ")

@app.get("/searchdata")
async def get_searched_data( searchdata:str , db: Session = Depends(get_db)):
    
    query1 =  db.query(models.InternsInfo).filter( \
        (models.InternsInfo.Name.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.DOB_as_per_certificate.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.ID.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.DOB_Original.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.Fang_Mail_Id.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.Personal_Email_Id.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.Contact.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.Education.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.Branch.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.College.ilike(f'%{searchdata}%')) |
        (models.InternsInfo.Year_of_Passing_Out.ilike(f'%{searchdata}%')) 
        ).all()
    query2 =  db.query(models.EmpInfo).filter( \
        (models.EmpInfo.Fang_Email_Id.ilike(f'%{searchdata}%')) |
          (models.EmpInfo.Personal_Email_Id.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.DOB_as_per_certificate.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.DOB_Original.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Contact.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Experience.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Education.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Branch.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Passed_out_Year.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.College.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Current_Employer.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Role.ilike(f'%{searchdata}%')) |
            (models.EmpInfo.Previous_Employers.ilike(f'%{searchdata}%')) 
            ).all()
    query3 =  db.query(models.Training_and_Placement_Info).filter( \
        (models.Training_and_Placement_Info.Name.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.DOB_as_per_certificate.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.ID.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.DOB_Original.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.Fang_Mail_Id.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.Personal_Email_Id.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.Contact.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.Education.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.Branch.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.College.ilike(f'%{searchdata}%')) |
        (models.Training_and_Placement_Info.Year_of_Passing_Out.ilike(f'%{searchdata}%')) 
        ).all()
    if len(query1)!=0 and len(query2)!=0 and  len(query3)!=0:
        return  {"data":query1+query2+query3, "message":"success", "status":status.HTTP_200_OK }
    elif len(query1)!=0 and len(query2)!=0:
        return  {"data":query1+query2 ,"message":"success", "status":status.HTTP_200_OK }
    elif len(query1)!=0 and len(query3)!=0:
        return {"data":query1+query3,"message":"success", "status":status.HTTP_200_OK }
    elif len(query2)!=0 and len(query3)!=0:
        return {"data":query2+query3,"message":"success", "status":status.HTTP_200_OK }
    elif(len(query1)!=0):
        return {"data": query1,"message":"success", "status":status.HTTP_200_OK }
    elif(len(query2)!=0):
        return { "data": query2,"message":"success", "status":status.HTTP_200_OK }
    elif(len(query3)!=0):
        return {"data": query3,"message":"success", "status":status.HTTP_200_OK }
    return {"message":"Failed", "status":status.HTTP_404_NOT_FOUND }

   # result = pd.read_sql(query,)
    #return result
    
    # output = db.query(models.EmpInfo).filter(models.EmpInfo.College==searchdata).all()
    # return output

@app.get("/employees")
async def get_employee_data(  db: Session = Depends(get_db)):
    return  {"data" :db.query(models.EmpInfo).all(),"message":"success", "status":status.HTTP_200_OK }

@app.get("/interns")
async def get_interns_data(  db: Session = Depends(get_db)):
    return   {"data" :db.query(models.InternsInfo).all(),"message":"success", "status":status.HTTP_200_OK }

@app.get("/training")
async def get_training_data(  db: Session = Depends(get_db)):
     return   {"data" :db.query(models.Training_and_Placement_Info).all(),"message":"success", "status":status.HTTP_200_OK }

@app.get("/search-data/{id}")
def search_data_based_on_employee_id(id: int, db: Session= Depends(get_db)):
    query1 = db.query(models.InternsInfo).filter(models.InternsInfo.ID == id).first()
    query2 = db.query(models.Training_and_Placement_Info).filter(models.Training_and_Placement_Info.ID==id).first()
    print(query1, query2)
    if query1 != None:
        return {"data" :query1,"message":"success", "status":status.HTTP_200_OK }
    elif query2 != None:
        return {"data" :query2,"message":"success", "status":status.HTTP_200_OK }
    return {"message":"Failed", "status":status.HTTP_404_NOT_FOUND }


@app.put("/update-data/{id}")
def update_data_based_on_employee_id(id: int ,interndata: InternData, db: Session = Depends(get_db)):
    intern_model = db.query(models.InternsInfo).filter(models.InternsInfo.ID == id).first()
    
    print(intern_model)
    if intern_model is not None:
        intern_model.Branch = interndata.Branch
        intern_model.College = interndata.College
        intern_model.Contact = interndata.Contact
        intern_model.Personal_Email_Id = interndata.Personal_Email_Id
        intern_model.DOB_as_per_certificate = interndata.DOB_as_per_certificate
        intern_model.DOB_Original = interndata.DOB_Original
        intern_model.Education = interndata.Education
        intern_model.Name= interndata.Name
        intern_model.Fang_Mail_Id = interndata.Fang_Mail_Id
        intern_model.Year_of_Passing_Out = interndata.Year_of_Passing_Out

        db.add(intern_model)
    
        db.commit()
        return {"message":"success", "status":status.HTTP_200_OK}
    return {"message":"success", "status":status.HTTP_404_NOT_FOUND}
    


    




