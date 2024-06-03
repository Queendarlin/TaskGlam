import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
"""
This module sets up the core components of the TaskGlam Flask application.
It includes configuration, initialization of extensions, and basic settings.
"""


# Initialize Flask application
app = Flask(__name__)

# Disable strict slashes for URL routing
app.url_map.strict_slashes = False

# Set the secret key for securely signing the session cookie.
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
if not app.config['SECRET_KEY']:
    raise RuntimeError("SECRET_KEY environment variable not set")

# Set up the database URI for SQLAlchemy (using SQLite here)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'

# Initialize the SQLALCHEMY extension
db = SQLAlchemy(app)

# Initialize the Bcrypt extension for hashing passwords securely.
bcrypt = Bcrypt(app)

# Initialize the LoginManager extension
# to handle user sessions and authentication.
login_manager = LoginManager(app)

# Set the login view to redirect users to the login page
# if they are not authenticated.
login_manager.login_view = "login_page"

# Set the category for flash messages
# when users are redirected to the login page.
login_manager.login_message_category = "info"

from task_manager import routes
