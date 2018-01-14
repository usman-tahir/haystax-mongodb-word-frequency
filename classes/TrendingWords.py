from collections import Counter

class TrendingWords():
    def __init__(self, timestamp = "", trending_words = []):
        self.timestamp = timestamp
        self.trending_words = trending_words
    
    def get_most_trending(self):
        counts = Counter(self.trending_words)
        return counts.most_common(1)[0] # return the first most trending word as a tuple

    def get_most_trending_count(self):
        return self.get_most_trending()[1]
    
    def __str__(self):
        return "Timestamp: %s\nTrending words: %s" % (self.timestamp, str(self.trending_words))