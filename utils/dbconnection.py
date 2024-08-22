from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://patilharshad:VgEyLG5StaSiFHLG@usersdata.rdnnb.mongodb.net/?retryWrites=true&w=majority&appName=UsersData"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    db = client.usersdata
    collection_name = db["user_data"]
except Exception as e:
    print(e)