from flask.globals import session
import boto3
from werkzeug.utils import secure_filename
from os import path, remove
from flask import current_app
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MEDIA_FOLDER = 'media/'


class S3Bucket:
  
    def __init__(self):
     
     
        self.session = boto3.session.Session(aws_access_key_id=current_app.config['AWS_ACCESS_KEY'],
            aws_secret_access_key=current_app.config['AWS_SECRET_KEY']
        )
            
   
    def upload(self, file):
        """
        This method is called when you want to upload an image
        The file url is returned from AWS
        """
        
        secure_file = secure_filename(file.filename)
      
    
        file.save(f'{MEDIA_FOLDER}{secure_file}') # save 
      
        s3_resource = self.session.resource('s3')

        bucket = s3_resource.Bucket(current_app.config['AWS_BUCKET_NAME'])

        bucket.upload_file(Filename=f'{MEDIA_FOLDER}{secure_file}', Key=f'{MEDIA_FOLDER}{secure_file}')
        
        # check if the file is successfully created
        if path.exists(f'{MEDIA_FOLDER}{secure_file}'):
            # remove the file
            remove(f'{MEDIA_FOLDER}{secure_file}')

            return f'https://{current_app.config["AWS_BUCKET_NAME"]}.s3-eu-west-1.amazonaws.com/{MEDIA_FOLDER}{secure_file}'
        else:
            raise Exception(f'Error: {secure_file} does not exist.')