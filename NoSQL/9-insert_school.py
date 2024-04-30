#!/usr/bin/env python3

"Inserts new documents in a MongoDB collection"


def insert_school(mongo_collection, **kwargs):
    """
    Inserts the new document based on kwargs and
    returns the new document's _id
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return str(result.inserted_id)
