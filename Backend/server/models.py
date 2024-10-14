from bson.objectid import ObjectId
from flask import jsonify
from flask_bcrypt import Bcrypt
import uuid

bcrypt = Bcrypt()

# Example user creation function
def create_user(username, first_name, last_name, email, password, mongo):
    user_exists = mongo.db.users.find_one({"username": username})
    
    if user_exists:
        return jsonify({"error": "User already exists"}), 409
    
    # Generate a hashed password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    
    # New user document (Python dictionary) to be inserted into MongoDB
    new_user = {
        "_id": str(uuid.uuid4()),  # Unique identifier, typically UUID or MongoDB's ObjectId
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": hashed_password
    }

    # Insert the new user document into MongoDB
    mongo.db.users.insert_one(new_user)
    
    return jsonify({
        "id": new_user["_id"],
        "username": new_user["username"],
        "message": "User created successfully"
    }), 201
