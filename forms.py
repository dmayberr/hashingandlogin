from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email
from wtforms.widgets.core import PasswordInput

class NewUserForm(FlaskForm):
    """Form for registering and creating a new user."""
    
    username = StringField("Username",
                           validators=[InputRequired()])
    password = StringField("Password",
                           widget=PasswordInput(hide_value=True))
    email = StringField("Email address",
                        validators=[Email(), InputRequired()])
    first_name = StringField("First name",
                             validators=[InputRequired()])
    last_name = StringField("Last name",
                            validators=[InputRequired()])
    
    
class LoginForm(FlaskForm):
    """Form for handling user login information."""
    
    username = StringField("Username",
                           validators=[InputRequired()])
    password = StringField("Password",
                           validators=[Email(), InputRequired()])
   