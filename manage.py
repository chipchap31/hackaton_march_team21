from sys import argv

FIRST_ARGUMENT = 1
SECOND_ARGUMENT = 2

from app.models.quizzes_model import QuizzesModel

if argv[FIRST_ARGUMENT] == 'quiz': 


    if argv[SECOND_ARGUMENT] == 'create':
        data = {
            'question': '',
            'options': {}
        }
        

        
        question = input('Please enter your question: ')
       
        data['question'] = question
        
        for letter in ['a', 'b', 'c']:
             
            possible_answer = input(f'Enter the possible answer for letter {letter}: ')
            data.update({'options': {
                **data['options'],
                letter: possible_answer
            }})
            

        right_answer = input('Enter the letter of the answer: ')

        data['correctAnswer'] = right_answer.lower()
        

        try:
            new_quiz = QuizzesModel().create(data)
            print(f'Succesfully created new quiz with id={new_quiz}')
        except Exception as e:
            print(e)
        