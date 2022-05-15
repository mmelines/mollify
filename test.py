from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('default.config.DevelopmentConfig')

    from default.model import db
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()

    return app

