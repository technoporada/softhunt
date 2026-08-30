from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import os

from app import models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "templates")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATE_DIR)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(request: Request):
    games = [
        {"title": "Mock Game 1", "url": "https://example.com/game1"},
        {"title": "Mock Game 2", "url": "https://example.com/game2"},
    ]
    return templates.TemplateResponse("index.html", {"request": request, "games": games})
