from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://Cristian2110:abcdef123@cluster0.tdjsw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = SamplePatientService
    collection_name = patients
    collection = connect_to_mongodb(uri, db_name, collection_name)
    return collection

