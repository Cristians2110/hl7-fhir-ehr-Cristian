from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://Cristian2110:abcde@cluster0.tdjsw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection
def insert_patient():
    collection = connect_to_mongodb("SamplePatientService", "patients")
    if collection:
        result = collection.insert_one({"name": "Paciente 1", "age": 30})
        print(f"✅ Documento insertado con ID: {result.inserted_id}")

insert_patient()
