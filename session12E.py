from pymongo import MongoClient
from pymongo.server_api import ServerApi

class DBHelper:

    def __init__(self, db_name='anjani_m_db'):
        uri = "mongodb+srv://anjaniyt5_db_user:a22@cluster0.5oqijo8.mongodb.net/?appName=Cluster0"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        print('[DBHelper] Connection Created')

    def select_collection(self, collection_name='users'):
        self.collection = self.db[collection_name]
        print('[DBHelper] Collection Selected:"', collection_name)

    def save(self, document):
       inserted_id = self.collection.insert_one(document)
       print('[DBHelper] Document Saved. Id is:', inserted_id)