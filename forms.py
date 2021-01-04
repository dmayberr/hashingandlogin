from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email

class NewUserForm(FlaskForm):
    """Form for registering and creating a new user."""
    
    username = StringField("Username")
    password = StringField("Password")
    email = StringField("Email address")
    first_name = StringField("First name")
    last_name = StringField("Last name")
    
    
class LoginForm(FlaskForm):
    """Form for handling user login information."""
    
    username = StringField("Username",
                           validators=[InputRequired()])
    password = StringField("Password",
                           validators=[Email()])
   