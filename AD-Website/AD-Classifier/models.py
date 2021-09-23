
from app.py import db

def init_db():
    db.create_all()