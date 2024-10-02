""" This is an API for a children's online store """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialise SQLAlchemy DB
db = SQLAlchemy()
# Initialise Flask-Migrate for database migrations
migrate = Migrate()


def create_app(config_class=Config):
    """ Function to initialise the flask app and configure it """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app