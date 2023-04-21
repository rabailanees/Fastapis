from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas import Registration, ShowUser
from sqlalchemy.orm import Session
from models import User
from database import get_db
from jwt_token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from hashing import Hash


router = APIRouter(
    tags=["Authenticate User"]
)


@router.post("/sign-in")
def user_authentication(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect Password"
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def create_new_user(request: Registration, db: Session = Depends(get_db)):
    new_user = User(
        first_name = request.first_name,
        last_name = request.last_name,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
