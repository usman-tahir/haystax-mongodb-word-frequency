import json
import sys
import collections

from pymongo import MongoClient
from classes.TrendingWords import *
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

def generate_trending_words_for_day(trending_data_json):
    trending_words_data = []
    
    for x in range(0, 24):
        timestamp = trending_data_json[x]["timestamp"]
        trending_words = trending_data_json[x]["trending_words"]
        t = TrendingWords(timestamp, trending_words)
        trending_words_data.append(t)
    return trending_words_data

def generate_day(trending_words_for_day):
    day = TrendingNode(trending_words_for_day[0])

    for x in range(1, 24):
        day.concatenate(TrendingNode(trending_words_for_day[x]))
    return day

def main():
    mongo_data = retrieve_mongo_collection()
    partitioned_data = partition_output(mongo_data)

    formatted_days = []

    for x in range(0, len(partitioned_data)):
        trending_words = generate_trending_words_for_day(partitioned_data[x])
        day = generate_day(trending_words)
        formatted_days.append(day)
    
    print(formatted_days)

if __name__ == "__main__":
    main()