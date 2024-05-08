# Imports from Flask
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from sqlalchemy import or_

import os

# Import from taskmanager package
from taskmanager import app, db
from taskmanager.models import Holiday, Recommendation, User

# Importing for photo upload
from werkzeug.utils import secure_filename
# Importing for password generation
from werkzeug.security import generate_password_hash, check_password_hash


# Home page Route
@app.route("/")
def home():
    recommendations = list(Recommendation.query.order_by(Recommendation.id).all())
    return render_template("index.html",recommendations=recommendations)  
    
# Contact Route
@app.route("/contact")
def contact():
    return render_template('contact.html')

# Create Account Route
@app.route("/create_account")
def create_account():
    return render_template('create_account.html')

# Sign in Route
@app.route("/sign_in",methods=["GET","POST"])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password_hash')
        # Check email address in database
        user = User.query.filter_by(email=email).first()     
        if user:
            # Check hashed password and return true/false
            if check_password_hash(user.password_hash, password):
                # Assign user information to session to give user specific functionality
                session['user_id'] = user.id
                session['username'] = user.username
                session['email'] = user.email
                session['is_admin'] = user.is_admin
                flash("Login Successful", "success")
                # change below to profile page once made
                return redirect(url_for("profile"))
            else:
                flash('Invalid email or password. Please try again.', 'error')
                return redirect(url_for('sign_in'))  
        else:
            flash('Invalid email or password. Please try again.', 'error')
    return render_template('sign_in.html')

# Sign out Route
@app.route("/sign_out")
def sign_out():
    # Remove user authentication information from session
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('email', None)
    session.pop('is_admin', None)
    flash('You have been signed out.', 'info')  
    return redirect(url_for('home'))


# Check User
@app.route("/users_check")
def users_check():
    users = list(User.query.all())
    return render_template('users_check.html', users=users)  

# Route to add a new user
@app.route('/create_account', methods=['POST'])
def add_user():   
    username = request.form.get('username')
    email = request.form.get('email') 
    is_admin = request.form.get("is_admin", "").lower() == "true"
    password = request.form.get('password_hash') 
    # sha256 is an algorhythm to generate the hashed password
    password_hash = generate_password_hash(password, "sha256")  

    # Check if the username already exists in the database
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
       flash("Sorry, the username you entered is already taken.", "error")
       return redirect(url_for("create_account"))

    # Check if the email address already exists in the database
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        flash("An account with this Email address already exists. Please sign in.")
        return redirect(url_for("sign_in"))

    new_user = User(username=username, email=email, password_hash=password_hash,is_admin=is_admin)   
    db.session.add(new_user) 
    db.session.commit()
    flash("You have created an account, please Sign In", "success")
    return redirect(url_for('sign_in'))
     
# Recommendations Route
@app.route("/recommendations")
def recommendations():
    recommendations = list(Recommendation.query.order_by(Recommendation.id).all())
    return render_template("recommendations.html", recommendations=recommendations)

# Search Recommendations Route
@app.route("/search", methods=['GET','POST'])
def search():
    if request.method == "POST":
        form = request.form
        search_value = form['search_string']        
        search = "%{0}%".format(search_value)        
        results = db.session.query(Recommendation).join(Holiday).filter(
            or_(
                Recommendation.recommendation_review.ilike(search),  # Case-insensitive search
                Holiday.holiday_name.ilike(search)  # Case-insensitive search
            )
        ).all()
        return render_template("recommendations.html", recommendations=results,)
    else:
        return redirect('/recommendations')

# Recommendation Map Route
@app.route("/recommendations_map")
def recommendations_map():
    data = Recommendation.query.with_entities(Recommendation.id, Recommendation.map_lat, Recommendation.map_long, Recommendation.location_name).all()
    map_data = [{'recommendation_id': item.id, 'map_lat': item.map_lat, 'map_long': item.map_long, 'location_name': item.location_name} for item in data]
    return jsonify(map_data)

# View Recommendation Route
@app.route("/recommendation/<int:recommendation_id>", methods=["GET"])
def view_recommendation(recommendation_id):
    recommendation = Recommendation.query.get_or_404(recommendation_id)
    return render_template('view_recommendation.html', recommendation=recommendation)

# Delete Recommendation (Admin from recommendations page)
@app.route("/delete_recommendation/<int:recommendation_id>")
def delete_recommendation(recommendation_id):
    recommendation = Recommendation.query.get_or_404(recommendation_id)
    db.session.delete(recommendation)
    db.session.commit()    
    # Check if the referrer URL contains '/profile'
    if '/profile' in request.referrer:
        return redirect(url_for("profile"))
    else:
        return redirect(url_for("recommendations"))

# Add Recommendation Route
# Image upload code adapted from ????
# defensive prgramming includes Werkzeug secure_filename function and check to ensure only jpg, png and jpeg files are uploaded

