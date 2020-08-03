class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.items = [None for i in range(capacity)]

    def append(self, item):
        if self.capacity == self.count:
            self.items[0] = item
            self.count = 1
        else:
            self.items[self.count] = item
            self.count += 1

    def get(self):
        if self.count > 0:
            return [i for i in self.items if i]