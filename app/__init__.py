from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

# Create an instance of all required extensions
db = SQLAlchemy()
login_mgr = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # initialize the configurations
    config = Config()
    # configure application
    app.config.from_object(config)
    config.init_app(app)

    # Initialize the database and extensions
    db.init_app(app)
    login_mgr.init_app(app)
    migrate.init_app(app, db)

    # Register your blueprints here
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app