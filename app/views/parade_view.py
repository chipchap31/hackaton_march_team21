from flask import Blueprint,render_template, jsonify, flash
from flask.globals import request
from flask.helpers import make_response
from ..models.parade_model import ParadeModel
from ..services.s3bucket import S3Bucket
from flask_mail import Message
from ..Mailer import mail
from itsdangerous import URLSafeSerializer
import os



serializer = URLSafeSerializer(os.getenv('SECRET_KEY'))

parade_view = Blueprint('parade_view', __name__)

@parade_view.route('/parade')
def parade_main():

    return render_template('parade.html')


@parade_view.route('/parade/join', methods=['POST'])
def parade_register():
    if request.method == 'POST':
        data =request.form.to_dict()
        

        msg = Message('Confirm your email',sender=os.getenv('EMAIL_SENDER'),
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
        return request.form.get('email')

    return render_template('parade.html')


@parade_view.route('/parade/confirm/<token>')
def parade_confirm(token):
    
    
    data = serializer.loads(token, salt='email-confirm')
    try: 
        
        data_id = ParadeModel().create({**data})
        
        resp = make_response(jsonify(data), 200)

        resp.set_cookie('parade_id', data_id)

        return resp
    except Exception as e:
        flash(e)    

        return jsonify({'Error': 'dsads'}),404
    


@parade_view.route('/parade/fetch')
def parade_fetch():
    parade = {
    "floats": [
        {
        "name": "John Doe",
        "country": "Ireland",
        "image": "https://www.irishtimes.com/polopoly_fs/1.3824661.1552497679!/image/image.jpg_gen/derivatives/box_1200_630/image.jpg",
        "message": "Happy St Patrick's Day!"      
        },
        {
        "name": "Mary Smith",
        "country": "Germany",
        "image": "https://www.shamrockeradventures.com/media/14828/st-patrciks-day-tours-mobile.jpg?anchor=center&mode=crop&rnd=132192357100000000",
        "message": "Have a great day!"      
        },
        {
        "name": "Supervalu",
        "country": "Ireland",
        "image": "https://cf-images.eu-west-1.prod.boltdns.net/v1/jit/4221396001/f7b10f7b-3a37-4b3a-8659-8e8438b39921/main/1280x720/59s466ms/match/image.jpg",
        "message": "Greetings from Supervalu"      
        },
        {
        "name": "Egg",
        "country": "USA",
        "image": "https://pbs.twimg.com/profile_images/482980960258908160/XawV_qBz_400x400.jpeg",
        "message": "It's a jumping off point."      
        },
        {
        "name": "Sweet Dee",
        "country": "Canada",
        "image": "https://external-preview.redd.it/8Rzj3TN_BaZ5rqoWGz799K9-w8ZMiwaPhnYVWNQcUiE.jpg?auto=webp&s=e7034460cab0303de18cabd7edbf7259a440c244",
        "message": "Come on down to Paddy's!"      
        }
    ]
    }
    return jsonify(parade), 200