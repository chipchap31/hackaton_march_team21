from ..DB import Database
from datetime import datetime
PARADE_COLLECTION = 'parades'



class ParadeModel(Database):

    def __init__(self) -> None:
        self.default = {
            'name': '', 
            'country': '',
            'email': '',
            'message': '',
            'image': '',
            'created_at': datetime.now()
        }


    def create(self, data_to_insert):
        
        collection = self.client[PARADE_COLLECTION]

      

        if self.fetch_one(data_to_insert['email']): 
            raise Exception(f'{data_to_insert["email"]} already exist')
        else: 

            self.default.update(data_to_insert)
            doc = collection.insert_one(self.default)
            
            return doc.inserted_id 

    def fetch_one(self, email):

        collection = self.client[PARADE_COLLECTION]


        doc = collection.find_one({'email': email})

        return doc
       
            
            
            

    def destroy_one(cookie_id):

        pass

