import os

class Config:
    SECRET_KEY = os.environ.get('SECRET KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collins:##@@collins1@localhost/pitch'

class ProdConfig(Config):    
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    