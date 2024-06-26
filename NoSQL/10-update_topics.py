#!/usr/bin/env python3

"Changes all topics in a MongoDB collection"


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document in a MongoDB collection
    based on the school name

    mongo_collection is The MongoDB collection object
    name is the name of the school to update
    topics is the list of topics approached in the school.
    """
    result = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return result.modified_count
