from flask import Blueprint, request, jsonify, session, redirect, url_for
from .models import User 
from .__init__ import db
from flask_bcrypt import Bcrypt

auth = Blueprint('auth',  __name__)

bcrypt = Bcrypt()

@auth.route('/', methods=["GET"]) 
def home():
    # Define home logic or leave as a placeholder
    pass

@auth.route('/login', methods=["POST"])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Store user ID in session
    session['user_id'] = user.id

    return redirect(url_for('views.home'))

@auth.route('/logout', methods=["POST"])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"}), 200

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        # Serve a registration form or some information
        return jsonify({"message": "Please send a POST request with registration data."}), 200

    if request.method == "POST":
        if request.is_json:
            data = request.get_json()  # Get the JSON data

            # Extract data and perform validation
            username = data.get('username')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')

            # Check if the user already exists
            user_exists = User.query.filter_by(username=username).first()
            if user_exists:
                return jsonify({"error": "User already exists"}), 409

            # Hash the password
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

            # Create a new user record
            new_user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password
            )

            db.session.add(new_user)
            db.session.commit()

            # Store the user ID in the session
            session["user_id"] = new_user.id

            return jsonify({"message": "User registered successfully!"}), 201
        else:
            return jsonify({"error": "Content-Type must be application/json"}), 415
