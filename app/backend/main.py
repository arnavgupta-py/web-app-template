import os
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import models, session
from app.backend import schemas

# Create database tables
models.Base.metadata.create_all(bind=session.engine)

app = FastAPI(title="Web App Template (MVP)")

# Resolve template directory relative to this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(BASE_DIR, "frontend", "templates")
templates = Jinja2Templates(directory=template_dir)

@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(session.get_db)):
    # You can access database models here:
    # items = db.query(models.Item).all()
    
    return templates.TemplateResponse(
        request=request, name="index.html", context={"message": "Welcome to your MVP Template!", "sub_message": "FastAPI + HTMX + Alpine.js + Tailwind CSS"}
    )
