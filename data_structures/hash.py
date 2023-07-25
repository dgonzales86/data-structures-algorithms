import csv
from model.package import Package


class HashTable:

    # Hash table constructor with a default size of 40 buckets
    # Time complexity of O(N) for the creation of a list of size N
    # Space complexity O(N) for the space requirements of N buckets to store key-value pairs.
    def __init__(self, size=40):
        self.__map = [None] * size

    # Runs key through hash calculation to determine storage location
    # Time complexity, O(1) as will always be same number of operations for a given key.
    # Space complexity, O(1) as the operation is fixed and uses constant space each time it is run and stores variables.
    def hash_fx(self, key):
        my_hash = 0
        my_hash = (key * 37) % len(self.__map)
        return my_hash

    # Utilizes hash method on provided key to determine storage location of value and appends to hash table.
    # Time complexity, O(1) as appending will take the same number of operations per item appended.
    # Space complexity, O(1) as the space required for this method isn't dependent on the size of hash table
    # and uses constant space each time method runs.
    def insert_item(self, key, value):
        key_hash = self.hash_fx(key)
        if self.__map[key_hash] is None:
            self.__map[key_hash] = []
        self.__map[key_hash].append([key, value])

    # Returns contents of hash 'bucket' by a specified key.
    # Accounts for chaining by searching bucket using a for loop within a nested list.
    # Time complexity, O(1) as items are evenly distributed using hash function and can be retrieved by key with
    # a constant number of operations as there are no collisions within this program. Note* if another hash
    # method were implemented which led to several collisions, the worst case scenario for this method would be O(N).
    # Space complexity, considered to be O(1) as the method does not depend on the number of elements in the hash table.
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
# Time complexity, O(N * M) as the method depends on the number of columns, and rows in a given csv file.
# Space complexity, O(M * N). Since the method's memory requirements are dependent on the number of rows and columns,
# the method's space requirement grows in linear proportion to the number of columns and rows.
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
