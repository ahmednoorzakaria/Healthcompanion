from dotenv import load_dotenv
import os  ## Used to handle paths and also retrieve data from the environment 

load_dotenv() ## Loads the SECRET_KEY variable from the .env file 

basedir = os.path.abspath(os.path.dirname(__file__)) ## basedir is a path to the root directory. Prevents from hardcoding the directory path which may change with time 

class ApplicationConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'users.db')
    # SESSION_TYPE = "mongodb"  # Configure session to use MongoDB
    # SESSION_PERMANENT = False
    # SESSION_USE_SIGNER = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MONGO_URI = os.environ["MONGO_URI"]  # MongoDB URI (e.g., mongodb://username:password@localhost:27017/mydatabase)
