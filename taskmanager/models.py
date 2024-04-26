# Import db from taskmanager package
from taskmanager import db


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
        
# 2. Users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  
    def __repr__(self):
        return "#{0} - Username: {1} | Email: {2}".format(
            self.id, self.username, self.email
        )

# 4. Recommendations table
class Recommendation(db.Model):
    # schema for the Recommendations model
    id = db.Column(db.Integer, primary_key=True)
    recommendation_name = db.Column(db.String(25), unique=True, nullable=False)
    location_name = db.Column(db.String(25), nullable=False)
    occupants = db.Column(db.String(15), nullable=False) 
    recommendation_review = db.Column(db.Text, nullable=False)   
    region = db.Column(db.String(25), nullable=False)
    image = db.Column(db.Text, unique=True,) # hash it so this is the case. 
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