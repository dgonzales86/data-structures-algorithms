# Name: Donald Gonzales, Student ID:  000983159

import datetime
import data_structures.hash
from data_structures.hash import HashTable
from model import package, trucks
from model.driver import Truck_Driver
from model.trucks import DeliveryTruck
from data_structures.distance_array import Distance_Array

# Creates instances of both truck drivers
# Time complexity, O(1) as it takes a constant number of operations to create an instance of an object.
# Space complexity, O(1) as it takes a constant space to store an instance of an object.
driver1 = Truck_Driver(1, 'Wayne')
driver2 = Truck_Driver(2, 'Garth')

# Creates instances of all 3 delivery trucks with truck id, driver id, and time of departure

truck1 = DeliveryTruck(1, 1, datetime.timedelta(hours=8, minutes=0))
truck2 = DeliveryTruck(2, 2, datetime.timedelta(hours=9, minutes=10))
truck3 = DeliveryTruck(3, None, datetime.timedelta(hours=10, minutes=45))

# Creates hash table object/ instantiating the HashTable class.
# Time complexity, O(1) as it requires a constant number of operations to instantiate a class.
# Space complexity, O(1) as it requires a constant amount of space for each object of the same class.
my_hash_table = HashTable()

# Parses .csv file and populates hash map
# Space and time complexity of package_file, O(1)
# Space and time complexity of data_structures.hash.extract_csv() elaborated in hash.py
package_file = "util/packageDestCSV.csv"
data_structures.hash.extract_csv(package_file, my_hash_table)

# Variable for string path to address file
# Space and time complexity, O(1)
address_file = "util/addresses.csv"

# Variable for string path to distance table file
# Space and time complexity, O(1)
distance_table = "util/Distance_Table_2.csv"

# Creates 2d array
# distance array variable, time and space complexity O(1)
# parse_distance space and time complexity O(N^2)
distance_array = Distance_Array()
distance_array.parse_distance(distance_table)

# Loading truck 1
# Appends packages to truck1 package list.
# Space and time complexity, O(1) for each line.
truck1.load_truck(my_hash_table.lookup_item(14), '06:00')
truck1.load_truck(my_hash_table.lookup_item(15), '06:00')
truck1.load_truck(my_hash_table.lookup_item(16), '06:00')
truck1.load_truck(my_hash_table.lookup_item(13), '06:00')
truck1.load_truck(my_hash_table.lookup_item(20), '06:00')
truck1.load_truck(my_hash_table.lookup_item(17), '06:00')
truck1.load_truck(my_hash_table.lookup_item(19), '06:00')
truck1.load_truck(my_hash_table.lookup_item(7), '06:00')
truck1.load_truck(my_hash_table.lookup_item(8), '06:00')
truck1.load_truck(my_hash_table.lookup_item(10), '06:00')
truck1.load_truck(my_hash_table.lookup_item(11), '06:00')
truck1.load_truck(my_hash_table.lookup_item(12), '06:00')
truck1.load_truck(my_hash_table.lookup_item(29), '06:00')
truck1.load_truck(my_hash_table.lookup_item(30), '06:00')
truck1.load_truck(my_hash_table.lookup_item(31), '06:00')
truck1.load_truck(my_hash_table.lookup_item(34), '06:00')

# Loading truck 2
# Appends package to truck2 package list.
# Space and time complexity, O(1) for each line.
truck2.load_truck(my_hash_table.lookup_item(3), '06:00')
truck2.load_truck(my_hash_table.lookup_item(18), '06:00')
truck2.load_truck(my_hash_table.lookup_item(36), '06:00')
truck2.load_truck(my_hash_table.lookup_item(38), '06:00')
truck2.load_truck(my_hash_table.lookup_item(1), '06:00')
truck2.load_truck(my_hash_table.lookup_item(26), '06:00')
truck2.load_truck(my_hash_table.lookup_item(4), '06:00')
truck2.load_truck(my_hash_table.lookup_item(5), '06:00')
truck2.load_truck(my_hash_table.lookup_item(37), '06:00')
truck2.load_truck(my_hash_table.lookup_item(39), '06:00')
truck2.load_truck(my_hash_table.lookup_item(40), '06:00')
truck2.load_truck(my_hash_table.lookup_item(35), '06:00')
truck2.load_truck(my_hash_table.lookup_item(6), '09:08')
truck2.load_truck(my_hash_table.lookup_item(25), '09:08')
truck2.load_truck(my_hash_table.lookup_item(27), '09:08')
truck2.load_truck(my_hash_table.lookup_item(32), '09:08')

# Address correction for package 9
# Space and time complexity O(1) for each line
my_hash_table.lookup_item(9).address = '410 S State St'
my_hash_table.lookup_item(9).zip_code = '84111'

# Loading truck 3
# Appends package to truck3 package list.
# Space and time complexity, O(1) for each line.
truck3.load_truck(my_hash_table.lookup_item(2), '06:00')
truck3.load_truck(my_hash_table.lookup_item(21), '06:00')
truck3.load_truck(my_hash_table.lookup_item(22), '06:00')
truck3.load_truck(my_hash_table.lookup_item(23), '06:00')
truck3.load_truck(my_hash_table.lookup_item(33), '06:00')
truck3.load_truck(my_hash_table.lookup_item(24), '06:00')
truck3.load_truck(my_hash_table.lookup_item(28), '09:20')
truck3.load_truck(my_hash_table.lookup_item(9), '10:30')

# Delivering packages for truck 1 and truck 2
# Time complexity O(M * N), and space complexity O(1) for each line
trucks.DeliveryTruck.package_delivery(truck1, distance_array, my_hash_table)
trucks.DeliveryTruck.package_delivery(truck2, distance_array, my_hash_table)

# Following completion of truck 1's route, driver 1 exits truck 1 and boards truck 3
# Space and time complexity O(1) for each line
truck1.driver_id = None
truck3.driver_id = 1

# Truck 3 begins delivery route
# Time complexity O(M * N), and space complexity O(1)
trucks.DeliveryTruck.package_delivery(truck3, distance_array, my_hash_table)

# All packages are delivered
# Space and time complexity O(1)
print("Package Delivery Complete: ")


# -------------------------------- Command Line Interface --------------------------------


# Interface provides options to view status of all packages, view status of all packages via a given time, and look up
# package by a given package id.
# Worst case run time complexity for this interface is O(M * N). The program runs for M options selected, excluding 7,
# and N number of items in the hash table. The best case scenario would be O(1) if option 7 were selected.
# Space complexity of this method is O(1) as memory requirements do not expand regardless of selection made.
option = 10
while option != 7:
    print('=' * 60)
    print('WGUPS Package Delivery')
    print('=' * 60)
    print('Total Milage: ', int(truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled))
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
        hour, minute = entered_time.split(':')
        query_time = datetime.timedelta(hours=int(hour), minutes=int(minute))
        print("Pkg ID | Address | City | State | Zip Code | Delivery Deadline | Mass | Status At Time | Time Delivered")
        for i in range(1, 41):
            print(my_hash_table.lookup_item(i).package_status_by_time(query_time))
    else:
        print('Please Make A Valid Selection: 1, 2, 3, or 7 to Exit:')
