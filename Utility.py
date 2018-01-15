import json
import datetime
import random

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
        trending_words_data.append(t)
    return trending_words_data

def generate_day(trending_words_for_day):
    day = TrendingNode(trending_words_for_day[0])

    for x in range(1, 24):
        day.concatenate(TrendingNode(trending_words_for_day[x]))
    return day

def main():
    words = read_words("./data/words.txt")
    data_for_collection = [] # contains a list of days represented as hour-based linked-lists
    
    # generate trends for sample days
    days = ["01/14/2018", "01/15/2018", "01/16/2018"]
    for day in days:
        trend_for_day = generate_day(generate_trending_words_for_day(day, words))
        data_for_collection.append(trend_for_day)
    
if __name__ == "__main__":
    main()