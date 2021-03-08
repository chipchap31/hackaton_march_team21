from flask import Blueprint, render_template





main_view = Blueprint('main_view', __name__)


@main_view.route('/')
@main_view.route('/index')
def index():


    return render_template('index.html')



@main_view.route('/history')
def history():

    return render_template('history.html')