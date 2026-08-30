from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OfferBase(BaseModel):
    source: Optional[str] = None
    title: str
    description: Optional[str] = None
    url: str
    expires: Optional[datetime] = None
    tags: Optional[str] = None
    requires_login: Optional[bool] = False
    has_captcha: Optional[bool] = False
    has_adfly: Optional[bool] = False
    notes: Optional[str] = ""
    added: Optional[datetime] = None

class OfferCreate(OfferBase):
    pass

class OfferUpdate(BaseModel):
    source: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    expires: Optional[datetime] = None
    tags: Optional[str] = None
    requires_login: Optional[bool] = None
    has_captcha: Optional[bool] = None
    has_adfly: Optional[bool] = None
    notes: Optional[str] = None

class Offer(OfferBase):
    id: int

    class Config:
        orm_mode = True  # Pydantic v1 (jeśli masz v2, to from_attributes=True)
