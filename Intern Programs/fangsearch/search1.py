
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Body 
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
        db = SessionLocal()#to contact with database
        yield db
    finally:
        db.close()


# class SearchRequest(BaseModel):
#     search_data: str = Field(description= "enter data to search ")

@app.get("/")
async def get_searched_data( searchdata :str, db: Session = Depends(get_db)):
    
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
        return query1+query2+query3
    elif len(query1)!=0 and len(query2)!=0:
        return query1+query2
    elif len(query1)!=0 and len(query3)!=0:
        return query1+query3
    elif len(query2)!=0 and len(query3)!=0:
        return query2+query3
    elif(len(query1)!=0):
        return query1
    elif(len(query2)!=0):
        return query2
    elif(len(query3)!=0):
        return query3

   # result = pd.read_sql(query,)
    #return result
    
    # output = db.query(models.EmpInfo).filter(models.EmpInfo.College==searchdata).all()
    # return output
null=''
@app.get("/employees")
async def get_employee_data(  db: Session = Depends(get_db)):
    return db.query(models.EmpInfo).all()

@app.get("/interns")
async def get_interns_data(  db: Session = Depends(get_db)):
    return db.query(models.InternsInfo).all()
@app.get("/training")
async def get_training_data(  db: Session = Depends(get_db)):
     return db.query(models.Training_and_Placement_Info).all()

"""

excel_file = pd.ExcelFile("fangsearch.xlsx")

# Define the sheet names
sheet_names = ["interns_info", "emp_info", "training_and_placement_info"]


def search_name_in_sheet(sheet_name, name):
    # Read the sheet into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Search for the name in the DataFrame
    result = df.loc[df['Name'] == name] | df.loc[df['Fang_Email_Id'] == name]

    # Return the result as a dictionary
    return result


@app.get("/search/{name}")
def search_name(name: str):
    results = {}

    for sheet_name in sheet_names:
        results[sheet_name] = search_name_in_sheet(sheet_name, name)

    return results
"""
@app.get("/excel_data")
def get_excel_data(column_name: str):
    file_path = "fangsearch.xlsx"
    sheet_names = ["interns_info", "emp_info", "training_and_placement_info"]  # Replace with your actual sheet names

    data = {}

    for sheet_name in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        column_data = df[column_name].tolist()
        data[sheet_name] = column_data

    return data
