import json
import sys
import collections

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

# partition the data based on a timestamp
def partition_output(data):
    partitioned_results = collections.defaultdict(list)
    for d in data:
        partitioned_results[d["timestamp"][0:11]].append(d)
    return list(partitioned_results.values())

def main():
    mongo_data = retrieve_mongo_collection()
    partitioned_data = partition_output(mongo_data)

if __name__ == "__main__":
    main()