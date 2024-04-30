#!/usr/bin/env python3

"Returns the list of school that have a specific topic"


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school names that have the specified topic
    
    mongo_collection is the MongoDB collection object
    topic is the topic to search for
    """
    schools = list(mongo_collection.find({"topics": topic}, {"name": 1}))

    school_names = [school["name"] for school in schools]
    
    return school_names
