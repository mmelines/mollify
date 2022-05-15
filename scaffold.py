class Scaffold:

    def __init__(self):
        # code for first iteration init.py file
        self.init_py = '''start_read
        from flask import Flask
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate
        import os

        def create_app():
            app = Flask(__name__)
            app.config.from_object('<APP_NAME>.config.DevelopmentConfig')

            from <APP_NAME>.model import db
            db.app = app
            db.init_app(app)
            migrate = Migrate(app, db)
            db.create_all()

            return app
        end_read
        '''
        # additional code for second iteration 
        self.init_api = """start_read
            from <APP_NAME>.api import mapi
            app.register_blueprint(mapi)
        end_read"""
        #
        self.model_py = """start_read
        from flask_sqlalchemy import SQLAlchemy

        db = SQLAlchemy()
        end_read"""
        # 
        self.config = """start_read
        class Config(object):
            TESTING=False
            SQLALCHEMY_TRACK_MODIFICATIONS=False

        class ProductionConfig(Config):
            SQLALCHEMY_DATABASE_URI = "<DB_URI>"

        class DevelopmentConfig(Config):
            SQLALCHEMY_DATABASE_URI = "<TEST_DB_URI>"
            FLASK_ENV = 'development'
            TESTING=True

        class TestingConfig(Config):
            SQLALCHEMY_DATABASE_URI = "<TEST_DB_URI>"
            TESTING=True

        end_read"""

    def init_txt(self, stage):
        if stage == 1: 
            return self.init_py
        if stage == 2:
            return self.init_api

    def setup_txt(self):
        return False

    def model_txt(self):
        return self.model_py

    def config_txt(self):
        return self.config

    def __iter__(self):
        yield ("init", self.init_py)
        yield ("init_api", self.init_api)


# data

