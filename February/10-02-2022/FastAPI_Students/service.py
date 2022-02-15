from database import insert_data
from utils import database_retrive,\
     database_retrive_one,database_update,database_delete
def service_insert(new_student,db):
    return insert_data(new_student,db)
   
def service_retrive(db):
    return database_retrive(db)

def service_retrive_one(id,db):
    return database_retrive_one(id,db)

def service_update(id, name, english, math, physics, chemistry, biology,sanskrit, total, grade, chance_given, db):
    return database_update(id, name, english, math, physics, chemistry, biology,sanskrit,total, grade, chance_given, db)
    

def service_delete(id,db):
    return database_delete(id,db)
