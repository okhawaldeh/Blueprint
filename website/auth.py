from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user


#setting up a blueprint
auth = Blueprint('auth', __name__)

#the methods are the type of requests this page can do
@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        
        #get the entered info
        email = request.form.get('email')
        password = request.form.get('password')
        
        #return the first email that matches (should work since email is unique)
        user = User.query.filter_by(email=email).first()
        
        #if user exists
        if user:
            #check if the hashed password matches the entered password
            if check_password_hash(user.password, password):
                login_user(user, remember=True) #keeps track if logged in
                flash('Logged in successfully', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email does not exists, please signup!', category='error')
    return render_template('login.html', user=current_user)

#the methods are the type of requests this page can do
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    #if submit is pressed, save the given info in variables
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # check that the input info is correct
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exists, please login', category='error')
        elif(len(email)==0 and len (name)==0 and len(password1)==0 and len(password2)==0):
            flash('Please fill out the fields', category='error')
        elif len(email) <  6:
            flash('Invalid email address', category='error')
        elif len(name) < 3:
            flash('Name must be at least 2 characters', category='error')
        elif (password1 != password2):
            flash('Password does not match', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        else:
            # add user to database
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user) #keeps track if logged in
            flash('Account created successfully', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)

@auth.route('/logout')
@login_required #you can't access the logout page unless you're logged in
def logout():
    logout_user() #logout current user
    return redirect(url_for('auth.login'))

