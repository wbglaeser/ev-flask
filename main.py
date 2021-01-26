from flask import Blueprint, render_template
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

@main.route('/guestlist', methods=['POST'])
@login_required
def guestlist():
    return render_template('guestlist.html')

@main.route('/invitemessage', methods=['POST'])
@login_required
def invitemessage():
    return render_template('message.html')

