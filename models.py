from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

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
    
    @classmethod
    def register(cls, username, password):
        """Register and create new user with hashed pw."""
        
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        
        return cls(username=username, password=hashed_utf8)
    
    @classmethod
    def authenticate(cls, username, password):
        """Authenticate username and password."""
        
        u = User.query.filter_by(username=username).first()
        
        if u and bcrypt.check_password_hash(u.password, password):
            # return user instance
            return u
        else:
            return False       
        