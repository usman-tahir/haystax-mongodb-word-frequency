
class TrendingNode():
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def has_next(self):
        return self.next != None

    def length(self):
        if not self.has_next():
            return 1
        return 1 + self.next.length()

    def __str__(self):
        return "Data: %s\nHas Next: %s" % (self.data, str(self.has_next()))