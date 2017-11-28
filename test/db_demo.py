#!/usr/bin/env python
#coding=utf-8
from app import db
from app.database import Role,Users

# db.create_all()
print Role.query.all()
print Users.query.all()
print Role.query.filter_by(name="Admin").first()

admin_role = Role(name="Admin")
user_role = Role(name="Users")
user_john = Users(username="John",role=admin_role)
user_jack = Users(username="Jack",role=user_role)
# db.session.add_all([admin_role,user_role,user_john,user_jack])
admin_role.name = "Administrator"
db.session.add(admin_role)
db.session.commit()
print admin_role.name
print user_role.id

