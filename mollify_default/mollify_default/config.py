class Config(object):
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://mollify@localhost/mollify_default"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://mollify@localhost/mollify_test"
    FLASK_ENV = 'development'
    TESTING=True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://mollify@localhost/mollify_test"
    TESTING=True

