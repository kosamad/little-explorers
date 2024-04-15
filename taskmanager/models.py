# Import db from taskmanager package
from taskmanager import db


# Database Tables

# 1. Holiday Type table
class Type(db.Model):
    #schema for the Type model
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(15), unique=True, nullable=False) #!!!!! work out how manycharacters limit for responsive design


    def __repr__(self):
        # represent self in the form of a string
        return self.type_name

# 2. Users table
class Users(db.Model):
    #schema for the Users model
    id = db.Column(db.Integer, primary_key=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self

# 3. Admin table
class Admin(db.Model):
    #schema for the Admin model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self

# 4. Recommendations table
class Recommendations(db.Model):
    #schema for the Recommendations model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self