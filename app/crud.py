from sqlalchemy.orm import Session
from app import models, schemas

def get_offer_by_url(db: Session, url: str):
    return db.query(models.Offer).filter(models.Offer.url == url).first()

def create_offer(db: Session, offer: schemas.OfferCreate):
    db_offer = models.Offer(
        title=offer.title,
        url=offer.url,
        source=offer.source,
        description=offer.description,
        expires=offer.expires,
        tags=offer.tags,
        requires_login=offer.requires_login,
        has_captcha=offer.has_captcha,
        has_adfly=offer.has_adfly,
        notes=offer.notes,
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer
