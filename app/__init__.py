from flask import Flask
from flask_bootsrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # # setting the config
    # app.config.from_object(DevConfig)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask Extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app