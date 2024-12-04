# Import necessary modules from Flask and related packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os  # For path handling

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "database.db"

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Configure the application
    app.config['SECRET_KEY'] = 'allen garcia'  # Replace with a secure secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')

    # Ensure the upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models
    from .models import User, Note

    # Create the database tables (if not already created)
    with app.app_context():
        db.create_all()

    # Initialize and configure Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Utility to create the database explicitly
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
