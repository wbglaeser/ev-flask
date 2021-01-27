from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

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
    print(request.form)
    print(request.form["occasion"])
    print(request.form["location"])
    print(request.form["date"])
    print(request.form["time"])
    return render_template('event_overview.html')
