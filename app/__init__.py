from flask import Flask
from .config import Config
from flask_migrate import Migrate
from dotenv import load_dotenv
from .common.helpers import login_mgr
from .models import db, Permission

load_dotenv()

# Create an instance of all required extensions
migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # initialize the configurations
    config = Config()
    # configure application
    app.config.from_object(config)
    config.init_app(app)

    # add the Permission class to the template context
    @app.context_processor
    def inject_permissions():
        return dict(Permission=Permission)

    # Initialize the database and extensions
    db.init_app(app)
    login_mgr.init_app(app)
    migrate.init_app(app, db)

    # Register your blueprints here
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
