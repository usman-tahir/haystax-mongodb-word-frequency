import json
import sys

from pymongo import MongoClient
from classes.TrendingNode import *

def retrieve_mongo_collection():
    formatted_output = []
    connection = MongoClient(sys.argv[1])
    collection = connection.word_frequencies.word_frequencies
    retrieval = collection.find()

    for r in retrieval:
        output = {
            "timestamp": r["timestamp"],
            "trending_words": r["trending_words"]
        }
        formatted_output.append(output)
    return formatted_output

def main():
    # print(retrieve_mongo_collection())

if __name__ == "__main__":
    main()