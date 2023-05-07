from fastapi import FastAPI
from database import Base, engine
from user_router import router as user
from auth_router import router as auth
from basic_information_routers import router as info
from education_routers import router as edu
from skills_routers import router as skl
from social_links_routers import router as slinks


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(auth)
app.include_router(user)
app.include_router(info)
app.include_router(edu)
app.include_router(skl)
app.include_router(slinks)

