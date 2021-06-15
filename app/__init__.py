from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__)

# setting up configurations
app.config.from_object(DevConfig)

# initializing flask extensions
bootstrap = Bootstrap()

from app import views
from app import error
