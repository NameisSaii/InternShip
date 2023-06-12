# models is a way for SQL alchemy to be able to understand what kind of database tables we are going
#to be creating within our database in the future.
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, TIMESTAMP,REAL
from database import Base
from sqlalchemy.orm import relationship


class InternsInfo(Base):
    __tablename__ = "interns_info"
    ID = Column(String, primary_key=True, index=True)
    Name = Column(String)
    DOB_as_per_certificate = Column(String)
    DOB_Original = Column(String)
    Fang_Mail_Id = Column(String)
    Personal_Email_Id = Column(String)
    Contact = Column(REAL)
    Education = Column(String)
    Branch = Column(String)
    College = Column(String)
    Year_of_Passing_Out = Column(Integer)



class EmpInfo(Base):
    __tablename__ = "emp_info"
    Fang_Email_Id = Column(String,primary_key = True)
    Personal_Email_Id = Column(String)
    DOB_as_per_certificate = Column(String)
    DOB_Original = Column(String)
    Contact = Column(REAL)
    Experience = Column(String)
    Education = Column(String)
    Branch = Column(String)
  
    
    Passed_out_Year = Column(Integer)
    College = Column(String)
    Current_Employer = Column(String)
    Role =Column(String)
    Previous_Employers =Column(String)

class Training_and_Placement_Info(Base):
    __tablename__ = "training_and_placement_info"
    ID = Column(REAL)
    Name = Column(String)
    DOB_as_per_certificate = Column(String)
    DOB_Original = Column(REAL)
    Fang_Mail_Id = Column(String,primary_key=True)
    Personal_Email_Id = Column(String)
    Contact = Column(REAL)
    Education = Column(String)
    Branch = Column(String)
    College = Column(String)
    Year_of_Passing_Out = Column(Integer)










    
    
    