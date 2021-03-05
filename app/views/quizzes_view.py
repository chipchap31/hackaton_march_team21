from flask import Blueprint, render_template
from ..models.quizzes_model import QuizzesModel



quizzes_blueprint = Blueprint('quizzes_blueprint', __name__)

@quizzes_blueprint.route('/quizzes', methods=['GET', 'POST'])
def get_quizzes():

    return render_template('quizzes.html', quizzes=QuizzesModel().fetch_all())