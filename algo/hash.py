"""HashTable is the custom hash table implementation class.
   __init__ : initializes instance of HashTable with 40 empty elements
   hash_fx : custom hash function
   """


class HashTable:

    def __init__(self, size=40):
        self.__map = [None] * size

    def hash_fx(self, key):
        my_hash = 0
        my_hash = (key * 37) % len(self.__map) - 1
        return my_hash

    def set_item(self, key, value):
        key_hash = self.hash_fx(key)
        if self.__map[key_hash] is None:
            self.__map[key_hash] = []
        self.__map[key_hash].append([key, value])

    def get_item(self, key):
        key_hash = self.hash_fx(key)
        container = self.__map[key_hash]
        if container is not None:
            for i in range(len(self.__map[key_hash])):
                if container[i][0] == key:
                    return container[i][1]
        return None

    def print_map(self):
        for i, val in enumerate(self.__map):
            print(i, ": ", val)