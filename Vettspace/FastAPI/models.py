# from sqlalchemy import Column, Integer, String
# from database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String, unique=True, index=True)
#     password = Column(String)

from sqlalchemy import create_engine,ForeignKey,Column,Integer,String,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Date
from database import Base
from sqlalchemy.orm import relationship


class ProfileModel(Base):
    __tablename__="Profile"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    profession=Column(String)
    email_address=Column(String,unique=True)
    password=Column(String)
    BasicInformation= relationship("BasicInformationModel", back_populates="profile")
    Education=relationship("EducationModel", back_populates="profile")
    Skill=relationship("SkillModel", back_populates="profile")
    SocialLinks=relationship("SocialLinksModel", back_populates="profile")
    
    
class BasicInformationModel(Base):
    __tablename__="BasicInformation"
    id=Column(Integer,primary_key=True,index=True)
    phone_number=Column(Integer)
    date_of_birth=Column(Date)
    job_title=Column(String)
    address=Column(String)
    gender=Column(String)
    description=Column(String)
    profile_id = Column(Integer, ForeignKey("Profile.id"))
    profile = relationship("ProfileModel", back_populates="BasicInformation")
    
    
class EducationModel(Base):
    __tablename__="Education"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    degree=Column(String)
    institute=Column(String)
    year=Column(Integer)
    profile_id = Column(Integer, ForeignKey("Profile.id"))
    profile = relationship("ProfileModel", back_populates="Education")
    
    
class SkillModel(Base):
    __tablename__="Skill"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    percentage=Column(Integer)
    profile_id = Column(Integer, ForeignKey("Profile.id"))
    profile = relationship("ProfileModel", back_populates="Skill")
    
class SocialLinksModel(Base):
    __tablename__="SocialLinks"
    id=Column(Integer,primary_key=True,index=True)
    facebook=Column(String)
    instagram=Column(String)
    linkedIn=Column(String)
    dribble=Column(String)
    profile_id = Column(Integer, ForeignKey("Profile.id"))
    profile = relationship("ProfileModel", back_populates="SocialLinks")
    