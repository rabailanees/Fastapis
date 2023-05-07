from fastapi import APIRouter, Depends, status, HTTPException
from schemas import Skill
from sqlalchemy.orm import Session
from models import SkillModel
from database import get_db
from oauth2 import get_current_user


router = APIRouter(
    prefix="/sk",
    tags=["Skill"]
)

@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=Skill)


def create_skill(skill: Skill, db: Session = Depends(get_db)):
    new_skill = SkillModel(
        id=skill.id,
        title=skill.title,
        percentage=skill.percentage,
        profile_id=skill.profile_id  
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


@router.get("/")
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(SkillModel).all()
    return skills
