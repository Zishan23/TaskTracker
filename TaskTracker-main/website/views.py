# Import necessary modules from Flask and related packages
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note  # Import the Note model from the models module
from . import db  # Import the SQLAlchemy instance 'db' from the current package
import os  # For handling file paths
from werkzeug.utils import secure_filename  # For securing uploaded filenames
import json  # For handling JSON data

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)

# Define the upload folder
UPLOAD_FOLDER = 'static/uploads'

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define a route for '/' with support for both GET and POST requests
@views.route('/', methods=['GET', 'POST'])
@login_required  # Require the user to be logged in to access this route
def home():
    if request.method == 'POST':
        # Retrieve note input from the form
        note = request.form.get('note')
        image_file = request.files.get('image')

        # Check for valid note or image
        if not note and not image_file:
            flash('Please provide a note or upload an image.', category='error')
        else:
            # Create a new Note object
            new_note = Note(data=note, user_id=current_user.id)

            # Handle image upload
            if image_file and image_file.filename != '':
                # Secure the filename
                filename = secure_filename(image_file.filename)
                relative_path = os.path.join('uploads', filename)  # Only store the relative path
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                new_note.image_path = f"uploads/{filename}"

                # Save the file to the static/uploads directory
                image_file.save(file_path)

                # Save the relative path to the Note object
                new_note.image_path = relative_path

            # Add the note to the database
            db.session.add(new_note)
            db.session.commit()

            # Flash a success message
            flash('Task added.', category='success')

    # Render the home page template and pass the current user to the template
    return render_template("home.html", user=current_user)

# Define a route for '/delete-note' with support for POST requests
@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Load JSON data from the request
    note = json.loads(request.data)
    noteId = note['noteId']
    
    # Query the database to get the Note with the given ID
    note = Note.query.get(noteId)
    
    if note:
        # Check if the current user owns the note
        if note.user_id == current_user.id:
            # Delete the associated image file, if any
            if note.image_path:
                file_path = os.path.join('static', note.image_path)
                if os.path.exists(file_path):
                    os.remove(file_path)

            # Delete the note from the database
            db.session.delete(note)
            db.session.commit()
            
            # Flash a success message for deleting the note
            flash('Note deleted.', category='success')

    # Return an empty JSON response
    return jsonify({})
