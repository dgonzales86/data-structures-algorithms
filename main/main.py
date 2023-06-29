import util
from algo.hash import HashTable
from util import extract_csv_hash
from model import trucks
import threading

my_hash_table = HashTable()

# parses .csv file and populates hash map
file_path = "util/packageDestCSV.csv"
extract_csv_hash.extract_csv(file_path, my_hash_table)

my_hash_table.set_item(41,'test address')

my_hash_table.print_map()
