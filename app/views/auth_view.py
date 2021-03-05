from flask import Blueprint
from flask.templating import render_template



auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/register')
def register():

    pass 


    return render_template('register.html')