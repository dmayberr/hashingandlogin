from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from wtforms.widgets.core import PasswordInput

class NewUserForm(FlaskForm):
    """Form for registering and creating a new user."""
    
    username = StringField("Username",
                           validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired()])
    email = StringField("Email address",
                        validators=[Email(message="Invalid input"), Length(min=3, max=50)])
    first_name = StringField("First name",
                             validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField("Last name",
                            validators=[InputRequired(), Length(min=1, max=30)])
    
    
class LoginForm(FlaskForm):
    """Form for handling user login information."""
    
    username = StringField("Username",
                           validators=[InputRequired()])
    password = PasswordField("Password",
                           validators=[InputRequired()]                           
                           )

# un=mayday pw=mayday 



class DeleteForm(FlaskForm):
    """Delete Form"""   
    
    