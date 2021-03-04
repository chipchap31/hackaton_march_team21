from flask import Flask, request, Response
from .views.main import main_blueprint
from werkzeug.utils import secure_filename
from .services.s3bucket import S3Bucket







def create_app(env='dev'): 

    app = Flask(__name__)

     
    app.config.from_pyfile(f'./config/config.{env}.py')


    app.register_blueprint(main_blueprint)

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
    