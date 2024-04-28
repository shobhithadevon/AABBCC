from sqlalchemy.orm import session
from models import School
from schemas import SchoolSchema

#get all book data
def get_school(db:session,skip:int=0,limit:int=200):
    return db.query(School).offset(skip).limit(limit).all()

#get by id bok data
def get_school_by_stud_id(db:session,school_stud_id: int):
    return db.query(School).filter(School.stud_id == school_stud_id).first()
#Crete book dta
def create_school(db:session, school: SchoolSchema):
    _school = School(stud_name=school.stud_name,stud_class=school.stud_class,stud_age=school.stud_age)
    db.add(_school)
    db.commit()
    db.refresh(_school)
    return _school
#remove book data
def remove_school(db:session,school_stud_id:int):
    _school = get_school_by_stud_id(db=db, school_stud_id= school_stud_id)
    db.delete (_school)
    db.commit()
#Update book data
def update_school(db:session,stud_id:int,stud_name:str,stud_class:str,stud_age:int):
    _school = get_school_by_stud_id(db=db,school_stud_id= stud_id)
    _school.stud_name = stud_name
    _school.stud_class = stud_class
    _school.stud_age = stud_age
    db.commit()
    db.refresh(_school)
    return _school





