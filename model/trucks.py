import algo.hash


class DeliveryTruck:
    def __init__(self, truck_id, driver_id):
        self.truck_id = truck_id
        self.driver_id = driver_id
        self.loaded_packages = []
        self.time_of_day = None
        self.distance_traveled = None

    def load_truck(self, package):
        self.loaded_packages.append(package)

    def unload_truck(self, package):
        while package in self.packages:
            self.packages.remove(package)
            package.package_status = 'delivered'

    def print_truck_status(self):
        package_str = [str(package) for package in self.loaded_packages]
        print(self.truck_id, ':', self.driver_id, ':', package_str)

















  #  def unload_truck(self):




