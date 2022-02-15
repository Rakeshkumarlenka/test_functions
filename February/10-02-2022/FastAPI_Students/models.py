from xmlrpc.client import Boolean
from database import Base
from sqlalchemy import Column, Integer, String


class Student_model(Base):
    __tablename__ = 'Student_Results'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    english = Column(Integer)
    math = Column(Integer)
    physics = Column(Integer)
    chemistry = Column(Integer)
    biology = Column(Integer)
    sanskrit = Column(Integer)
    total = Column(Integer)
    grade = Column(String)
    chance_given = Column(Integer)
