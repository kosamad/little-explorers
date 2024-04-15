# Imports from Flask
from flask import render_template
# Import from taskmanager package
from taskmanager import app, db

# Create Route Decorator
@app.route("/")
def home():
    return render_template("base.html")