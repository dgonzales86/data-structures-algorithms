import algo.hash
import util
from algo.graph import Graph, dijkstra
from algo.hash import HashTable
from util import extract_csv_hash
import threading

my_hash_table = HashTable()

# parses .csv file and populates hash map
package_file = "util/packageDestCSV.csv"
algo.hash.extract_csv(package_file, my_hash_table)

address_file = "util/addresses.csv"
distance_table = "util/Distance_Table.csv"

#
# my_hash_table.insert_item(41, 'test address')
#
# my_hash_table.print_map()
#
# my_hash_table.lookup_item(21)
#
# print(my_hash_table.lookup_item(27))
#
# for i in range(1, 40):
#     print(my_hash_table.lookup_item(i).address)
#
#
# print(my_hash_table.lookup_item(27).address)

my_graph = Graph()
#
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')

# my_graph.add_edge('A', 'B', 10)
# my_graph.add_edge('A', 'C', 20)
# my_graph.add_edge('A', 'D', 30)
# my_graph.add_edge('B', 'D', 40)
# my_graph.add_edge('C', 'D', 50)
#
# my_graph.delete_vertex('D')
# my_graph.delete_vertex('D')
#
# my_graph.print_distance_graph()

my_graph = Graph()

my_graph.csv_parse_graph(address_file)

dijkstra(my_graph,)

# my_graph.print_distance_graph()

# ###############################loading graph###################################



