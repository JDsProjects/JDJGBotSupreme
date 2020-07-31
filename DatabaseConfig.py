import os
import pymongo
DB_logindetails = str(os.environ['DB_data'])

DB_client = pymongo.MongoClient(DB_logindetails)

db = DB_client.db_name
content_database=db.list_collection_names()
db.users_testing.create_index([('user_id', pymongo.ASCENDING)],unique=True)