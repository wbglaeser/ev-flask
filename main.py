from datetime import datetime

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app import db
from models import Event

main = Blueprint('main', __name__)
pending_events = []

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():

    events = Event.query.filter_by(user_id=current_user.id).all()

    return render_template('profile.html', name=current_user.name, events=events)

@main.route('/event')
@login_required
def event():
    return render_template('event.html')

@main.route('/event_overview', methods=['POST'])
@login_required
def event_overview():

    # create new event
    new_event = Event(
        user_id=current_user.id,
        occasion=request.form["occasion"],
        location=request.form["location"],
        date=datetime.strptime(request.form["date"], '%Y-%m-%d').date(),
        time=datetime.strptime(request.form["time"], '%M:%H').time(),
        subject=request.form["subject"],
        message=request.form["message"],
    )
    pending_events.append(new_event)
    
    return render_template('event_overview.html', event=new_event)

@main.route('/event_confirmation', methods=['POST'])
@login_required
def event_confirmation():
    
    new_event = pending_events[0]
    db.session.add(new_event)
    db.session.commit()

    return render_template('event_confirmation.html', event=new_event)
