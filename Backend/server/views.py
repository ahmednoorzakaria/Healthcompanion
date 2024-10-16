from flask import Blueprint 

views = Blueprint('views',  __name__)

@views.route('/')
def home():
    return "Welcome to the Home Page!"

@views.route('/dashboard')
def dashboard():
    pass
    # return render_template('dashboard.html')
