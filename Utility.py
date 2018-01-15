import json
import datetime
import random
import sys
from pymongo import MongoClient

from classes.TrendingWords import *
from classes.TrendingNode import *

def read_words(filename):
    return [word.strip("\n") for word in open(filename, "r").readlines()]

def generate_trending_words(words):
    return [random.choice(words) for x in range(0, 10)]

def generate_trending_words_for_day(day_string, words):
    day_string_parts = [int(part) for part in day_string.split("/")]
    trending_words_data = []
    
    for x in range(0, 24):
        timestamp = datetime.datetime(day_string_parts[2], day_string_parts[0], day_string_parts[1], x, 0, 0).strftime("%m/%d/%Y %H:%M:%S")
        t = TrendingWords(timestamp, generate_trending_words(words))
        trending_words_data.append(str(t))
    return trending_words_data

def generate_day(trending_words_for_day):
    day = TrendingNode(trending_words_for_day[0])

    for x in range(1, 24):
        day.concatenate(TrendingNode(trending_words_for_day[x]))
    return day

def generate_data_for_insertion(data):
    with open("./data/frequencies.json", "w") as output:
        json.dump(data, output)

def update_mongo_collection():
    word_frequency_data = [json.loads(data) for data in json.load(open("./data/frequencies.json"))]
    print(word_frequency_data)
    connection = MongoClient(sys.argv[1])
    collection = connection.word_frequencies.word_frequencies
    collection.insert(word_frequency_data)

def main():
    words = read_words("./data/words.txt")
    data_for_collection = [] # contains a list of days represented as hour-based linked-lists

    days = ["01/14/2018", "01/15/2018", "01/16/2018"]
    for day in days:
        trending_words_data = generate_trending_words_for_day(day, generate_trending_words(words))
        data_for_collection.append(trending_words_data)
    data_for_collection = sum(data_for_collection, []) # flatten the nested lists

    generate_data_for_insertion(data_for_collection)
    update_mongo_collection()
    
if __name__ == "__main__":
    main()