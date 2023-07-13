import algo.hash


class DeliveryTruck:
    def __init__(self, packages):
        self.packages = [packages]

    def load_truck(self, package):
        self.packages.append(package)

    def unload_truck(self, package):
        while package in self.packages:
            self.packages.remove(package)

















  #  def unload_truck(self):




