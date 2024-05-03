#!/usr/bin/env python3

"Provides some stats about Nginx logs stored in MongoDB"

from pymongo import MongoClient
import pymongo

if __name__ == "__main__":

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count total documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents by method
    methods_count = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "PATCH": 0,
        "DELETE": 0
    }

    for log in collection.find():
        method = log.get("method")
        if method in methods_count:
            methods_count[method] += 1

    for method, count in methods_count.items():
        print(f"\t{count} {method}")

    # Count documents with specific method and path
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"\t{get_status_count} GET /status")
