from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class User(db.Model):
    """User model"""
    
    __tablename__ = 'users'
    
    def __repr__(self):
        u = self
        return f"<id={u.id}"
    
    username = db.Column(db.String(20),
                         primary_key=True,
                         unique=True,
                         )
    password = db.Column(db.String(20),
                         nullable=False,
                         )
    email = db.Column(db.String(50),
                      nullable=False)
    first_name = db.Column(db.String(30),
                           nullable=False)
    last_name = db.Column(db.String(30),
                           nullable=False)
    
    