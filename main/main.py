import util
from algo.hash import HashTable
from util import extract_csv_hash

my_hash_table = HashTable()

file_path = "util/packageDestCSV.csv"
extract_csv_hash.extract_csv(file_path, my_hash_table)

my_hash_table.print_table()







