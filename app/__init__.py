from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_name):

# Initializing application
    app = Flask(__name__)

# setting up configurations
    app.config.from_object(config_options[config_name])

# initializing flask extensions
    bootstrap = Bootstrap()

    return app


