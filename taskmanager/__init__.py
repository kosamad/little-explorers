# Import operating system
import os

# Import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import hidden environment variables
if os.path.exists("env.py"):
    import env  

# Create a Flask Instance
app = Flask(__name__)

# App configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create Instance os SQAlchemy
db = SQLAlchemy(app)

# Import routes file
from taskmanager import routes  