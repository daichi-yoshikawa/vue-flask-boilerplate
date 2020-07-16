import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('development_config_secret_key')


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get(f'FLASK_SECRET_KEY')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
