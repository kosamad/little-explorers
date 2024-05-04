# Import db from taskmanager package
from taskmanager import db
# Import flask_login requriment. 
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 


# Database Tables

# 1. Holiday Type table
class Holiday(db.Model):
    #schema for the Type model
    id = db.Column(db.Integer, primary_key=True)
    holiday_name = db.Column(db.String(15), unique=True, nullable=False) #!!!!! work out how manycharacters limit for responsive design
    selected_icon = db.Column(db.Text, nullable=False)
    recommendation = db.relationship("Recommendation", backref="holiday", cascade="all, delete", lazy=True)
    def __repr__(self):
        return "#{0} - Holiday Name: {1} | Icon: {2}".format(
            self.id, self.holiday_name, self.selected_icon        
    )
        
# 2. User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)    
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  
    recommendation = db.relationship("Recommendation", backref="user", cascade="all, delete", lazy=True)
    
    # methods to manage password hashing and verification using werkzeug.securtiy
    # Adapted from the Codemy tutorials Flask Friday 
    @property
    def password(self):
        raise AttributeError('password is not an readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "#{0} - Username: {1} | Email: {2}".format(
            self.id, self.username, self.email
        )

# 4. Recommendations table
class Recommendation(db.Model):
    # schema for the Recommendations model
    id = db.Column(db.Integer, primary_key=True)
    recommendation_name = db.Column(db.String(30), unique=True, nullable=False)
    location_name = db.Column(db.String(100), nullable=False)
    occupants = db.Column(db.String(15), nullable=False) 
    recommendation_review = db.Column(db.Text, nullable=False)   
    region = db.Column(db.String(50), nullable=False)     
    mimetype = db.Column(db.Text, nullable=False) 
    image_name = db.Column(db.Text, nullable=False, unique=True) 
    recommendation_date = db.Column(db.Date, nullable=False) 
    holiday_id = db.Column(db.Integer, db.ForeignKey("holiday.id", ondelete="CASCADE"), nullable=False)
    map_long = db.Column(db.Float, nullable=False)
    map_lat = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)   
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name:{1} | Date:{2} | User ID:{3}".format(
            self.id, self.recommendation_name, self.recommendation_date, self.user_id
        )
