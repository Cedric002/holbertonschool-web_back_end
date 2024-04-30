#!/usr/bin/env python3

"Inserts new documents in a MongoDB collection"


def insert_school(mongo_collection, **kwargs):
    """
    Inserts the new document based on kwargs and returns
    _id of the new document

    **kwargs is Keyword arguments representing the fields and
    values of the new document
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return str(result.inserted_id)
