from flask import Blueprint, render_template, request, flash

#setting up a blueprint
auth = Blueprint('auth', __name__)

#the methods are the type of requests this page can do
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

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
        if(len(email)==0 and len (name)==0 and len(password1)==0 and len(password2)==0):
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
            flash('Account created successfully', category='success')

    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return "<p>Logged out</p>"

