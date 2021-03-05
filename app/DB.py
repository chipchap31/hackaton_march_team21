import pymongo
import os






class Database:
    
    # file out of app context, so just we just use the os module     
    client = pymongo.MongoClient(os.getenv('MONGO_URI'))[os.getenv('MONGO_DATABASE')]

