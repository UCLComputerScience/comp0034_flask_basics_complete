from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

# The SQLAlchemy object is defined globally
db = SQLAlchemy()


def create_app(config_class=DevConfig):
    """
    Creates an application instance to run
    :return: A Flask object
    """
    app = Flask(__name__)

    # Configure app wth the settings from config.py
    app.config.from_object(config_class)

    # Allow the app to access to the database
    db.init_app(app)
    from app.models import Teacher, Student, Course, Grade
    with app.app_context():
        db.create_all()

    # Default route to be moved later in the lecture

    '''@app.route('/')
    def index():
        return render_template('index.html')

    '''
    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
