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


# Holiday type template route
@app.route("/holiday_types")
# Database query the Holiday model, get holiday types and order by name. Template displayed to user. 
def holiday_types():
    holiday_types = list(Holiday.query.order_by(Holiday.holiday_name).all())
    return render_template('holiday_types.html', holiday_types=holiday_types)


# Add cataegory bytton uses Get method, renders add_holiday_types page. Submiting the form (POST) posts data (holiday_name and icon) to database
@app.route("/add_holiday_types", methods=["GET", "POST"])
def add_holiday_types():
    if request.method == "POST":
        holiday_type = Holiday(holiday_name=request.form.get("holiday_name"), selected_icon=request.form.get("selected_icon"))
        db.session.add(holiday_type)
        db.session.commit()
        return redirect(url_for("holiday_types"))
    return render_template('add_holiday_types.html')


@app.route("/edit_holiday_types/<int:holiday_id>", methods=["GET", "POST"])
def edit_holiday_types(holiday_id):
    holiday_type = Holiday.query.get_or_404(holiday_id)
    if request.method == "POST":
        holiday_type.holiday_name = request.form.get("holiday_name")
        holiday_type.selected_icon = request.form.get("selected_icon")
        db.session.commit()
        return redirect(url_for("holiday_types"))
    return render_template('edit_holiday_types.html',holiday_type=holiday_type)