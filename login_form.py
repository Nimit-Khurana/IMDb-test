from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired


class loginform(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=6,message="Enter between 3 and 6")])
    password = PasswordField('password')
