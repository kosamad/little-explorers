# Import operating system
import os

# Import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Import hidden environment variables
if os.path.exists("env.py"):
    import env  

# Create a Flask Instance
app = Flask(__name__)

# App configuration variables
# Secret Key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# Add Database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Initialise the database
db = SQLAlchemy(app)

app.config['user_uploaded_images'] = 'taskmanager/static/images/user_uploaded_images'

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Import routes and models file
from taskmanager import routes 
# from taskmanager import models

# Function req to load user object based on the user_id (in session) from the database as part of Flasks login manager
@login_manager.user_loader
def load_user(user_id):    
    return User.query.get(int(user_id))