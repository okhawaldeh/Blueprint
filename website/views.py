from flask import Blueprint

#setting up a blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"
