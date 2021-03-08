from flask import Flask, request, Response
from .services.s3bucket import S3Bucket
from .views.quizzes_view import quizzes_view
from .views.main_view import main_view
from .views.parade_view import parade_view
from .Mailer import mail


def create_app(): 

    app = Flask(__name__)

     
    app.config.from_pyfile(f'./config.py')

    
    # Define middlewares here
    app.register_blueprint(main_view)
    app.register_blueprint(quizzes_view)
    app.register_blueprint(parade_view)
    mail.init_app(app)
  


    return app
    