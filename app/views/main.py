from flask import Blueprint, render_template





main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
@main_blueprint.route('/index')
def index():


    return render_template('index.html')