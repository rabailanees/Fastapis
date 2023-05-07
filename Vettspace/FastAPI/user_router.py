from fastapi import APIRouter, Depends, status, HTTPException
from schemas import ProfileSchema
from sqlalchemy.orm import Session
from models import ProfileModel
from database import get_db
from oauth2 import get_current_user


router = APIRouter(
    prefix="/user",
    tags=["User Details"]
)


@router.get("/")
def get_all_users(db: Session = Depends(get_db), current_user: ProfileSchema = Depends(get_current_user)):
    users = db.query(ProfileModel).all()
    return users


@router.get("/{id}", response_model=ProfileSchema)
def get_user(id: int, db: Session = Depends(get_db), current_user: ProfileSchema = Depends(get_current_user)):
    user = db.query(ProfileModel).filter(ProfileModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"User of ID {id} is not found."
        )
    return user


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(id: int, request: ProfileSchema, db: Session = Depends(get_db), current_user: ProfileSchema = Depends(get_current_user)):
    user = db.query(ProfileModel).filter(ProfileModel.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"User of id {id} is not found"
        )
    update_data = request.dict(exclude_unset=True)
    user.update(update_data)
    db.commit()
    return {"detail": f"User with id {id} has been updated successfully."}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), current_user: ProfileSchema = Depends(get_current_user)):
    user = db.query(ProfileModel).filter(ProfileModel.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"User of id {id} is not found"
        )
    user.delete(synchronize_session=False)
    db.commit()
    return


# @router.put("/updatePassword")
# def update_password(request: PasswordUpdate, db: Session = Depends(get_db)):
#     if request.status == True:
#         user = db.query(User).filter(User.email == request.email).first()
#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")
#         user.password = request.password
#         db.add(user)
#         db.commit()
#         return {"message": "Password updated successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="User not found")
