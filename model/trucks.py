import queue

import algo.hash
from algo.distance_array import Distance_Array
from collections import deque


def nearest_address(distance_array, package_list):
    new_array = []
    unvisited = []
    start_address = '4001 South 700 East'
    closest = 999
    next_closest = None

    for package in package_list:
        new_array.append(package)
    while len(new_array) > 0:
        for package in package_list:
            package_to_remove = package
            next_closest = Distance_Array.find_distance_for_address(distance_array, start_address, package.address)
            if float(next_closest) < float(closest):
                closest = next_closest
               # start_address = package.address
                new_array.remove(package_to_remove)
                print(closest, package.address)
            else:
                unvisited.append(package_to_remove)
        for package in unvisited:
            package_to_remove = package




    # address = package_list.package.address(i)
    # Distance_Array.find_distance_for_address(start_address, address)
    # if package_list.address < closest:
    #     closest = package_list.address
    return closest


class DeliveryTruck:
    def __init__(self, truck_id, driver_id):
        self.truck_id = truck_id
        self.driver_id = driver_id
        self.loaded_packages = []
        self.miles_per_hour = None
        self.time_in_route = None
        self.distance_traveled = None
        self.delivery_route = queue.Queue()

    def load_truck(self, package):
        self.loaded_packages.append(package)

    # def deliver_package(self, truck):
    #     while len(truck.loaded_packages) > 0:
    #         for truck.loaded_packages

    def print_truck_status(self):
        package_str = [str(package) for package in self.loaded_packages]
        print(self.truck_id, ':', self.driver_id, ':', package_str)

#  def unload_truck(self):
