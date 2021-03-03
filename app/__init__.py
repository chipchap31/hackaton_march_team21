from flask import Flask 
from .views.main import main_blueprint
def create_app(env='dev'): 

    app = Flask(__name__)

     
    app.config.from_pyfile(f'./config/config.{env}.py')


    app.register_blueprint(main_blueprint)



    return app
    