from flask import Flask, request, Response
from .services.s3bucket import S3Bucket
from .views.quizzes_view import quizzes_view
from .views.main_view import main_view
from .views.parade_view import parade_view
from .Mailer import mail


def create_app(): 

    app = Flask(__name__)

     
    app.config.from_pyfile(f'./config.py')

    
    
    app.register_blueprint(main_view)
    app.register_blueprint(quizzes_view)
    app.register_blueprint(parade_view)
    mail.init_app(app)
    # url can be change if you want 
    # make sure you make the same changes on the front-end 
    @app.route('/upload', methods=['POST'])
    def upload():
        """
        This is just a placeholder
        """

        if request.method == 'POST':

            files = request.files['file']

          
    
          


            
               
               

            return Response(S3Bucket().upload(files), 200)
            
            


    return app
    