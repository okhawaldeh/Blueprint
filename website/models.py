#importing package from this directory
from . import db

#helps with logging in
from flask_login import UserMixin

#helps with the dataTime automated functionality
from sqlalchemy.sql import func

#create DB models (users and financial data)

#defining a schema for an object in our db
class User(db.Model, UserMixin):
    
    #creating the columns for users
    #every user has to have a primary key of type integer
    id = db.Column(db.Integer, primary_key=True)
    
    #user has an email of type string and max length 100. Also, unique
    email = db.Column(db.String(100), unique=True)
    #same goes for the rest of data
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    #everytime we create a finData, add this finData ID to this relationship
    #this helps with keeping all the finData of a user together
    notes = db.relationship('Note')

#defining a schema for financial data of the users
class Note(db.Model): ###### this should be for project purposes ######
    
    id = db.Column(db.Integer, primary_key=True)
    #all the finData should be associated to users, foreign key is needed
    #when creating a finData, we must pass a valid ID of an existing user (foreign key)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user.id goes to the user class, id column (primary key)

    data = db.Column(db.String(10000)) 
    date = db.Column(db.DateTime(timezone=True), default=func.now())