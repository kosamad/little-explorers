# Imports from Flask
from flask import render_template
# Import from taskmanager package
from taskmanager import app, db
from taskmanager.models import Holiday, Recommendation

# Create Route Decorator
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/holiday_types")
def holiday_types():
    return render_template('holiday_types.html')

@app.route("/add_holiday_types", methods=["GET", "POST"])
def add_holiday_types():
    return render_template('add_holiday_types.html')