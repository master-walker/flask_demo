#!/usr/bin/env python
#coding=utf-8


'''
test app
'''
# pip install flask-openid
# pip install flask-mail
# pip install sqlalchemy
# pip install flask-sqlalchemy
# pip install sqlalchemy-migrate
# pip install flask-whooshalchemy==0.55a
# pip install flask-wtf
# pip install pytz
# pip install flask-babel
# pip install flup

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"


if __name__ == "__main__":
    app.run()