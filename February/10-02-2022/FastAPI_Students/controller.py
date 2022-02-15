from fastapi import FastAPI, Depends
import uvicorn
from schemas import Student, StudentResponse
from sqlalchemy.orm import Session
from utils import get_db
from service import service_insert,service_retrive, \
    service_retrive_one, service_update,service_delete
import models
from database import engine
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/insert',status_code=201 )
def insert_data(st : Student, db : Session = Depends(get_db)):
    total = st.english + st.math + st.physics + st.chemistry + st.biology + st.sanskrit
    avg = (total/600) * 100
    chance_given = 1
    if(avg >= 90):
        grade ="DISTINCTION"
    elif(70 <= avg < 90):
        grade = "GOLD MEDAL"
    elif(30 <= avg < 70):
        grade = "PASS"
    elif(30 < avg ):
        grad = "FAIL"
    else:
        grade = "FAIL"
        chance_given = 0
    new_student = models.Student_model( id = st.id,
                                      name=st.name,
                                      english = st.english,
                                      math = st.math,
                                      physics = st.physics,
                                      chemistry = st.chemistry,
                                      biology = st.biology,
                                      sanskrit = st.sanskrit,
                                      total = total,
                                      grade = grade,
                                      chance_given = chance_given
                                      )

    return service_insert(new_student,db)


@app.get('/retrieve',status_code=200, response_model = List[StudentResponse])
def retrieve_data(db : Session = Depends(get_db)):
    return service_retrive(db)

@app.get('/retrieve/{id}',status_code=200, response_model = StudentResponse)
def retrieve_data(id:int, db : Session = Depends(get_db)):
    return service_retrive_one(id,db)

@app.put('/update')
def update_data(st : Student, db : Session = Depends(get_db)):
    id = st.id
    name = st.name
    english = st.english
    math = st.math
    physics = st.physics
    chemistry = st.chemistry
    biology = st.biology
    sanskrit = st.sanskrit
    total = english + math + physics + chemistry + biology + sanskrit
    avg = (total/600) * 100
    chance_given = 1
    if(avg >= 90):
        grade ="DISTINCTION"
    elif(70 <= avg < 90):
        grade = "GOLD MEDAL"
    elif(30 <= avg < 70):
        grade = "PASS"
    elif(30 < avg ):
        grad = "FAIL"
    else:
        grade = "FAIL"
        chance_given = 0
    
    #chance_given = st.chance_given
    
    return service_update(id,name, english,math,physics,chemistry, biology, sanskrit, total, grade, chance_given, db)

@app.delete('/delete/{id}')
def delete_data(id:int,db : Session = Depends(get_db)):
    return service_delete(id,db)


if __name__ == '__main__':
    uvicorn.run(app)