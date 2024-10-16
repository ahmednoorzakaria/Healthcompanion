from flask import Flask
from .config import ApplicationConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(ApplicationConfig)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views 
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User 

    migrate = Migrate(app, db)
    login = LoginManager(app)

    create_database(app)

    return app

def create_database(app):
    if not path.exists('server/' + DB_NAME):
        with app.app_context():
            db.create_all()  # Ensure database creation runs inside app context
            print("Created Database!")