@app.route("/add_recommendation", methods=["GET", "POST"])
def add_recommendation():
    holiday_types = list(Holiday.query.order_by(Holiday.holiday_name).all())
    user_id = session.get('user_id')  
    image_name = None
    if request.method == "POST":
        mimetype = request.form.get("mimetype")  # Get the mimetype from the form
        if mimetype.startswith('image'):  # Check if the mimetype starts with 'image'
            if 'image' in request.files:
                image = request.files['image']
                if image.filename != '':
                    # Read image data
                    image_name = secure_filename(image.filename)
                    image_path = os.path.join(app.config['user_uploaded_images'], image_name)
                    image.save(image_path)  # Save the image to the file system
                               
             
        else:
            flash("Invalid file format. Please upload only images.", "error")

        # Check if the recommendation title already exists in the database
        existing_recommendation = Recommendation.query.filter_by(recommendation_name=request.form.get("recommendation_name")).first()

        if existing_recommendation:
            flash("Recommendation title already exists. Please choose a different title.", "error")
        else:
        # Create a new Recommendation object and add it to the database
            recommendation = Recommendation(            
                recommendation_name=request.form.get("recommendation_name"),
                location_name=request.form.get("location_name"),
                occupants=request.form.get("occupants"),
                recommendation_review=request.form.get("recommendation_review"),  
                region=request.form.get("region"),            
                mimetype=mimetype,
                image_name=image_name,
                recommendation_date=request.form.get("recommendation_date"),
                holiday_id=request.form.get("holiday_id"),
                map_long=request.form.get("map_long"),
                map_lat=request.form.get("map_lat"),
                user_id = session.get('user_id')
            )         
            db.session.add(recommendation)
            db.session.commit()
            return redirect(url_for("recommendations"))
    return render_template('add_recommendation.html', holiday_types=holiday_types, user_id=user_id )

@app.route("/check_recommendation_title", methods=["POST"])
def check_recommendation_title():
    recommendation_name = request.json.get("recommendation_name")
    existing_recommendation = Recommendation.query.filter_by(recommendation_name=recommendation_name).first()

    if existing_recommendation:
        # If the recommendation title already exists, return exists=True
        return jsonify({"exists": True})
    else:
        # If the recommendation title is unique, return exists=False
        return jsonify({"exists": False})

# Edit Recommendation Route
@app.route("/edit_recommendation/<int:recommendation_id>", methods=["GET", "POST"])
def edit_recommendation(recommendation_id):
    recommendation = Recommendation.query.get_or_404(recommendation_id)
    holiday_types = list(Holiday.query.order_by(Holiday.holiday_name).all())
    image_name = recommendation.image_name
    if request.method == "POST":
        mimetype = request.form.get("mimetype") 
        if mimetype.startswith('image'): 
            if 'image' in request.files:
                image = request.files['image']
                if image.filename != '':                    
                    image_name = secure_filename(image.filename)
                    image_path = os.path.join(app.config['user_uploaded_images'], image_name)
                    image.save(image_path)
                    recommendation.image_name = image_name # Update the image name                           
            else:
                flash("Invalid file format. Please upload only images.", "error")

        # Update the existing Recommendation object and add it to the database
               
        recommendation.recommendation_name=request.form.get("recommendation_name")
        recommendation.location_name=request.form.get("location_name")
        recommendation.occupants=request.form.get("occupants")
        recommendation.recommendation_review=request.form.get("recommendation_review")
        recommendation.region=request.form.get("region")          
        recommendation.mimetype=mimetype
        recommendation.image_name=image_name
        recommendation.recommendation_date=request.form.get("recommendation_date")
        recommendation.holiday_id=request.form.get("holiday_id")
        recommendation.map_long=request.form.get("map_long")
        recommendation.map_lat=request.form.get("map_lat")
        recommendation.user_id = session.get('user_id')                      
        db.session.commit()
        return redirect(url_for("profile"))
    return render_template('edit_recommendation.html',recommendation=recommendation, holiday_types=holiday_types, user_id=session.get('user_id'))


# Holiday type Route
@app.route("/holiday_types")
# Database query the Holiday model, get holiday types and order by name. Template displayed to user. 
def holiday_types():
    holiday_types = list(Holiday.query.order_by(Holiday.holiday_name).all())
    return render_template('holiday_types.html', holiday_types=holiday_types)

# Add holiday type. Button uses Get method, renders add_holiday_types page. Submiting the form (POST) posts data (holiday_name and icon) to database
@app.route("/add_holiday_types", methods=["GET", "POST"])
def add_holiday_types():
    if request.method == "POST":
        holiday_type = Holiday(holiday_name=request.form.get("holiday_name"), selected_icon=request.form.get("selected_icon"))
        db.session.add(holiday_type)
        db.session.commit()
        return redirect(url_for("holiday_types"))
    return render_template('add_holiday_types.html')

# Edit holiday types (name and icon)
@app.route("/edit_holiday_types/<int:holiday_id>", methods=["GET", "POST"])
def edit_holiday_types(holiday_id):
    holiday_type = Holiday.query.get_or_404(holiday_id)
    if request.method == "POST":
        holiday_type.holiday_name = request.form.get("holiday_name")
        holiday_type.selected_icon = request.form.get("selected_icon")
        db.session.commit()
        return redirect(url_for("holiday_types"))
    return render_template('edit_holiday_types.html',holiday_type=holiday_type)

# Users
@app.route("/users")
# Database query the User model, get users and order by name. 
def users():
    users = list(User.query.order_by(User.username).all())
    return render_template('users.html', users=users)

# Delete User 
@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    users = User.query.get_or_404(user_id)
    db.session.delete(users)
    db.session.commit()
    return redirect(url_for("users"))

# Profile Page
@app.route("/profile")
def profile():
    user_id = session.get('user_id')
    user_recommendations = Recommendation.query.filter_by(user_id=user_id).order_by(Recommendation.recommendation_name).all() 
    return render_template("profile.html", user_recommendations=user_recommendations) 


@app.route("/check_current_user")
def check_current_user():
    print(current_user)
    return "Check console for current_user details"
