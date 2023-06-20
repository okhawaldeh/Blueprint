from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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
    from .models import User, Note
    
    #if the database doesn't exist in the directory
    #specifying the app that the db is associated with
    with app.app_context():
        db.create_all()
        
    #tells flask how we actually login a user
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where does flask takes us if we're not logged in
    login_manager.init_app(app) #telling login manager which app we're using
    
    #telling flask how to we load a user (referencing them by ID)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app