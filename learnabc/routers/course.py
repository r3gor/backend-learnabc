from hashlib import new
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
# from ..repository import blog

router = APIRouter(
    prefix="/course",
    tags=['Course']
)

get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_course(
        request: schemas.RequestCourse,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)):

    new_course = models.Course(name=request.name, user_id=current_user.id)
    db.add(new_course)
    db.commit()
    return "created"


@router.get('/', response_model=List[schemas.ShowCourse], status_code=status.HTTP_200_OK)
def all_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses


@router.get('/{id}', response_model=schemas.ShowCourse, status_code=status.HTTP_200_OK)
def get_course(
        id: int,
        db: Session = Depends(get_db)):
    course = db.query(models.Course).filter_by(id=id).first()
    return course


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(
        id: int,
        db: Session = Depends(get_db)):
    course = db.query(models.Course).filter_by(id=id)
    if not course.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    course.delete(synchronize_session=False)
    db.commit()
    return "deleted"