class Scaffold:

    def __init__(self):
        # code for first iteration init.py file
        self.init_py = '''start_read
        import os
        from flask import Flask
        from flask_sqlalchemy import SQLAlchemy
        from flask_migrate import Migrate

        def create_app():
            app = Flask(__name__)
            app.config.from_object('<APP_NAME>.config.DevelopmentConfig')
            
            register_blueprints(app)

            from <APP_NAME>.model import db
            db.app = app
            db.init_app(app)
            migrate = Migrate(app, db)
            db.create_all()

            return app

        def register_blueprints(app):
            from <APP_NAME>.api import mapi
            from <APP_NAME>.main import mapp

            app.register_blueprint(mapi, url_prefix="/api")
            app.register_blueprint(mapp)
        end_read
        '''
        # code for first iteration init.py file
        self.main_application = '''start_read
        from app import create_app

        application = create_app()

        if __name__ == '__main__':
            application.run()
        end_read'''
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
        #
        self.api_py = """start_read
        import requests
        import logging
        from . import mapi # api blueprint
        from flask import jsonify, session, request

        logging.basicConfig(filename='demo.log', level=logging.DEBUG)

        @mapi.route('/', methods=['GET'])
        def json_hello():
            hello_world = {"message": "hello, world!"}
            return jsonify(hello_world)
        end_read"""
        #
        self.api_init_py = """start_read
        from flask import Blueprint

        # Blueprint Configuration
        mapi = Blueprint(
            'mapi', __name__,
            template_folder = 'templates'
        )

        from . import api
        end_read"""
        self.main_py = """start_read
        import requests
        import logging
        from . import mapp # main app/views Blueprint
        from flask import render_template, request, redirect, url_for

        logging.basicConfig(filename='demo.log', level=logging.DEBUG)

        @mapp.route('/', methods=['GET'])
        def hello():
            return "hello, world!"
        end_read"""
        self.main_init_py = """start_read
        from flask import Blueprint

        # Blueprint Configuration
        mapp = Blueprint(
            'mapp', __name__,
            template_folder = 'templates'
        )

        from . import main
        end_read"""

    def init_txt(self, stage):
        if stage == 1: 
            return self.init_py
        if stage == 2:
            return self.init_api

    def api_init_txt(self, stage):
        if stage == 1:
            return self.api_init_py

    def api_txt(self):
        return self.api_py

    def main_init_txt(self, stage):
        if stage == 1:
            return self.main_init_py

    def main_txt(self):
        return self.main_py

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

