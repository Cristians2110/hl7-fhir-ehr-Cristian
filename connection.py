from pymongo import MongoClient
from pymongo.server_api import ServerApi

def connect_to_mongodb(db_name, collection_name):
    # URL de conexión a MongoDB
    uri = "mongodb+srv://Cristian2110:abcdef123@cluster0.tdjsw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    # Conectar al cliente de MongoDB
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    # Seleccionar la base de datos y la colección
    db = client[db_name]
    collection = db[collection_name]
    
    return collection

# Ejemplo de uso:
collection = connect_to_mongodb("SamplePatientService", "patients")
print("✅ Conectado a la colección:", collection)
