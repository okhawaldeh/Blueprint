from flask import Blueprint, render_template

#setting up a blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
