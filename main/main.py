"""Main method:
    Truck and driver objects initialized.
    Hash table built and populated with package data.
    2D array/list created and populated with distance data.
    Truck objects loaded with package objects.
    Package delivery algorithm ran for each truck.
    Command line interface implemented.
    """

import datetime
import data_structures.hash
from data_structures.hash import HashTable
from model import package, trucks
from model.driver import Truck_Driver
from model.trucks import DeliveryTruck
from data_structures.distance_array import Distance_Array

# Initializes both truck drivers
driver1 = Truck_Driver(1, 'Wayne')
driver2 = Truck_Driver(2, 'Garth')

# Initializes all 3 delivery trucks with truck id, driver id, and time of departure
truck1 = DeliveryTruck(1, 1, datetime.timedelta(hours=8, minutes=0))
truck2 = DeliveryTruck(2, 2, datetime.timedelta(hours=9, minutes=10))
truck3 = DeliveryTruck(3, None, datetime.timedelta(hours=10, minutes=45))

# Creates hash table object
my_hash_table = HashTable()

# Parses .csv file and populates hash map
package_file = "util/packageDestCSV.csv"
data_structures.hash.extract_csv(package_file, my_hash_table)

# Variable for string path to address file
address_file = "util/addresses.csv"

# Variable for string path to distance table file
distance_table = "util/Distance_Table_2.csv"

# Creates 2d array
distance_array = Distance_Array()
distance_array.parse_distance(distance_table)

# Loading truck 1
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
my_hash_table.lookup_item(9).address = '410 S State St'
my_hash_table.lookup_item(9).zip_code = '84111'

# Loading truck 3
truck3.load_truck(my_hash_table.lookup_item(2), '06:00')
truck3.load_truck(my_hash_table.lookup_item(21), '06:00')
truck3.load_truck(my_hash_table.lookup_item(22), '06:00')
truck3.load_truck(my_hash_table.lookup_item(23), '06:00')
truck3.load_truck(my_hash_table.lookup_item(33), '06:00')
truck3.load_truck(my_hash_table.lookup_item(24), '06:00')
truck3.load_truck(my_hash_table.lookup_item(28), '09:20')
truck3.load_truck(my_hash_table.lookup_item(9), '10:30')

# Delivering packages for truck 1 and truck 2
trucks.DeliveryTruck.package_delivery(truck1, distance_array, my_hash_table)
trucks.DeliveryTruck.package_delivery(truck2, distance_array, my_hash_table)

# Following completion of truck 1's route, driver 1 exits truck 1 and boards truck 3
truck1.driver_id = None
truck3.driver_id = 1

# Truck 3 begins delivery route
trucks.DeliveryTruck.package_delivery(truck3, distance_array, my_hash_table)

# All packages are delivered
print("Package Delivery Complete: ")


# -------------------------------- Command Line Interface --------------------------------

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
