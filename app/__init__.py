import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils.read_config import config

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["MAIL_SERVER"] = config.mail_server
app.config["MAIL_PORT"] = config.mail_port
# app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = True
app.config["FLASKY_MAIL_SUBJECT_PREFIX"] = "[Flasky]"
app.config["FLASKY_MAIL_SENDER"] = config.email_address
app.config["MAIL_USERNAME"] = config.email_address
app.config["MAIL_PASSWORD"] = config.password
# export MAIL_USERNAME=

# app.config.from_object("config")
# csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)
# moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)
migrate = Migrate(app,db)
from app import models
from app.main import views
