import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('mollify_default.config.DevelopmentConfig')

    register_blueprints(app)

    from mollify_default.model import db
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()

    return app

def register_blueprints(app):
    from mollify_default.api import mapi
    from mollify_default.main import mapp

    app.register_blueprint(mapi, url_prefix="/api")
    app.register_blueprint(mapp)

