import algo.hash
from algo.graph import Graph
from algo.hash import HashTable
from model import package
from model.driver import Truck_Driver
from model.trucks import DeliveryTruck
import threading

driver1 = Truck_Driver(1, 'Wayne')
driver2 = Truck_Driver(2, 'Garth')

truck1 = DeliveryTruck(1, 1)
truck2 = DeliveryTruck(2, 2)
truck3 = DeliveryTruck(3, None)

# creates hash table object
my_hash_table = HashTable()

# parses .csv file and populates hash map
package_file = "util/packageDestCSV.csv"
algo.hash.extract_csv(package_file, my_hash_table)

# variable for string path to address file
address_file = "util/addresses.csv"

# variable for string path to distance table file
distance_table = "util/Distance_Table.csv"

for i in range(1, 41):
    print(my_hash_table.lookup_item(i))

# creates address graph object
address_graph = Graph()

address_graph.csv_parse_graph(address_file)
#print(address_graph.distance_graph)

# loading truck 1
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())
truck1.load_truck(my_hash_table.lookup_item())


truck1.print_truck_status()

# loading truck 2
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())
truck2.load_truck(my_hash_table.lookup_item())

truck2.print_truck_status()

# example of how to access package objects
# for package in truck1.loaded_packages:
#     print(package.address)



