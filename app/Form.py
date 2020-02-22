# @file :Form.py

from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_wtf import FlaskForm


class Login_Form(FlaskForm):
    name = StringField('name', validators=[Required()])
    pwd = PasswordField('pwd', validators=[Required()])
    submit = SubmitField('Login in')


class Register_Form(FlaskForm):
    name = StringField('name', validators=[Required()])
    pwd = PasswordField('pwd', validators=[Required()])
    submit = SubmitField('register')