import datetime
import argparse
import data_structures.hash
from data_structures.graph import Graph
from data_structures.hash import HashTable
from model import package, trucks
from model.driver import Truck_Driver
from model.trucks import DeliveryTruck
from data_structures.distance_array import Distance_Array

import threading

driver1 = Truck_Driver(1, 'Wayne')
driver2 = Truck_Driver(2, 'Garth')

truck1 = DeliveryTruck(1, 1, datetime.timedelta(hours=8, minutes=0))
truck2 = DeliveryTruck(2, 2, datetime.timedelta(hours=9, minutes=5))
truck3 = DeliveryTruck(3, None, datetime.timedelta(hours=9, minutes=5))

print(truck1.current_time())

# creates hash table object
my_hash_table = HashTable()

# parses .csv file and populates hash map
package_file = "util/packageDestCSV.csv"
data_structures.hash.extract_csv(package_file, my_hash_table)

# variable for string path to address file
address_file = "util/addresses.csv"

# variable for string path to distance table file
distance_table = "util/Distance_Table_2.csv"

# for i in range(1, 41):
#     print(my_hash_table.lookup_item(i))

# creates address graph object
# address_graph = Graph()
# parse csv file into graph into vertex for graph
# address_graph.csv_parse_graph(address_file)
# print(address_graph.distance_graph)

# creates 2d array
distance_array = Distance_Array()
distance_array.parse_distance(distance_table)

# loading truck 1
truck1.load_truck(my_hash_table.lookup_item(14))
truck1.load_truck(my_hash_table.lookup_item(15))
truck1.load_truck(my_hash_table.lookup_item(16))
truck1.load_truck(my_hash_table.lookup_item(13))
truck1.load_truck(my_hash_table.lookup_item(20))
truck1.load_truck(my_hash_table.lookup_item(17))
truck1.load_truck(my_hash_table.lookup_item(19))
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())
# truck1.load_truck(my_hash_table.lookup_item())


# truck1.print_truck_status()

# loading truck 2
truck2.load_truck(my_hash_table.lookup_item(3))
truck2.load_truck(my_hash_table.lookup_item(18))
truck2.load_truck(my_hash_table.lookup_item(36))
truck2.load_truck(my_hash_table.lookup_item(38))
truck2.load_truck(my_hash_table.lookup_item(1))
truck2.load_truck(my_hash_table.lookup_item(2))
truck2.load_truck(my_hash_table.lookup_item(4))
truck2.load_truck(my_hash_table.lookup_item(5))
truck2.load_truck(my_hash_table.lookup_item(37))
truck2.load_truck(my_hash_table.lookup_item(39))
truck2.load_truck(my_hash_table.lookup_item(40))
truck2.load_truck(my_hash_table.lookup_item(35))
# truck2.load_truck(my_hash_table.lookup_item())
# truck2.load_truck(my_hash_table.lookup_item())
# truck2.load_truck(my_hash_table.lookup_item())
# truck2.load_truck(my_hash_table.lookup_item())

# truck2.print_truck_status()

start_vertex = '4001 South 700 East'
# for package in truck2.loaded_packages:
#     print(distance_array.get_address_index(package.address))

# print(distance_array.find_distance_for_address('600 E 900 South', '195 W Oakland Ave'))
# print(distance_array.find_distance_for_address('195 W Oakland Ave', '600 E 900 South'))
# example of how to access package objects
# for package in truck1.loaded_packages:
#     print(package.address)

print(truck2.loaded_packages)
trucks.DeliveryTruck.package_delivery(truck2, distance_array, my_hash_table)
print(truck2.loaded_packages)

print(truck1.loaded_packages)
trucks.DeliveryTruck.package_delivery(truck1, distance_array, my_hash_table)
print(truck1.loaded_packages)



for i in range(1, 41):
    print(my_hash_table.lookup_item(i).package_status)



print(truck2.time_in_route)

for i in range(1, 41):
    print(my_hash_table.lookup_item(i).time_delivered)


# CLI -------------------

option = 10
while option != 7:
    print('=' * 60)
    print('WGUPS Package Delivery')
    print('=' * 60)
    print('Total Milage: ', int(truck1.distance_traveled + truck2.distance_traveled))
    print('-' * 60)
    print("1. All Package Statuses")
    print("2: Specific Package Status")
    print("3. All Package Statuses For Specific Time")
    print('7. Exit')
    option = int(input('Select an option: '))
    if option == 1:
        for i in range(1, 41):
            print(my_hash_table.lookup_item(i))
    elif option == 2:
        pkg_id = int(input('Enter a package id: '))
        print(my_hash_table.lookup_item(pkg_id))
    elif option == 3:
        entered_time = input('Enter time to check package status HH:MM: ')
        hour,minute = entered_time.split(':')
        query_time = datetime.timedelta(hours=int(hour), minutes=int(minute))
        for i in range(1, 41):
            print(my_hash_table.lookup_item(i).package_status_by_time(query_time))




