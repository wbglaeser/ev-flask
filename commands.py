import click
from database import db
from models import Event, User

def create_db():
    """Creates database"""
    db.create_all()
    
def drop_db():
    """Cleans database"""
    db.drop_all()

def create_user_table():
    """ Create table model in the database """
    User.__table__.create(db.engine)

def create_event_table():
    """ Create table model in the database """
    User.__table__.create(db.engine)

def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, create_user_table, create_event_table]:
        app.cli.add_command(app.cli.command()(command))
