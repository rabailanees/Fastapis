from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()


class UserProfile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    profession = Column(String)
    email = Column(String, unique=True,index=True)
    basic_information=relationship("BasicUserInformation",back_populates="profile")
    education=relationship("Educations",back_populates="profile")
    skill=relationship("Skills",back_populates="profile")
    sociallink=relationship("Sociallinks",back_populates="profile")
    
class BasicUserInformation(Base):
    __tablename__="basic_information"
    id= Column(Integer, primary_key=True, index=True)
    phone_number = Column(String)
    date_of_birth = Column(Date)
    job_title = Column(String)
    address = Column(String)
    gender = Column(String)
    description=Column(String)
    profile_id=Column(Integer,ForeignKey("profiles.id"))
    profile=relationship("UserProfile", back_populates="basic_information")
    
class Educations(Base):
    __tablename__="education"
    id=Column(Integer, primary_key=True, index=True)
    title = Column(String)
    degree = Column(String)
    institute = Column(String)
    year = Column(Integer)
    profile_id=Column(Integer,ForeignKey("profiles.id"))
    profile=relationship("UserProfile", back_populates="education")

class Skills(Base):
    __tablename__="skill"
    id=Column(Integer, primary_key=True, index=True)
    skill_title = Column(String)
    percentage = Column(Integer)
    profile_id=Column(Integer,ForeignKey("profiles.id"))
    profile=relationship("UserProfile", back_populates="skill")

class Sociallinks(Base):
    __tablename__="sociallink"
    id=Column(Integer, primary_key=True, index=True)
    facebook = Column(String)
    instagram = Column(String)
    linkedIn = Column(String)
    dribble = Column(String)
    profile_id=Column(Integer,ForeignKey("profiles.id"))
    profile=relationship("UserProfile", back_populates="sociallink")
    
    