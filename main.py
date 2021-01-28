from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app import db
from models import Event

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/event')
@login_required
def event():
    return render_template('event.html')

@main.route('/event_overview', methods=['POST'])
@login_required
def event_overview():

    # create new event
    new_event = Event(
        occasion=request.form["occasion"],
        location=request.form["location"],
        date=request.form["date"],
        time=request.form["time"],
        subject=request.form["subject"],
        message=request.form["message"],
    )

    return render_template('event_overview.html', event=new_event)
