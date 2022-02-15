from pydantic import BaseModel

class Student(BaseModel):
    id : int
    name:str
    english:int
    math:int
    physics:int
    chemistry:int
    biology:int
    sanskrit:int
    
    

class StudentResponse(BaseModel):
    id : int
    english:int
    math:int
    physics:int
    chemistry:int
    biology:int
    sanskrit:int
    total : int
    grade : str
    chance_given : int


    class Config:
        orm_mode = True
