#!/usr/bin/env python
#coding=utf-8

from flask_mail import Mail,Message
from flask import render_template
from app import app

app.config["FLASKY_MAIL_SUBJECT_PREFIX"] = "FLASKY"
app.config["FLASKY_MAIL_SENDER"] = "FLASKY ADMIN <1158620887@qq.com>"

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config["FLASKY_MAIL_SUBJECT_PREFIX"] + subject, sender=app.config["FLASKY_MAIL_SENDER"],recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    Mail.send(msg)
