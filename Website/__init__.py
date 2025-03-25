# This file will be used to initialize the Flask App

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate 
import os
 
db = SQLAlchemy() #Initialize the db, do not assign yet 
bcrypt = Bcrypt() #Initialize without passing app yet

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'fitness_tracker.db')}" #Flask knows we are storing fitness_tracker.db in /instance
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['SECRET_KEY'] = 'secretkey' #Key for Flask sessions
    
    if test_config is not None:
        app.config.update(test_config)
    
    app.config['UPLOADS_BASE_DIR'] = os.path.join(app.root_path, 'static', 'uploads')
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(app.config['UPLOADS_BASE_DIR'], 'progress_photos')
    app.config['UPLOADED_EXERCISES_DEST'] = os.path.join(app.config['UPLOADS_BASE_DIR'], 'exercises')
    
    migrate = Migrate(app, db)
    db.init_app(app) # Connect database to the app
    bcrypt.init_app(app) # Passsing app to bcrypt
    
    from .models import User, ExerciseLog, WeightLog, ExerciseMedia, Note # Import the models
    
    with app.app_context():
        Note.__table__.drop(db.engine, checkfirst=True)
        Note.__table__.create(db.engine)
        db.create_all() #Creates a database table for our data models

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    
    @login_manager.user_loader
    def load_user(user_id): 
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_theme():
        from flask_login import current_user
        if current_user.is_authenticated and hasattr(current_user, 'theme'):
            return {'user_theme': current_user.theme}
        return {'user_theme': 'light'} # Default theme 
    
    from .views import main
    app.register_blueprint(main) # Connect blueprint to app so we can use in .views
    
    return app


        