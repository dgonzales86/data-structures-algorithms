"""HashTable is the custom hash table implementation class.
   __init__ : Initializes instance of HashTable with 40 empty buckets
   hash_fx : Hash method runs key through hash calculation to determine storage location.
   insert_item: Method to insert item into hash table, uses hash method on specified key
   """

import csv
from model.package import Package


class HashTable:

    # Initializes hash table with a default size of 40 buckets
    def __init__(self, size=40):
        self.__map = [None] * size

    # Runs key through hash calculation to determine storage location
    # Time complexity, O(1) as will always be same number of operations for a given key.
    def hash_fx(self, key):
        my_hash = 0
        my_hash = (key * 37) % len(self.__map)
        return my_hash

    # Utilizes hash method on provided key to determine storage location of value.
    # Time complexity, O(1) as appending will take the same number of operations per item appended.
    def insert_item(self, key, value):
        key_hash = self.hash_fx(key)
        if self.__map[key_hash] is None:
            self.__map[key_hash] = []
        self.__map[key_hash].append([key, value])

    # Returns contents of hash 'bucket' by a specified key.
    # Accounts for chaining by searching bucket using a for loop within a nested list.
    # Time complexity, O(1) as items are evenly distributed using hash function and can be retrieved by key with
    # a constant number of operations.
    def lookup_item(self, key):
        key_hash = self.hash_fx(key)
        container = self.__map[key_hash]
        if container is not None:
            for i in range(len(self.__map[key_hash])):
                if container[i][0] == key:
                    return container[i][1]
        return None

    # Prints elements of hash table, in the scope of this project, package objects.
    # Time complexity, O(N) as method depends on N number of items in hash table.
    def print_map(self):
        for i, val in enumerate(self.__map):
            print(i, ": ", val)


# Non-class method that is passed a path to csv file and a hash table object.
# Utilizes python's csv reader to read and parse package information from provided csv file.
# Stores parsed information into a package object and inserts into the hash table object.
# Time complexity, O(M * N) as the while loop executes M times independently of the for loop, while the file has rows
# to be read. The for loop executes N times independently of the while loop for each column in the csv file.
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
            package = Package(package_id, address, city, state, zip_code, delivery_deadline, mass)

            # print(package)
            package_hash_table.insert_item(int(package_id), package)

        return package_hash_table
