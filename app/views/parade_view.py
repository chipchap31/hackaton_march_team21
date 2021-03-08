from flask import Blueprint, json,render_template, jsonify, flash, make_response
from flask.globals import request
from flask.wrappers import Response
from werkzeug.utils import redirect
from ..models.parade_model import ParadeModel
from ..services.s3bucket import S3Bucket
from flask_mail import Message
from ..Mailer import mail
from itsdangerous import URLSafeSerializer
import os
from ..config import MAIL_USERNAME,HOST
import webbrowser

serializer = URLSafeSerializer(os.getenv('SECRET_KEY'))

parade_view = Blueprint('parade_view', __name__)

@parade_view.route('/parade')
def parade_main():
    parade_exist = request.cookies.get('parade_id')

    return render_template('parade.html', parade_exist=parade_exist)


@parade_view.route('/parade/join', methods=['POST'])
def parade_register():
    if request.method == 'POST':
        data=request.form.to_dict()
        if data['email'] == '' or data['country'] == '' or data['name'] == '' or data['message'] == '':
            flash('All fields are required')
            return render_template('parade.html')
        msg = Message('Confirm your email',sender=MAIL_USERNAME,
                  recipients=[data['email']])

        data_to_dump = {
            **data
            }
        token = serializer.dumps(data_to_dump,salt='email-confirm')
        msg.html = f"""<html>
                        <body> 
                        <p>Hello {data['name']},</p>
                        
                      

                        <p>Please click the link below to confirm:</p>
                                <a style='margin-left:1em;' href='{os.getenv('HOST')}/parade/confirm/{token}'>{data['email']}</a>
                        <p>
                        Cheers,<br>
                        <span style='margin-left:1em;'>Virtual St. Patrick's Day Team</span>
                        </p>


                        </body>
                    </html>
                    """ 
                  


        mail.send(msg)
        return render_template('check_email.html')

    return render_template('parade.html')


@parade_view.route('/parade/confirm/<token>')
def parade_confirm(token):
    
    
    data = serializer.loads(token, salt='email-confirm')
  
 
        
    data_id = ParadeModel().create(data_to_insert=data)
    
    if data_id:

        resp = make_response(render_template('parade-confirmed.html'), 200)

        resp.set_cookie('parade_id', str(data_id).encode())

        return resp
    else: 

        return Response('You already have an account',500)
    


@parade_view.route('/parade/fetch')
def parade_fetch():
    
   
    parade = {
    "floats": ParadeModel().fetch_all()}
    return jsonify(parade), 200

@parade_view.route('/parade/upload', methods=['POST'])
def parade_upload():
    parade_id = request.cookies.get('parade_id')


    if request.method == 'POST':
        files = request.files['file']
       
        try: 

            ParadeModel().change_one({
                'image': S3Bucket().upload(files),
                'parade_id': parade_id
            })

            return redirect('/parade/watch')
        except Exception as e:

            print(e)


@parade_view.route('/parade/watch')
def parade_watch():
    

    return render_template('parade-watch.html', parades=ParadeModel().fetch_all())