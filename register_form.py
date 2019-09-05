from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, InputRequired


class registerform(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired(), Length(min=3, max=6,message="Enter between 3 and 6")], render_kw={"placeholder": "First Name"})
    lname = StringField('Last Name', validators=[Length(min=3, max=6,message="Enter between 3 and 6")], render_kw={"placeholder": "Last Name"})
    username = StringField('Username',validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[Length(min=5, max=16,message="Enter between 5 and 16")], render_kw={"placeholder": "Email"})
    password = PasswordField('password', validators=[DataRequired()],render_kw={"placeholder": "New Password"})
    #avatar