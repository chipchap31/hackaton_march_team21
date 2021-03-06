import os
from dotenv import load_dotenv
load_dotenv()

DEBUG=os.getenv('DEBUG')
ENV=os.getenv('ENV')
AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY') 
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
AWS_BUCKET_NAME=os.getenv('AWS_BUCKET_NAME')
MONGO_URI=os.getenv('MONGO_URI')
MONGO_DATABASE=os.getenv('MONGO_DATABASE')
SECRET_KEY=os.getenv('SECRET_KEY')
MAIL_SERVER= 'smtp.gmail.com'
MAIL_PORT= 465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME=os.getenv('MAIL_USERNAME')
MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
HOST=os.getenv('HOST')
