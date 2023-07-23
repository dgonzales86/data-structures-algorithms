"""Package class:
    __init__ : package constructor
    __str__ : returns string of package object
    package_status_by_time : returns package status at specified time"""

import datetime


class Package:

    # Package object constructor
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
        self.truck_start_time = datetime.timedelta(hours=0, minutes=0)
        self.time_loaded = None

# Returns f string from package object. Time complexity of O(1). Space complexity of O(1)
    def __str__(self):
        return f'{self.package_id} | {self.address} | {self.city} | {self.state} | {self.zip_code} | ' \
               f'{self.delivery_deadline} | {self.mass} | {self.package_status} | {self.time_delivered}'

# Returns package status using query time variable. Used within command line interface. Time complexity 0(1).
    # Space complexity O(1)
    def package_status_by_time(self, query_time):

        if query_time >= self.time_delivered:
            time_status = 'Delivered'
        elif query_time <= self.truck_start_time:
            time_status = 'At Hub'
        else:
            time_status = 'In Route'
        return f'{self.package_id} | {self.address} | {self.city} | {self.state} | {self.zip_code} | ' \
               f'{self.delivery_deadline} | {self.mass} | {time_status} | {self.time_delivered}'
