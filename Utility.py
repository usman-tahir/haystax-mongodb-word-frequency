import json
import datetime
import random

from classes.TrendingWords import *
from classes.TrendingNode import *

def read_words(filename):
    return [word.strip("\n") for word in open(filename, "r").readlines()]

def generate_trending_words(words):
    return [random.choice(words) for x in range(0, 10)]

def main():
    words = generate_trending_words(read_words("./data/words.txt"))
    print(words)

if __name__ == "__main__":
    main()