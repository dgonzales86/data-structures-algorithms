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
        for row in self.distance:
            if row[0] == address:
                return count
            count += 1
        return -1

    def find_distance_for_address(self, address_start, address_end):
        start_index = self.get_address_index(address_start)
        end_index = self.get_address_index(address_end)
        distance = self.distance[start_index][end_index+1]
        if distance == '':
            distance = self.distance[end_index][start_index+1]

        return distance
