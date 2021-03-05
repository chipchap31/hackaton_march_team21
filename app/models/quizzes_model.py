from ..DB import Database

QUIZZES_COLLECTION = 'quizzes'

class QuizzesModel(Database): 
    def __init__(self):

        self.default = {'quizzes':[
            {
            'question': '',
            'correctAnswer': 'a',
            'options': 
                {
                    'a': 'Lorem Ipsum doner kebab mixed kebab',
                    'b': 'Lorem Ipsum doner kebab mixed kebab',
                    'c': 'Lorem Ipsum doner kebab mixed kebab'
                }
            }
            
        ]}

    
    def fetch_all(self):
        collection = self.client[QUIZZES_COLLECTION]
        doc_list = []
        for doc in collection.find({}):

            doc_list.append(doc)

   
        return doc_list
        



    def insert_one(self):
        collection = self.client[QUIZZES_COLLECTION]
        doc = collection.insert_one(self.default)

        print(doc.inserted_id)