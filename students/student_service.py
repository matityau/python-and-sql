from fastapi import APIRouter,HTTPException
import student_repository as s
from pydantic import BaseModel
from typing import Optional


router = APIRouter()

class Student(BaseModel):
    name:str
    age: int
    course:str
    email:Optional[str]
    status:str = "active"


@router.get("")
def all_students():
    try:
        all = s.all_students()
        if not all:
            return []
        return all
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}")
def get_by_id(id:int):
    try:
        student = s.get_student_by_id(id)
        if not student:
            raise HTTPException(status_code=404,detail=f"Students {id} not found")
        return student
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("",status_code=201)
def create_student(new:Student):
    try:
        dict_data = new.model_dump()#ביצירה של הטבלה ההגדה הי אUNIQE EMAIL
        new_id = s.add_student(dict_data)#ID הוא AUTO INCREMENT ככה שתמיד הןא יהיה יחודי ןלא כפןל
        return{"message":f"students {new_id} create succsesfuly"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.patch("/{id}")
def rename_student(id:int,body:dict):
    try:
        succses = s.update_student_name(id,body["name"])
        if not succses:
            raise HTTPException(status_code=400,detail="bad reqest")
        return {"message":f"Student {id} rename to {body['name']}"}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
