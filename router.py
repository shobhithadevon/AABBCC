from fastapi import APIRouter,HTTPException,Path,Depends
from configparser import SessionLocal
from sqlalchemy.orm import Session
from schemas import SchoolSchema,requestSchool,Response
import AABBCC.crud as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create (request:requestSchool,db:Session=Depends(get_db)):
    crud.create_school(db,school=request.parameter)
    return Response(code=200,status="OK",message = "Data added successfully").dict(exclude_none=True)

@router.get("/")
async def get(db: Session = Depends(get_db)):
    _school = crud.get_school(db,0,100)
    return Response(code=200, staus='OK',message ='Success update Data',result=_school).dict(exclude_none=True)

@router.get("/{id}")
async def get_school_by_stud_id(stud_id: int,db: Session = Depends(get_db)):
    _school = crud.get_school_by_stud_id(db,stud_id)
    return Response(code=200,status="OK",message = "Success get Data",result=_school).dict(exclude_none=True)

@router.post("\update")
async def update_school(request:requestSchool,db:Session = Depends(get_db)):
    _school = crud.update_school(db,school_stud_id=request.parameter.stud_id, 
                                 stud_name=request.parameter.stud_name, stud_class=request.parameter.stud_class,
                                stud_age=request.parameter.stud_age)
    return Response(code=200, staus='OK',message ='Success update Data',result=_school).dict(exclude_none=True)

@router.delete("/{id}")
async def delete(id:int,db:Session = Depends(get_db)):
    crud.remove_school(db,school_stud_id= id)
    return Response(code=200, staus='OK',message ='Success delete Data').dict(exclude_none=True)












