class HashTable:

    def __init__(self, size=40):
        self.data_map = [None] * size

    def hash_fx(self, key):
        my_hash = 0
        my_hash = (key * 37) % len(self.data_map)-1
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.hash_fx(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])