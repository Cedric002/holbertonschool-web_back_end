#!/usr/bin/env python3

from pymongo import MongoClient

"Returns the list of school that have a specific topic"


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school names that have the specified topic

    mongo_collection is the MongoDB collection object
    topic is the topic to search for
    """
    cursor = mongo_collection.find({"topic": topic})

    schools = []

    for document in cursor:
        schools.append(document['name'])

    return schools
