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
        

def main():
    words = read_words("./data/words.txt")

if __name__ == "__main__":
    main()