from fastapi import FastAPI
from database import Base, engine
from user_router import router as user
from auth_router import router as auth


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(auth)
app.include_router(user)
