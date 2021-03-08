from pymongo import collection
from app.services.s3bucket import S3Bucket

from ..DB import Database
from datetime import datetime
from bson.objectid import ObjectId
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

      

        if self.fetch_one(email=data_to_insert['email']): 
            return False
        else: 

            self.default.update(data_to_insert)
            doc = collection.insert_one(self.default)
            
            return doc.inserted_id 

    def fetch_all(self):
        collection = self.client[PARADE_COLLECTION]
        doc_list = []
        for doc in collection.find({}):

            doc_list.append({**doc, '_id': str(doc['_id'])})

   
        return doc_list
    
    def fetch_one(self, email='', id=''):

        
        collection = self.client[PARADE_COLLECTION]

        if email != '': 
            return collection.find_one({'email': email})
        elif id != '':
            return collection.find_one({'_id': ObjectId(id)})

        else: 

            raise ValueError('No argument provided')
   
            
    def change_one(self, data):
        collection = self.client[PARADE_COLLECTION]
        newvalues = { "$set": { "image": data['image']} }
        collection.update_one({'_id': ObjectId(data['parade_id'])}, newvalues)
            
        return True
    def destroy_one(self,cookie_id):

        collection = self.client[PARADE_COLLECTION]
        try:

            collection.delete_one({ "_id": ObjectId(cookie_id) })
            return True
        except:

            return False
                
