# Imports from Flask
from flask import render_template, request, redirect, url_for
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

# Add cataegory bytton uses Get method, renders add_holiday_types page. Submiting the form (POST) posts data to database
@app.route("/add_holiday_types", methods=["GET", "POST"])
def add_holiday_types():
    if request.method == "POST":
        holiday_type = Holiday(holiday_name=request.form.get("holiday_name"), selected_icon=request.form.get("selected_icon"))
        db.session.add(holiday_type)
        db.session.commit()
        return redirect(url_for("holiday_types"))
    return render_template('add_holiday_types.html')