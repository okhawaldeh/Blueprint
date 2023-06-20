from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

#setting up a blueprint
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])

@login_required #you can't access the home page unless you're logged in
def home():
    
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            
            
    return render_template("home.html", user=current_user) #pass the current user to use in the front end

@views.route('/delete-note', methods={'POST'})
def delete_note():
    note = json.loads(request.data) #load the request that was made in the javascript
    noteId = note['noteId']
    note = Note.query.get(noteId) #get that note from db using its ID
    
    #if it exists
    if note:
        if note.user_id == current_user.id: # the user of the note matches current user
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({}) #return empty response (required to return something when using json)
    