from flask import Blueprint, render_template
from ..models.quizzes_model import QuizzesModel



quizzes_view = Blueprint('quizzes_view', __name__)

@quizzes_view.route('/quizzes', methods=['GET', 'POST'])
def get_quizzes():

    return render_template('quizzes.html', quizzes=QuizzesModel().fetch_all())