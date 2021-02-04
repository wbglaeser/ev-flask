from flask_login import UserMixin
from database import db

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    events = db.relationship("Event")

class Event(UserMixin, db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    occasion = db.Column(db.String(100))
    location = db.Column(db.String(100))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    subject = db.Column(db.String(100))
    message = db.Column(db.String(1000))
    token = db.Column(db.String(100))
