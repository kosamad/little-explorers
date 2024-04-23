# Import db from taskmanager package
from taskmanager import db


# Database Tables

# 1. Holiday Type table (cannot use work type as it is a reserved word in SQL)
class Holiday(db.Model):
    #schema for the Type model
    id = db.Column(db.Integer, primary_key=True)
    holiday_name = db.Column(db.String(15), unique=True, nullable=False) #!!!!! work out how manycharacters limit for responsive design
    selected_icon = db.Column(db.String(50), nullable=False)
    recommendation = db.relationship("Recommendation", backref="holiday", cascade="all, delete", lazy=True)
    def __repr__(self):
        # represent self in the form of a string
        return self.holiday_name, selected_icon

# # 2. Users table
# class Users(db.Model):
#     #schema for the Users model
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True, nullable=False)
#     email = db.Column(db.String(30), unique=True, nullable=False)
#     password_hash 


#     def __repr__(self):
#         # __repr__ to represent itself in the form of a string
#         return self

# 3. Admin table
#class Admin(db.Model):
    #schema for the Admin model
    #id = db.Column(db.Integer, primary_key=True)
    #a_username
   # a_email

    #def __repr__(self):
        # __repr__ to represent itself in the form of a string
      #  return self

# 4. Recommendations table
class Recommendation(db.Model):
    # schema for the Recommendations model
    id = db.Column(db.Integer, primary_key=True)
    recommendation_name = db.Column(db.String(25), unique=True, nullable=False)
    # location_name = db.Column(db.String(25), nullable=False)
    occupants = db.Column(db.Integer, nullable=False) 
    recommendation_review = db.Column(db.Text, nullable=False)
    holiday_id = db.Column(db.Integer, db.ForeignKey("holiday.id", ondelete="CASCADE"), nullable=False)
    region = db.Column(db.String(25), nullable=False)
    image = db.Column(db.Text, unique=True,) # hash it so this is the case. 
    recommendation_date = db.Column(db.Date, nullable=False) 
    #map_long = 
    #map_lat
    #user_id
   
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Name:{1} | Date:{2}".format(
            self.id, self.recommendation_name, self.recommendation_date
        )