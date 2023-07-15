import csv


class Distance_Array:
    def __init__(self):
        self.distance = []

    def parse_distance(self, path):
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.distance.append(row)

    def get_address_index(self, address):
        count = 0
        for row in self.distance