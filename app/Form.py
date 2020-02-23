# @file :Form.py

from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_wtf import FlaskForm


class Login_Form(FlaskForm):
    name = StringField('name', validators=[Required()])
    pwd = PasswordField('pwd', validators=[Required()])
    submit = SubmitField('Login in')


class Register_Form(FlaskForm):
    name = StringField('登录名', validators=[Required()])
    pwd = PasswordField('密码', validators=[Required()])
    confirm_pwd = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('register')