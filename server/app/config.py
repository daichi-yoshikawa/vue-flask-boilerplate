import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 15
    JWT_REFRESH_TOKEN_EXPIRES = 60 * 60 * 24 * 200
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JWT_SECRET_KEY = os.environ.get('development_config_secret_key')
    SECRET_KEY = os.environ.get('development_config_secret_key')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '../data-test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    JWT_SECRET_KEY = os.environ.get('test_config_secret_key')
    SECRET_KEY = os.environ.get('test_config_secret_key')


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get(f'FLASK_SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get(f'JWT_SECRET_KEY')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
