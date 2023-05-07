from fastapi import APIRouter, Depends, status, HTTPException
from schemas import SocialLinks
from sqlalchemy.orm import Session
from models import SocialLinksModel
from database import get_db
from oauth2 import get_current_user


router = APIRouter(
    prefix="/links",
    tags=["Social Links"]
)


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=SocialLinks)
def create_social_links(social_links: SocialLinks, db: Session = Depends(get_db)):
    new_social_link = SocialLinksModel(
        id=social_links.id,
        facebook=social_links.facebook,
        instagram=social_links.instagram,
        linkedIn=social_links.linkedIn,
        dribble=social_links.dribble,
        profile_id=social_links.profile_id
    )
    db.add(new_social_link)
    db.commit()
    db.refresh(new_social_link)
    return new_social_link

@router.get('/')
def get_social_links(db: Session = Depends(get_db)):
    social_links = db.query(SocialLinksModel).all()
    return social_links