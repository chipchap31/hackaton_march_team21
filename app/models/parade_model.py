from ..DB import Database
from datetime import datetime
PARADE_COLLECTION = 'parades'



class ParadeModel:

    def __init__(self) -> None:
        self.default = {
            '_user_id': '',
            'message': '',
            'img_url': ''
        }


    def insert_one(self, data_to_insert):
        
        collection = self.client[PARADE_COLLECTION]
        self.default.update(data_to_insert)
        

        collection.insert_one(self.default)
        