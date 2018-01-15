from collections import Counter
import json
class TrendingWords():
    def __init__(self, timestamp = "", trending_words = []):
        self.timestamp = timestamp
        self.trending_words = trending_words
    
    def get_most_trending(self):
        counts = Counter(self.trending_words)
        return counts.most_common(1)[0] # return the first most trending word as a tuple

    def format(self):
        output = {
            "timestamp": self.timestamp,
            "trending_words": self.trending_words
        }
        return json.dumpscl(output)

    def get_most_trending_count(self):
        return self.get_most_trending()[1]
    
    def __str__(self):
        return self.format()