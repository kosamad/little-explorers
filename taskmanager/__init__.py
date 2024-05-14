# Import operating system
import os

# Import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create a Flask Instance
app = Flask(__name__)

# Cloudinary Credentials
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.uploader import upload

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

# Import hidden environment variables
if os.path.exists("env.py"):
    import env  

# App configuration variables
# Secret Key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Heroku Requirments
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


# Initialise the database
db = SQLAlchemy(app)

app.config['user_uploaded_images'] = 'taskmanager/static/images/user_uploaded_images'

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Function req to load user object based on the user_id (in session) from the database as part of Flasks login manager
@login_manager.user_loader
def load_user(user_id):    
    return User.query.get(int(user_id))
    

# Import routes and models file
from taskmanager import routes 