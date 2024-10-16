# from flask import Flask, request, jsonify, session
# from flask_session import Session
# from flask_bcrypt import Bcrypt
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# import os

# # Load environment variables
# from dotenv import load_dotenv
# load_dotenv()

# # Flask app configuration
# class ApplicationConfig:
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Using SQLite database
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SESSION_PERMANENT = False
#     SESSION_USE_SIGNER = True

# app = Flask(__name__)
# app.config.from_object(ApplicationConfig)

# CORS(app, supports_credentials=True)
# bcrypt = Bcrypt(app)

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # User model for SQLite
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(28), unique=True, nullable=False)
#     first_name = db.Column(db.String(28), nullable=False)
#     last_name = db.Column(db.String(28), nullable=False)
#     email = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)

#     def __repr__(self):
#         return f"<User {self.username}>"

# # Initialize database
# with app.app_context():
#     db.create_all()

# # User Registration
# @app.route("/register", methods=["POST"])
# def register_user():
#     if request.content_type != "application/json":
#         return jsonify({"error": "Content-Type must be application/json"}), 415
    
#     username = request.json["username"]
#     first_name = request.json["first_name"]
#     last_name = request.json["last_name"]
#     email = request.json["email"]
#     password = request.json["password"]

#     # Check if the user already exists
#     user_exists = User.query.filter_by(username=username).first()
#     if user_exists:
#         return jsonify({"error": "User already exists"}), 409

#     # Hash the password
#     hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

#     # Create a new user record
#     new_user = User(
#         username=username,
#         first_name=first_name,
#         last_name=last_name,
#         email=email,
#         password=hashed_password
#     )

#     db.session.add(new_user)
#     db.session.commit()

#     # Store the user ID in the session
#     session["user_id"] = new_user.id

#     return jsonify({
#         "id": new_user.id,
#         "username": new_user.username,
#         "message": "User created successfully",
#     }), 201

# # User Login
# @app.route("/login", methods=["POST"])
# def login_user():
#     email = request.json["email"]
#     password = request.json["password"]

#     # Find the user by email in SQLite
#     user = User.query.filter_by(email=email).first()
#     if not user:
#         return jsonify({"error": "Unauthorized"}), 401

#     # Check if the password matches the hashed password
#     if not bcrypt.check_password_hash(user.password, password):
#         return jsonify({"error": "Unauthorized"}), 401

#     # Store the user ID in the session
#     session["user_id"] = user.id

#     return jsonify({
#         "id": user.id,
#         "email": user.email
#     })

# # Logout User
# @app.route("/logout", methods=["POST"])
# def logout_user():
#     session.pop("user_id", None)
#     return jsonify({"message": "User logged out successfully"}), 200

# # Get Current Logged-In User
# @app.route("/@me")
# def get_current_user():
#     user_id = session.get("user_id")

#     if not user_id:
#         return jsonify({"error": "Unauthorized"}), 401

#     # Find the user by ID in SQLite
#     user = User.query.get(user_id)

#     return jsonify({
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#         "first_name": user.first_name,
#         "last_name": user.last_name
#     })

# # Home Route
# @app.route("/")
# def home():
#     return "Welcome to My Flask Web Application!"

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(port=5555, debug=True)
