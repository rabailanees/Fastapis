from typing import List, Union, Optional
from datetime import date
from pydantic import BaseModel,Field
from sqlalchemy_utils import URLType

class User(BaseModel):
    name: str
    profession: str
    email: str
    class Config:
        orm_mode = True
class Basic_Information(BaseModel):
    id:int
    date_of_birth: date
    phone_number: str
    job_title: str
    address: str
    gender: str
    description: str
    profile_id:int
    class Config:
        orm_mode = True
class Education(BaseModel):
    id:int
    title: str
    degree: str
    institute: str
    year: int
    profile_id:int
    class Config:
        orm_mode = True
class Skill(BaseModel):
    id:int
    skill_title: str
    percentage: int
    profile_id:int
    class Config:
        orm_mode = True
class SocialLinks(BaseModel):
    id:int
    facebook: str
    instagram: str
    linkedIn: str
    dribble: str
    class Config:
        orm_mode = True


    
