#!/usr/bin/env python
#coding=utf-8

from flask_wtf import Form
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class FormDemo(Form):
    name = StringField("what's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")