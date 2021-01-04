from flask import Flask, request, render_template, redirect, flash, session
from models import User, db, connect_db
from forms import User

app = Flask(__name__)
# TODO- Add db name to link below
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///*****'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db.init_app(app)
connect_db(app)

@app.route('/')
def root():
    
    redirect (f"/register")
    
@app.route('/register')
def show_registration_form():
    """Route to get and show registration form to create new users."""
    
    return render_template('new_user_form.html')

@app.route('/register', methods=['POST'])
def submit_new_user():
    """Handle submission of new user form."""
    
    return redirect (f"/secret")

@app.route('/login')
def login():
    """Route will render a user login form accepting username and password."""
    
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login():
    """Route to handle submission of login information"""
    
    return redirect (f"/secret")

@app.route('/secret')
def secret():
    
    return (f"You made it!")