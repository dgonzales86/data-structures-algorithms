import csv
from algo.hash import HashTable


def extract_csv(path, package_hash_table):

    with open(path, 'r') as file:
        csv_reader = csv.reader(file)

        for column in csv_reader:
            key = column[0]
            value = column[1]

            package_hash_table.set_item(int(key), value)

        return package_hash_table
