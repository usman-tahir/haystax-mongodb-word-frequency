import json
import sys
import collections
import numpy

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
    # print(day.last())
    return day

def determine_daily_trending_word(day):
    # using an underscore in order to resolve any key/trending word issues
    overall_trending_word = {
        "_word": "",
        "_count": 0
    }

    current = day
    index = 1
    while index <= current.length():
        data = current.search(index).data
        if overall_trending_word["_count"] <= data.get_most_trending_count():
            new_overall_trending_word = {
                "_word": data.get_most_trending_word(),
                "_count": data.get_most_trending_count()
            }
        overall_trending_word = new_overall_trending_word
        index += 1
    return overall_trending_word

def determine_overall_trending_word(days):
    overall_trending_word = {
        "_word": "",
        "_count": 0
    }

    for day in days:
        overall_trending_word_for_day = determine_daily_trending_word(day)
        if overall_trending_word_for_day["_count"] >= overall_trending_word["_count"]:
            overall_trending_word = overall_trending_word_for_day
    return overall_trending_word

# based on the past 24 hours
def determine_recent_trending_word(days):
    return determine_daily_trending_word(days[-1])

def generate_trend_for_words(day):
    word_trends = {}
    linear_fit_trend = []
    current = day
    index = 1

    while index <= current.length():
        current_data = current.search(index).data
        current_trending_words_set = list(set(current_data.trending_words))
        for word in current_trending_words_set:
            word_count = current_data.trending_words.count(word)
            if word in word_trends:
                word_trends[word].append(word_count)
            else:
                word_trends[word] = []
                word_trends[word].append(word_count)
        index += 1
    for word in word_trends.keys():
        linear_fit_trend.append(generate_linear_fit(word, word_trends[word]))

    return linear_fit_trend

def generate_linear_fit(word, data):
    x = numpy.arange(0, len(data))
    y = numpy.array(data)
    z = numpy.polyfit(x, y, 1)
    return (word, z[1])

def determine_most_trending_word(days):
    word_trends = []

    word_trends.append(generate_trend_for_words(days[1]))
    word_trends.append(generate_trend_for_words(days[2]))
    word_trends = sum(word_trends, [])
    word_trends.sort(key = lambda t: t[1])
    return word_trends[-1][0]

def generate_results(days):
    print("The word that occurs most frequently in the entire data set: %s" % determine_overall_trending_word(days)["_word"])
    print("The word that occurs most frequently in the last 24 hours: %s" % determine_recent_trending_word(days)["_word"])
    print("The word that is trending the most: %s" % determine_most_trending_word(days))

def main():
    mongo_data = retrieve_mongo_collection()
    partitioned_data = partition_output(mongo_data)

    formatted_days = []

    for x in range(0, len(partitioned_data)):
        trending_words = generate_trending_words_for_day(partitioned_data[x])
        day = generate_day(trending_words)
        formatted_days.append(day)
    
    generate_results(formatted_days)

if __name__ == "__main__":
    main()