from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Event(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    occasion = db.Column(db.String(100))
    location = db.Column(db.String(100))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    subject = db.Column(db.String(100))
    message = db.Column(db.String(1000))
