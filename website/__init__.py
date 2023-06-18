from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oamfsadklnfsda'
    
    #importing views' blueprints
    from .views import views
    
    #importing auth's blueprints
    from .auth import auth
    
    
    
    return app