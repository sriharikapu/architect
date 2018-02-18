import os
basedir = os.path.abspath(os.path.dirname(__file__))
from os.path import join, dirname


class HackConfig(object):
    DEBUG = True
    TESTING = False
    HACKING = True

config = {
    "hack": "archie.config.HackConfig",
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'hack')
    app.config.from_object(config[config_name]) # object-based default configuration
    app.config.from_pyfile('config.cfg', silent=True) # instance-folders configuration