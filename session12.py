"""
    1. Register on MongoDB Atlas (GCP/AWS/Azure)
    2. MongoDB User -> ROLE ->Admin
    3. IP Whitelisiting -> 0.0.0.0/0
    4. Create DataBase with a collection
    5. pip install "pymongo[srv]" (ensure 1. internet 2. your venv selected)
    6. Run the sample code
"""

from pymongo import MongoClient
uri = "mongodb+srv://anjaniyt5_db_user:a22@cluster0.5oqijo8.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)



#access the database
db=client['anjani_m_db']
names=db.list_collection_names()
print(names)
