#!/usr/bin/env python3

"Provides some stats about Nginx logs stored in MongoDB"

from pymongo import MongoClient
import pymongo

if __name__ == "__main__":

    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']  # Assuming MongoDB is running locally on default port
    collection = db["nginx"]

    # Get the total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get the number of documents for each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{count}")

    # Get the number of documents with method=GET and path=/status
    count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"\tmethod=GET, path=/status: {count}")d
