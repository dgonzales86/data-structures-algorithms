"""HashTable is the custom hash table implementation class.
   __init__ : initializes instance of HashTable with 40 empty elements
   hash_fx : custom hash function
   """

import csv
from model.package import Package


class HashTable:

    def __init__(self, size=40):
        self.__map = [None] * size

    def hash_fx(self, key):
        my_hash = 0
        my_hash = (key * 37) % len(self.__map)
        return my_hash

    def insert_item(self, key, value):
        key_hash = self.hash_fx(key)
        if self.__map[key_hash] is None:
            self.__map[key_hash] = []
        self.__map[key_hash].append([key, value])

    def lookup_item(self, key):
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


def extract_csv(path, package_hash_table):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)

        for column in csv_reader:
            package_id = column[0]
            address = column[1]
            city = column[2]
            state = column[3]
            zip_code = column[4]
            delivery_deadline = column[5]
            mass = column[6]
            package_status = column[7]
            package = Package(package_id, address, city, state, zip_code, delivery_deadline, mass,
                              package_status)

            value = package

            package_hash_table.insert_item(int(package_id), value)

        return package_hash_table
