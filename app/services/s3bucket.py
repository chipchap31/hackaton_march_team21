from flask.globals import session
import boto3
from werkzeug.utils import secure_filename
from os import path, remove

import urllib.parse as urlparse
from ..config import AWS_BUCKET_NAME, AWS_ACCESS_KEY, AWS_SECRET_KEY

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MEDIA_FOLDER = 'media/'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class S3Bucket:
  
    def __init__(self):
     
     
        self.session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
            
   
    def upload(self, file):
        """
        This method is called when you want to upload an image
        The file url is returned from AWS
        """
        if file and allowed_file(file.filename):

            secure_file = secure_filename(file.filename)
            

            file.save(f'{MEDIA_FOLDER}{secure_file}') # save 
        
            s3_resource = self.session.resource('s3')

            bucket = s3_resource.Bucket(AWS_BUCKET_NAME)

            bucket.upload_file(Filename=f'{MEDIA_FOLDER}{secure_file}', Key=f'{MEDIA_FOLDER}{secure_file}')
            
            # check if the file is successfully created
            if path.exists(f'{MEDIA_FOLDER}{secure_file}'):
                # remove the file
                remove(f'{MEDIA_FOLDER}{secure_file}')

                return f'https://{AWS_BUCKET_NAME}.s3-eu-west-1.amazonaws.com/{MEDIA_FOLDER}{secure_file}'
            else:
                raise Exception(f'Error: {secure_file} does not exist.')

        else: 

            raise Exception('File type is not allowed')

  
    def delete_obj(self, img_url=''):

        try:
            parsed = urlparse.urlparse(img_url)
            print(str(parsed.path[1:]))
            s3_resource = self.session.resource('s3')

            bucket = s3_resource.Bucket(AWS_BUCKET_NAME)
            response = bucket.delete_objects(
            Delete={
                'Objects': [
                    {
                        'Key': str(parsed.path[1:])
                    },
                ],
                'Quiet': True
            }
        
        )
        except: 
            raise Exception('Fail to destroy image from AWS')