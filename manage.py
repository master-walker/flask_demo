#coding=utf-8

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from app import app
from app import db
from app.database import Role, Users

manager = Manager(app)

manager.add_command("run_server",host="0.0.0.0",port=5000,use_debugger=True)
def make_shell_context():
    return dict(app=app, db=db, Users=Users, Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()