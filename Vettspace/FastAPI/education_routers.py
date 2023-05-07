from fastapi import APIRouter, Depends, status, HTTPException
from schemas import ProfileSchema,BasicUserInformation,Education
from sqlalchemy.orm import Session
from models import ProfileModel,BasicInformationModel,EducationModel
from database import get_db
from oauth2 import get_current_user


router = APIRouter(
    prefix="/edu",
    tags=["Education"]
)

@router.post('/signup',status_code=status.HTTP_201_CREATED,response_model=Education)
def create_education(education: Education, db: Session = Depends(get_db)):
    new_education = EducationModel(
        id=education.id,
        title=education.title,
        degree=education.degree,
        institute=education.institute,
        year=education.year,
        profile_id=education.profile_id  
    )
    db.add(new_education)
    db.commit()
    db.refresh(new_education)
    return new_education



@router.get("/")
def get_education(db: Session = Depends(get_db)):
    educations = db.query(EducationModel).all()
    return educations
