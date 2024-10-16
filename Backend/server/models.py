from bson.objectid import ObjectId
from flask import jsonify
from flask_bcrypt import Bcrypt
import uuid
from server import db
from flask_login import UserMixin


bcrypt = Bcrypt()

# # Example user creation function
# def create_user(username, first_name, last_name, email, password, mongo):
#     user_exists = mongo.db.users.find_one({"username": username})
    
#     if user_exists:
#         return jsonify({"error": "User already exists"}), 409
    
#     # Generate a hashed password
#     hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    
#     # New user document (Python dictionary) to be inserted into MongoDB
#     new_user = {
#         "_id": str(uuid.uuid4()),  # Unique identifier, typically UUID or MongoDB's ObjectId
#         "username": username,
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email,
#         "password": hashed_password
#     }

#     # Insert the new user document into MongoDB
#     mongo.db.users.insert_one(new_user)
    
#     return jsonify({
#         "id": new_user["_id"],
#         "username": new_user["username"],
#         "message": "User created successfully"
#     }), 201

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(28), nullable=False, unique=True)
    first_name = db.Column(db.String(28), nullable=False)
    last_name = db.Column(db.String(28), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    #Used to hash the password
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    #Check if the password is correct
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # "password": self.password,
        }
    
    def __repr__(self): #Used to give a textual representation of an object when it's printed, logged or inspected in the python shell

        return '<User {} - Email: {}>'.format(self.username, self.email)#The {} acts as a placeholder. format(self.username) inserts the value of the username attribute of the object into the placeholder {}
    

                                                                                                                                          
                                                                         
                                                                                                                                          
