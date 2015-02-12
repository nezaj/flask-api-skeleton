
from flask import Flask

from . import api, services
from .loggers import configure_sqlalchemy_logger, get_app_stderr_handler

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_app(app)
    register_loggers(app)
    register_blueprints(app)
    return app

def register_app(app):
    """ Do any one-time initialization of the app before serving """
    app.static_folder = app.config['STATIC_DIR']

def register_loggers(app):
    """ Sets up app and sqlalchemy loggers """
    app.logger.handlers = []
    app.logger.setLevel(app.config["APP_LOG_LEVEL"])
    app.logger.addHandler(get_app_stderr_handler())

    configure_sqlalchemy_logger(app.config["STDERR_LOG_FORMAT"], level=app.config["SQLALCHEMY_LOG_LEVEL"])

def register_blueprints(app):
    app.register_blueprint(api.views.blueprint)
    app.register_blueprint(services.views.blueprint)
