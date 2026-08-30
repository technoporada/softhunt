from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from app.database import Base
import datetime

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    url = Column(String, unique=True, nullable=False, index=True)
    expires = Column(DateTime, nullable=True)
    tags = Column(String, nullable=True)
    requires_login = Column(Boolean, default=False)
    has_captcha = Column(Boolean, default=False)
    has_adfly = Column(Boolean, default=False)
    notes = Column(Text, default="")
    added = Column(DateTime, default=datetime.datetime.utcnow)
