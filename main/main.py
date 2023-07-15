import algo.hash
import model.trucks
from algo import distance_array
from algo.distance_array import Distance_Array
from algo.graph import Graph

from algo.hash import HashTable

import threading

my_hash_table = HashTable()

# parses .csv file and populates hash map
package_file = "util/packageDestCSV.csv"
algo.hash.extract_csv(package_file, my_hash_table)

address_file = "util/addresses.csv"
distance_table = 'util/Distance_Table_2.csv'
# distance_table = "util/Distance_Table.csv"

# for i in range(1, 40):
#     print(my_hash_table.lookup_item(i).address)
#
# my_graph = Graph()
#
# my_graph.print_distance_graph()
#
# my_graph = Graph()
#
# my_graph.csv_parse_graph(address_file)
# print(my_graph.distance_graph)
# start_vertex = '4001 South 700 East'
#
#
# def distance_from(address1, address2):
#     distance = address2 - address1
#     return distance
#
#
# truck1 = model.trucks.DeliveryTruck(my_hash_table.lookup_item(1))
#
# truck1.load_truck(1)
# truck1.load_truck(22)
# truck1.load_truck(32)
# print(truck1.packages)
# truck1.unload_truck(22)
#
# print(my_hash_table.lookup_item(5))
distance = Distance_Array()
Distance_Array.parse_distance(distance, distance_table)

print()
