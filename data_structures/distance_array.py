import csv


class Distance_Array:
    # Distance list, or 2D array constructor.
    # Time complexity, O(1) as it requires a constant number of operations to create an empty list.
    # Space complexity, O(1) as creation of an empty list requires constant space.
    def __init__(self):
        self.distance = []

    # Parses given csv file into a 2d array/list.
    # Time complexity, O(N^2) as the file iterates through each row and column in a given csv file.
    # With the csv file given as a symmetrical graph, there are the same number of rows as columns.
    # Space complexity, O(N^2) as the space requirements grow proportionately to the number of rows and columns.
    # The csv file for this method to work correctly in the scope of this application must have the same number of
    # rows as there are columns. If method were to be used outside the scope of this project, it would operate in a
    # space and time complexity of O(M * N).
    def parse_distance(self, path):
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.distance.append(row)

    # Retrieves index of a passed address.
    # Time complexity, O(N) as method depends on N number of elements in the distance array.
    # Space complexity, O(1) as it takes a constant amount of space to store the count variable.
    def get_address_index(self, address):
        count = 0
        for row in self.distance:
            if row[0] == address:
                return count
            count += 1
        return -1

    # Uses indices to locate the next closest address.
    # The distance array is a given as a symmetrical graph.
    # If the index returns an empty value, the indices are reversed to obtain the distance value
    # Time complexity, O(1) as values are retrieved using indices and requires a constant number of operations.
    # Space complexity, O(1) as it takes a constant amount of space to store variables.
    def find_distance_for_address(self, address_start, address_end):
        start_index = self.get_address_index(address_start)
        end_index = self.get_address_index(address_end)
        distance = self.distance[start_index][end_index+1]
        if distance == '':
            distance = self.distance[end_index][start_index+1]

        return distance
