from database import SessionLocal
import models
from models import Student_model

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def database_retrive(db):
    user_data = db.query(models.Student_model).all()
    response = {}
    out_res = []
    for each in user_data:
        response['id'] = each.id
        response['name'] = each.name
        response['english'] = each.english
        response['maths'] = each.english
        response['physics'] = each.physics
        response['chemistry'] = each.chemistry
        response['biology'] = each.biology
        response['sanskrit'] = each.sanskrit
        response['total'] = each.total
        response['grade'] = each.grade
        response['chance_given'] = each.chance_given
        out_res.append(response)
    return out_res

def database_retrive_one(id,db):
    user_data = db.query(Student_model).filter(Student_model.id == id).first()
    response = {}
    response['id'] = user_data.id
    response['name'] = user_data.name
    response['english'] = user_data.english
    response['math'] = user_data.math
    response['physics'] = user_data.physics
    response['chemistry'] = user_data.chemistry
    response['biology'] = user_data.biology
    response['sanskrit'] = user_data.sanskrit
    response['total'] = user_data.total
    response['grade'] = user_data.grade
    response['chance_given'] = user_data.chance_given
    return response

def database_update(id, name, english, math, physics, chemistry, biology,sanskrit,total, grade, chance_given,db):
    update_obj = db.query(Student_model).filter(Student_model.id == id).first()
    update_obj.name = name
    update_obj.english = english
    update_obj.maths = math
    update_obj.physics = physics
    update_obj.chemistry = chemistry
    update_obj.biology = biology
    update_obj.sanskrit = sanskrit
    update_obj.total = total
    update_obj.grade = grade
    update_obj.chance_given = chance_given
    db.add(update_obj)
    db.commit()
    db.refresh(update_obj)
    return "data updated successfully"

def database_delete(id,db):
    if db.query(Student_model).filter(Student_model.id == id).delete():
        db.commit()
        return "success"
    else:
        return 'user not found'


