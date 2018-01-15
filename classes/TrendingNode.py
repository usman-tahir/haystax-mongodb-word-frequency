
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

    def concatenate(self, y):
        current = self

        while current.has_next():
            current = current.next
        current.next = y
        return self

    def search(self, position = 1):
        if position <= 0:
            raise ValueError("An invalid position was entered - enter a position between 1 and %s, inclusive." % str(self.length()))
        
        current = self
        index = 0

        # account for an offset
        while index < position - 1:
            current = current.next
            index += 1
        return current

    def __str__(self):
        return "Data: %s\nHas Next: %s" % (self.data, str(self.has_next()))