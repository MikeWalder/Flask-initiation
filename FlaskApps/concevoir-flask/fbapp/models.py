from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

# Create a database connection object
db = SQLAlchemy(app)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(240), nullable=False)
    gender = db.Column(db.Integer(), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender
    
def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Scary Movie 1", Gender['male']))
    db.session.add(Content("Spartacus", Gender['male']))
    db.session.add(Content("The Great Rose", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized')



db.create_all()


