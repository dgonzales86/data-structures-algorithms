from enum import Enum

from data_structures.graph import Graph


class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.package_status = "At Hub"
        self.time_delivered = None

    def __str__(self):
        return f'{self.package_id} {self.address} {self.city} {self.state} {self.zip_code} {self.delivery_deadline} ' \
               f'{self.mass} {self.package_status} {self.time_delivered}'
