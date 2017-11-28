#!/usr/bin/env python
#coding=utf-8

from flask_mail import Mail,Message
from flask import render_template
from app import app, mail
from utils.read_config import config
from threading import Thread

app.config["FLASKY_MAIL_SUBJECT_PREFIX"] = "FLASKY"
app.config["FLASKY_MAIL_SENDER"] = "FLASKY ADMIN <{0}>".format(config.email_address)

# 异步发送邮件
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config["FLASKY_MAIL_SUBJECT_PREFIX"] + subject, sender=app.config["FLASKY_MAIL_SENDER"],recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    # mail.send(msg)
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr