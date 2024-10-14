from flask import Flask, request, jsonify, session
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  # For handling MongoDB ObjectId
import os

# Load environment variables (make sure you have your .env file set up)
from dotenv import load_dotenv
load_dotenv()

# Flask app configuration
class ApplicationConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")
    SESSION_TYPE = "mongodb"  # Store sessions in MongoDB
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

app = Flask(__name__)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

# MongoDB configuration
app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/mydatabase")
mongo = PyMongo(app)

# Initialize sessions using MongoDB
app.config.from_object(ApplicationConfig)
Session(app)

# User Registration
@app.route("/register", methods=["POST"])
def register_user():
    username = request.json["username"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    email = request.json["email"]
    password = request.json["password"]

    # Check if the user already exists
    user_exists = mongo.db.users.find_one({"username": username})
    if user_exists:
        return jsonify({"error": "User already exists"}), 409

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    # Create a new user document
    new_user = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": hashed_password
    }

    # Insert the new user into MongoDB
    mongo.db.users.insert_one(new_user)

    # Store the user ID in the session
    session["user_id"] = str(new_user["_id"])

    return jsonify({
        "id": str(new_user["_id"]),
        "username": new_user["username"],
        "message": "User created successfully",
    }), 201

# User Login
@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    # Find the user by email in MongoDB
    user_exists = mongo.db.users.find_one({"email": email})
    if not user_exists:
        return jsonify({"error": "Unauthorized"}), 401

    # Check if the password matches the hashed password
    if not bcrypt.check_password_hash(user_exists["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    # Store the user ID in the session
    session["user_id"] = str(user_exists["_id"])

    return jsonify({
        "id": str(user_exists["_id"]),
        "email": user_exists["email"]
    })

# Logout User
@app.route("/logout", methods=["POST"])
def logout_user():
    session.pop("user_id", None)
    return jsonify({"message": "User logged out successfully"}), 200

# Get Current Logged-In User
@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    # Find the user by ID in MongoDB
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    return jsonify({
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "first_name": user["first_name"],
        "last_name": user["last_name"]
    })

# Home Route
@app.route("/")
def home():
    return "Welcome to My Flask Web Application!"

# Run the Flask app
if __name__ == "__main__":
    app.run(port=5555, debug=True)
