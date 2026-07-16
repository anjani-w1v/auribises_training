from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://xxqw@cluster0.eh8zx.gcp.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the DataBase
db = client['x']
names = db.list_collection_names()
print(names)