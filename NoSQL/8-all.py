#!/usr/bin/env python3

"Lists all documents in a MongoDB collection"


def list_all(mongo_collection):
    """
    mongo_collection is The MongoDB collection and
    returns a list of all documents in the collection
    """
    try:
        documents = list(mongo_collection.find())
        return documents
    except Exception as e:
        print(f"Error: {e}")
        return []
