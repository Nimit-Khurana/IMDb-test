from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired


class loginform(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=6,message="Enter between 3 and 6")])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label="Remember me")