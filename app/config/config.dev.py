import os

DEBUG=True
ENV='development'
AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY') 
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
AWS_BUCKET_NAME=os.getenv('AWS_BUCKET_NAME')