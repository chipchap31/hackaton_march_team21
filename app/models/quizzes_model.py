from ..DB import Database

QUIZZES_COLLECTION = 'quizzes'

class QuizzesModel(Database): 
    def __init__(self):

        self.default = {
            'question': '',
            'correctAnswer': 'a',
            'options': 
                {
                    'a': '',
                    'b': '',
                    'c': ''
                }
            }
            
        

    
    def fetch_all(self):
        collection = self.client[QUIZZES_COLLECTION]
        doc_list = []
        for doc in collection.find({}):

            doc_list.append(doc)

   
        return doc_list
        



    def create(self, data):
        collection = self.client[QUIZZES_COLLECTION]

        self.default.update(data)

        doc = collection.insert_one(self.default)

        return doc.inserted_id