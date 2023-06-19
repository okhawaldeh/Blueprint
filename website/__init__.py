from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oamfsadklnfsda'
    
    #connect the database to the flask app
    #this is saying that my sqlalchemy database is located at sqlite:///{DB_NAME}
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    #inialize DB
    db.init_app(app)
    
    #importing views' blueprints
    from .views import views
    #importing auth's blueprints
    from .auth import auth
    
    #registering the views' blueprint
    app.register_blueprint(views, url_prefix='/')
    #registering the auth's blueprint
    app.register_blueprint(auth, url_prefix='/')
    
    #importing the classes so that flask know that they're there
    from .models import User, FinData
    
    create_database(app)
    
    return app

def create_database(app):
    #if the database doesn't exist in the directory
    if not path.exists('website/' + DB_NAME):
        
        #specifying the app that the db is associated with
        db.create_all(app=app)
        print('Created Database')