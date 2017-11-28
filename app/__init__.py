import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["MAIL_SERVER"] = "smtp.qq.com"
app.config["MAIL_PORT"] = 25
# app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = True
app.config["FLASKY_MAIL_SUBJECT_PREFIX"] = "[Flasky]"
app.config["FLASKY_MAIL_SENDER"] = "1158620887@qq.com"
app.config["MAIL_USERNAME"] = "1158620887@qq.com"
app.config["MAIL_PASSWORD"] = "00,.,."
# export MAIL_USERNAME=

# app.config.from_object("config")
# csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)
# moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)
from app import views, models
