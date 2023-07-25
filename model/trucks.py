import queue
import datetime
from data_structures.distance_array import Distance_Array


# Constructor for DeliveryTruck class
# Time complexity, O(1)
# Space complexity, O(1)
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

    # Loads packages to truck and timestamps the loaded time.
    # Time complexity, O(1) as appending to a list, and storing variables are all O(1). Method takes a constant
    # number of operations per run.
    # Space complexity, O(1) as it takes a constant number of space required to store variables and append to a list.
    def load_truck(self, package, time_loaded):
        package.truck_start_time = self.time_of_departure
        self.loaded_packages.append(package)
        package.time_loaded = time_loaded

    # Prints status of trucks. Space and time complexity of O(1)
    def print_truck_status(self):
        package_str = [str(package) for package in self.loaded_packages]
        print(self.truck_id, ':', self.driver_id, ':', package_str)

    # Computes the time a specific truck is in route by passing the distance traveled in miles.
    # Time complexity, O(1) as this method requires a constant number of operations regardless of miles traveled.
    # Space complexity, O(1) as space requirements do not grow based on input and a constant amount of memory is
    # required to store the time_in_route variable for this method.
    def time_travel(self, distance_traveled):
        mph = self.miles_per_hour

        self.time_in_route = datetime.timedelta(hours=distance_traveled / self.miles_per_hour)

        return self.time_in_route

    # Returns current time.
    # Time complexity, O(1) as method's operations are constant.
    # Space complexity, O(1) as it requires a constant space requirement to store and return current_time variable.
    def current_time(self):
        current_time = self.time_of_departure + self.time_travel(self.distance_traveled)
        return current_time

    # Package delivery algorithm: Nearest Neighbor Algorithm.
    # Method takes distance_array, and hash_table as parameters.
    # Using a while-loop, the method checks packages loaded in truck object finding the closest address to the current
    # location. Since the first package will always be closer than the initial closest variable, this package will be
    # the first location visited. Subsequent iterations will use the previously visited address as the start address,
    # and iterate through the remaining packages in the truck to find the next closest address. Once the next closest
    # address is located, the distance traveled will increment based on the distance, the truck package list will
    # decrement, and the package will be timestamped and marked delivered in the package hash table. When the
    # truck package list is at zero, the while-loop ends, the last stop becomes the start address, the final destination
    # is set to the hub address, and those addressed are passed to the lookup method to increment the distance.
    # The route is then marked complete and an empty list of loaded packages is returned.
    # Time complexity, O(M * N) as the while-loop runs for M number of loaded_packages, and the for-loop runs for N
    # number of packages in loaded_packages. while both loops pertain to the same list of packages, they operate
    # independently of each-other.
    # Space complexity, O(1) as the method does not increase memory requirements as it runs. If the application were
    # scaled up with a larger distance_array, and a larger hash_table, those data structures would grow in space
    # complexity, but it would not affect this specific method.
    def package_delivery(self, distance_array, hash_table):
        start_address = '4001 South 700 East'
        closest = 999
        next_address = None
        package_clone = None

        print('Truck ', self.truck_id, ' delivery started at: ', self.current_time())

        for hash_table.package in self.loaded_packages:
            hash_table.package_status = 'In Route'

        # O(M * N) Time complexity
        while len(self.loaded_packages) > 0:
            for package in self.loaded_packages:
                next_closest = Distance_Array.find_distance_for_address(distance_array, start_address, package.address)
                if float(next_closest) < float(closest):
                    closest = next_closest
                    package_clone = package
                    next_address = package.address
            self.distance_traveled = self.distance_traveled + float(closest)

            # O(1)
            print('Next closet address is: ', closest, ' miles. ', package_clone.address, ' total distance: ',
                  self.distance_traveled, ' miles')
            # O(1)
            print('time traveled: ', self.time_travel(self.distance_traveled))

            # O(1)
            if package_clone in self.loaded_packages:
                self.loaded_packages.remove(package_clone)
                hash_table.lookup_item(int(package_clone.package_id)).package_status = 'Delivered'
                hash_table.lookup_item(int(package_clone.package_id)).time_delivered = self.current_time()
                hash_table.lookup_item(int(package_clone.package_id)).truck_start_time = self.time_of_departure

            # O(1)
            start_address = next_address
            # O(1)
            closest = 999
        # O(1)
        last_stop = start_address
        # O(1)
        final_destination = '4001 South 700 East'
        # O(1) as reading from a list by index is O(1)
        distance_back_to_hub = Distance_Array.find_distance_for_address(distance_array, last_stop, final_destination)
        self.distance_traveled = self.distance_traveled + float(distance_back_to_hub)
        print('Truck ', self.truck_id, ' route completed at: ', self.current_time())
        return self.loaded_packages
