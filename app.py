from flask import Flask, request, render_template, redirect, flash, session
from models import User, db, connect_db
from forms import NewUserForm, LoginForm, DeleteForm
from flask_bcrypt import Bcrypt
from werkzeug.exceptions import Unauthorized

bcrypt = Bcrypt()

app = Flask(__name__)

app.config['SECRET_KEY'] = "whatever"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///UserDB'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

db.init_app(app)
connect_db(app)

@app.route('/')
def root():    
    return render_template("home.html")
    
@app.route('/register')
def show_registration_form():
    """Route to get and show registration form to create new users."""
    
    form = NewUserForm()
    
    return render_template('users/new_user_form.html', form=form)

@app.route('/register', methods=['POST'])
def submit_new_user():
    """Handle submission of new user form."""
    
    form = NewUserForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        
        user = User.register(username, password, email, first_name, last_name)
        
        db.session.commit()
        session['username'] = user.username
        
        flash(f"User created.")
        return redirect(f"/users/{user.username}")
    else:
        return render_template("users/new_user_form.html", form=form)
        
    

@app.route('/login')
def login():
    """Route will render a user login form accepting username and password."""
    
    if "username" in session:
        return redirect(f"/users/{session['username']}")
    
    form = LoginForm()
    
    return render_template('users/user_login_form.html', form=form)

@app.route('/login', methods=['POST'])
def handle_login():
    """Route to handle submission of login information"""
    
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            session['username'] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Invalid username or password."]
            return render_template("users/user_login_form.html", form=form)
        
    return render_template("users/user_login_form.html", form=form)

@app.route('/secret')
def secret():    
    return render_template('secret.html')

@app.route("/logout")
def logout():
    """Logout route."""

    session.pop("username")
    return redirect("/login")

@app.route("/users/<username>")
def show_user(username):
    """Example page for logged-in-users."""

    if "username" not in session or username != session['username']:
        raise Unauthorized()

    user = User.query.get(username)
    form = DeleteForm()

    return render_template("users/show.html", user=user, form=form)