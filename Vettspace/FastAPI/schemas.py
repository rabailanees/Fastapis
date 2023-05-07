# from pydantic import BaseModel
# from typing import Optional, List


# class Registration(BaseModel):
#     first_name: str
#     last_name: str
#     email: str
#     password: str


# class RegistrationUpdate(BaseModel):
#     first_name: Optional[str]
#     last_name: Optional[str]
#     email: Optional[str]
#     password: Optional[str]


# class ShowUser(BaseModel):
#     first_name: str
#     last_name: str
#     email: str
#     class Config():
#         orm_mode = True



# class PasswordUpdate(BaseModel):
#     email: str
#     password: str
#     status: bool = False

from typing import List, Union, Optional
from datetime import date
from pydantic import BaseModel

class ProfileSchema(BaseModel):
    id: int
    name: str
    profession: str
    email_address: str
    password:str
    class Config:
        orm_mode = True

class BasicUserInformation(BaseModel):
    id: int
    date_of_birth: date
    phone_number: int
    job_title: str
    address: str
    gender: str
    description: str
    profile_id: int

    class Config:
        orm_mode = True

class Education(BaseModel):
    id: int
    title: str
    degree: str
    institute: str
    year: int
    profile_id: int
    class Config:
        orm_mode = True
        
class Skill(BaseModel):
    id: int
    title: str
    percentage: int
    profile_id: int
    class Config:
        orm_mode = True
        
class SocialLinks(BaseModel):
    id: int
    facebook: str
    instagram: str
    linkedIn: str
    dribble: str
    profile_id: int
    class Config:
        orm_mode = True

    
     


class Login(BaseModel):
     email: str
     password: str


class Token(BaseModel):
     access_token: str
     token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
