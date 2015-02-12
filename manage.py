#!/usr/bin/env python

"""
Usage: ./manage.py [submanager] <command>
Manage script for development. Type ./manage.py for more info
"""
from flask_script import Manager
from flask_script.commands import ShowUrls

from src.app import create_app
from src.settings import app_config

app = create_app(app_config)
manager = Manager(app)
manager.add_command("routes", ShowUrls())

@manager.shell
def make_context_shell():
    """
    Usage: ./manage.py shell
    Starts a python shell with with configured app loaded
    """
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
