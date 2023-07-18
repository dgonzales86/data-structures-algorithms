import queue

import algo.hash
from algo.distance_array import Distance_Array


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


def time_travel(distance_traveled):
    mph = 18


def package_delivery(distance_array, package_list, hash_table):
    start_address = '4001 South 700 East'
    closest = 999
    next_address = None
    package_clone = None
    total_distance = 0.0

    while len(package_list) > 0:
        for package in package_list:
            next_closest = Distance_Array.find_distance_for_address(distance_array, start_address, package.address)
            if float(next_closest) < float(closest):
                closest = next_closest
                package_clone = package
                next_address = package.address
        total_distance = total_distance + float(closest)
        print(closest, package_clone.address, ' total distance: ', total_distance)

        if package_clone in package_list:
            package_list.remove(package_clone)
        hash_table.lookup_item(int(package_clone.package_id)).package_status = 'Delivered'

        start_address = next_address
        closest = 999

    return package_list

