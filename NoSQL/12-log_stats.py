#!/usr/bin/env python3

"Provides some stats about Nginx logs stored in MongoDB"

from pymongo import MongoClient
import pymongo

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['logs']  # Assuming MongoDB is running locally on default port

# Query the nginx collection
collection = db['nginx']

# Total number of documents in the collection
total_docs = collection.count_documents({})
print(f"{total_docs} logs")

# Count of documents for each HTTP method
methods_counts = {
    "GET": 0,
    "POST": 0,
    "PUT": 0,
    "PATCH": 0,
    "DELETE": 0
}

# Counting documents for each method
for doc in collection.find():
    method = doc.get('method', '')
    if method in methods_counts:
        methods_counts[method] += 1

# Displaying the counts
for method, count in methods_counts.items():
    print(f"\t{count} {method}")

# Count of documents with method=GET and path=/status
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"\t{get_status_count} GET /status")
