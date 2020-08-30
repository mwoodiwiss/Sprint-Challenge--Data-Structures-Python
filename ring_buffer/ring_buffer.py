class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.data_index = None

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.data_index] = item
            self.data_index = (self.data_index + 1) % self.capacity
        else:
            self.data.append(item)
            if len(self.data) == self.capacity:
                self.data_index = 0
            
    def get(self):
        print(self.data)
        return self.data