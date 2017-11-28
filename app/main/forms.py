#!/usr/bin/env python
#coding=utf-8

from flask_wtf import Form
from wtforms import StringField,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo

class SignUp(Form):
    email_account = StringField("Email address", validators=[DataRequired(),Email(message="Please enter a valid email address")])
    verification_code = StringField("Enter verification code", validators=[DataRequired()])
    password = PasswordField("New password", validators=[DataRequired(),EqualTo("confirm_password", message="Passwords must match")])
    confirm_password = PasswordField("Repeat Password")
    submit = SubmitField("Submit")


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class FormDemo(Form):
    name = StringField("what's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")