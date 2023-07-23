import queue
import datetime
from data_structures.distance_array import Distance_Array


class DeliveryTruck:
    def __init__(self, truck_id, driver_id, time_of_departure):
        self.truck_id = truck_id
        self.driver_id = driver_id
        self.loaded_packages = []
        self.miles_per_hour = 18
        self.time_in_route = datetime.timedelta(0, 0)
        self.time_of_departure = time_of_departure
        self.distance_traveled = 0
        self.delivery_route = queue.Queue()

    def load_truck(self, package, time_loaded):
        package.truck_start_time = self.time_of_departure
        self.loaded_packages.append(package)
        package.time_loaded = time_loaded

    def print_truck_status(self):
        package_str = [str(package) for package in self.loaded_packages]
        print(self.truck_id, ':', self.driver_id, ':', package_str)

    def time_travel(self, distance_traveled):
        mph = self.miles_per_hour

        self.time_in_route = datetime.timedelta(hours=distance_traveled / self.miles_per_hour)

        return self.time_in_route

# returns
    def current_time(self):
        current_time = self.time_of_departure + self.time_travel(self.distance_traveled)
        return current_time

    # delivery algorithm: Nearest Neighbor Algorithm
    def package_delivery(self, distance_array, hash_table):
        start_address = '4001 South 700 East'
        closest = 999
        next_address = None
        package_clone = None

        print('Truck ', self.truck_id, ' delivery started at: ', self.current_time())

        for hash_table.package in self.loaded_packages:
            hash_table.package_status = 'In Route'

        while len(self.loaded_packages) > 0:
            for package in self.loaded_packages:
                next_closest = Distance_Array.find_distance_for_address(distance_array, start_address, package.address)
                if float(next_closest) < float(closest):
                    closest = next_closest
                    package_clone = package
                    next_address = package.address
            self.distance_traveled = self.distance_traveled + float(closest)

            print('Next closet address is: ', closest, ' miles. ', package_clone.address, ' total distance: ',
                  self.distance_traveled, ' miles')
            print('time traveled: ', self.time_travel(self.distance_traveled))

            if package_clone in self.loaded_packages:
                self.loaded_packages.remove(package_clone)
                hash_table.lookup_item(int(package_clone.package_id)).package_status = 'Delivered'
                hash_table.lookup_item(int(package_clone.package_id)).time_delivered = self.current_time()
                hash_table.lookup_item(int(package_clone.package_id)).truck_start_time = self.time_of_departure

            start_address = next_address
            closest = 999
        last_stop = start_address
        final_destination = '4001 South 700 East'
        distance_back_to_hub = Distance_Array.find_distance_for_address(distance_array, last_stop, final_destination)
        self.distance_traveled = self.distance_traveled + float(distance_back_to_hub)
        print('Truck ', self.truck_id, ' route completed at: ', self.current_time())
        return self.loaded_packages
