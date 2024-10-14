from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SESSION_TYPE = "mongodb"  # Configure session to use MongoDB
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    MONGO_URI = os.environ["MONGO_URI"]  # MongoDB URI (e.g., mongodb://username:password@localhost:27017/mydatabase)
