from pymongo import MongoClient

def auth(usr, pw):
    uri = "mongodb://" + usr + ":" + pw + "@ds157544.mlab.com:57544/apscm3"
    
    return MongoClient(uri)