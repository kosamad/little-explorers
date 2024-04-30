# Imports from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 
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
    return render_template("index.html")

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
        email_to_check = User.query.filter_by(email=email).first()      
        if email_to_check:
            # Check hashed password and return true/false
            if check_password_hash(email_to_check.password_hash, password):
                flash("Login successful", "success")
                # change below to profile page once made
                return redirect(url_for("add_recommendation"))
            else:
                flash('Invalid email or password. Please try again.', 'error')
                return redirect(url_for('sign_in'))  
        else:
            flash('Invalid email or password. Please try again.', 'error')
    return render_template('sign_in.html')





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
    password = request.form.get('password_hash') 
    # sha256 is an algorhythm to generate the hashed password
    password_hash = generate_password_hash(password, "sha256")  

    # Check if the username already exists in the database
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "Username already exists. Please choose a different username."

    # Check if the email address already exists in the database
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return "An account with this Email address already exists."

    new_user = User(username=username, email=email, password_hash=password_hash)   
    db.session.add(new_user) 
    db.session.commit()
    return redirect(url_for('sign_in'))
     
# Recommendations Route
@app.route("/recommendations")
def recommendations():
    return render_template("recommendations.html")
    
# Add Recommendation Route
@app.route("/add_recommendation", methods=["GET", "POST"])
def add_recommendation():
    holiday_types = list(Holiday.query.order_by(Holiday.holiday_name).all())
    if request.method == "POST":
        if 'image' in request.files:
            image = request.files['image']            
            if image.filename != '':
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['user_uploaded_images'], filename))
                mimetype = image.mimetype
                # Create a new Image object and add it to the database
                new_image = Image(name=filename, mimetype=mimetype) 
                db.session.add(new_image)
                db.session.commit()

        # Create a new Recommendation object and add it to the database
        recommendation = Recommendation(
            recommendation_name=request.form.get("recommendation_name"),
            location_name=request.form.get("location_name"),
            occupants=request.form.get("occupants"),
            recommendation_review=request.form.get("recommendation_review"),  
            region=request.form.get("region"),
            image=request.form.get("image"),
            mimetype=request.form.get("mimetype"),
            recommendation_date=request.form.get("recommendation_date"),
            holiday_id=request.form.get("holiday_id"),
            map_long=request.form.get("map_long"),
            map_lat=request.form.get("map_lat"),
            user_id=current_user.id,
        )         
        db.session.add(recommendation)
        db.session.commit()
        return redirect(url_for("recommendations"))
    return render_template('add_recommendation.html', holiday_types=holiday_types )

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





# Admin User Route
@app.route('/create_admin')
def create_admin():
    admin_user = Users(username='admin', email='admin@example.com', password_hash='hashed_password', is_admin=True)
    db.session.add(admin_user)
    db.session.commit()
    return 'Admin user created successfully.'


