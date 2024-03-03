import pymongo
import json

# Define MongoDB connection details
mongo_uri = "mongodb+srv://vipankumar98780:mongodb@cluster0.ovcufp6.mongodb.net/mongodbVSCodePlaygroundDB"

# Create a MongoDB client
client = pymongo.MongoClient(mongo_uri)

# Specify the database name
db_name = "test_db"  # Replace with your desired database name

# Create a new database or switch to an existing one
db = client[db_name]

# Add a document to a collection
collection_name = "my_collection"
my_collection = db[collection_name]

data_to_insert = {"name": "John", "age": 30}
result = my_collection.insert_one(data_to_insert)
print(f"Inserted document with _id: {result.inserted_id}")

# Get the database size information
db_stats = db.command("dbstats")
print(f"Size information for {db_name}:")
print(json.dumps(db_stats, indent=4))


# Retrieve and print all documents in the collection
cursor = my_collection.find({})
for document in cursor:
    # Convert ObjectId to string for JSON serialization
    document['_id'] = str(document['_id'])
    print(json.dumps(document, default=str, indent=4))

client.close()
