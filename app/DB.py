import pymongo
import os
from . import config



class Database:
    
    # file out of app context, so just we just use the os module     
    client = pymongo.MongoClient(config.MONGO_URI)[config.MONGO_DATABASE]

