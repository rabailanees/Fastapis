from fastapi import FastAPI, Depends,status, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
import shutil
from database import Base, engine, get_db
from schemas import User,Basic_Information,Education,Skill,SocialLinks
from models import *



app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get('/profiles', response_model=List[User])
def get_profiles(db: Session = Depends(get_db)):
    profiles = db.query(UserProfile).all()
    return profiles

@app.post('/profiles', response_model=User)
def create_profile(profile: User, db: Session = Depends(get_db)):
    new_profile = UserProfile(
        name=profile.name,
        profession=profile.profession,
        email=profile.email,
    )
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@app.get('/basic_info', response_model=List[Basic_Information])
def get_basic_information(db: Session = Depends(get_db)):
    basicinfo = db.query(BasicUserInformation).all()
    return basicinfo

@app.post('/basic_info',response_model=Basic_Information)
def create_basic_information(basic_info: Basic_Information, db: Session = Depends(get_db)):
    new_basic_info = BasicUserInformation(
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

@app.get('/education',response_model=List[Education])
def get_education(db: Session = Depends(get_db)):
    educations = db.query(Educations).all()
    return educations


@app.post('/education',response_model=Education)
def create_education(education: Education, db: Session = Depends(get_db)):
    new_education = Educations(
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

@app.get('/skill',response_model=List[Skill])
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skills).all()
    return skills


@app.post('/skill',response_model=Skill)
def create_skill(skill: Skill, db: Session = Depends(get_db)):
    new_skill =Skills(
        id=skill.id,
        skill_title=skill.skill_title,
        percentage=skill.percentage,
        profile_id=skill.profile_id
    )
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill

@app.get('/socialLinks',response_model=List[SocialLinks])
def get_social_links(db: Session = Depends(get_db)):
    social_links = db.query(Sociallinks).all()
    return social_links


@app.post('/socialLinks',response_model=SocialLinks)
def create_social_links(social_links: SocialLinks, db: Session = Depends(get_db)):
    new_social_link = Sociallinks(
        id=social_links.id,
        facebook=social_links.facebook,
        instagram=social_links.instagram,
        linkedIn=social_links.linkedIn,
        dribble=social_links.dribble,
    )
    db.add(new_social_link)
    db.commit()
    db.refresh(new_social_link)
    return new_social_link

@app.get("/{id}", response_model=User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter(UserProfile.id == id).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"User of ID {id} is not found."
        )
    return user    
