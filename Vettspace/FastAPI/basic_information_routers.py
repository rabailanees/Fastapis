from fastapi import APIRouter, Depends, status, HTTPException
from schemas import ProfileSchema,BasicUserInformation
from sqlalchemy.orm import Session
from models import ProfileModel,BasicInformationModel
from database import get_db
from oauth2 import get_current_user


router = APIRouter(
    prefix="/info",
    tags=["Basic Information"]
)

@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=BasicUserInformation)
def create_basic_information(basic_info: BasicUserInformation, db: Session = Depends(get_db)):
    new_basic_info = BasicInformationModel(
        id=basic_info.id,
        date_of_birth=basic_info.date_of_birth,
        phone_number=basic_info.phone_number,
        job_title=basic_info.job_title,
        address=basic_info.address,
        gender=basic_info.gender,
        description=basic_info.description, 
        profile_id=basic_info.profile_id 
    )
    db.add(new_basic_info)
    db.commit()
    db.refresh(new_basic_info)
    return new_basic_info


@router.get("/")

def get_basic_information(db: Session = Depends(get_db)):
    basic_info = db.query(BasicInformationModel).all()
    return basic_info