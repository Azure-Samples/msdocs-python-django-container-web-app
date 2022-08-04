import os
import pymongo
from datetime import datetime
from bson import ObjectId

def get_collection():
    # Get connection info from environment variables
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    DB_NAME = os.getenv('DB_NAME')
    COLLECTION_NAME = os.getenv('COLLECTION_NAME')
    
    # Create a MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)
    try:
        client.server_info() # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")

    collection = create_database_unsharded_collection(client, DB_NAME, COLLECTION_NAME)
    return collection

def create_database_unsharded_collection(client, DB_NAME, COLLECTION_NAME):
    """Create sample database with shared throughput if it doesn't exist and an unsharded collection"""
    db = client[DB_NAME]

    # Create database if it doesn't exist
    if DB_NAME not in client.list_database_names():
        # Database with 400 RU throughput that can be shared across the DB's collections
        db.command({'customAction': "CreateDatabase", 'offerThroughput': 400})
        print("Created db {} with shared throughput". format(DB_NAME))
    
    # Create collection if it doesn't exist
    if COLLECTION_NAME not in db.list_collection_names():
        # Creates a unsharded collection that uses the DBs shared throughput
        db.command({'customAction': "CreateCollection", 'collection': COLLECTION_NAME})
        print("Created collection {}". format(COLLECTION_NAME))
        print("Collection name {}". format(db.COLLECTION_NAME))
    
    return db[COLLECTION_NAME]


def create_restaurant_record(name, street_address, description):
    ts = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    restaurant_record = {
		"type": "restaurant",
		"name": name,
		"street_address": street_address,
		"description": description,
        "create_date":ts,
    }
    return restaurant_record

def create_review_record(restaurant_id, user_name, rating, review_text):
    ts = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    review_record = {
        "restaurant": ObjectId(restaurant_id),
		"type": "review",
		"user_name": user_name,
		"rating": int(rating),
		"review_text": review_text,
		"review_date": ts,
    }
    return review_record