import util
from algo.hash import HashTable
from util import extract_csv_hash
import threading

my_hash_table = HashTable()

# parses .csv file and populates hash map
file_path = "util/packageDestCSV.csv"
extract_csv_hash.extract_csv(file_path, my_hash_table)

#my_hash_table.set_item(41,'test address')

#my_hash_table.print_map()


my_hash_table.lookup_item(21)

print(my_hash_table.lookup_item(27))

for i in range (1,40):
    print(my_hash_table.lookup_item(i).address)
#print(my_hash_table.get_item(41))

print(my_hash_table.lookup_item(27).address)