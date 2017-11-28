#!/usr/bin/env python
#coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from app import app
from app import db
# db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship("Users",backref="role")

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))
#
class Users(db.Model):
    pass
#     __tablename__ = "users"
#     id = db.Column(db.Integer,primary_key=True)
#     email_address = db.Column(db.String(64),unique=True,index=True)
#     password = db.Column(db.String(64))
    # username = db.Column(db.String(64),unique=True,index=True)
    # role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))


