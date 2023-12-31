"""
***** Class not used within project, but kept for possible future implementations *****
class Graph:
    add_vertex - adds a node/vertes to the graph
    add_edge - adds weighted edge between nodes
    delete_edge - removes edges between nodes
    delete_vertes - loops through edges between nodes, deletes them, and proceeds to delete self
    print_distance_graph - prints graph's contents
"""

import csv

class Graph:
    def __init__(self):
        self.distance_graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.distance_graph.keys():
            self.distance_graph[vertex] = {}
            return True
        return False

    def add_edge(self, vertex1, vertex2, distance):
        if vertex1 in self.distance_graph.keys() and vertex2 in self.distance_graph.keys():
            self.distance_graph[vertex1][vertex2] = distance
            self.distance_graph[vertex2][vertex1] = distance
            return True
        return False

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.distance_graph.keys() and vertex2 in self.distance_graph[vertex1]:
            del self.distance_graph[vertex1][vertex2]
            del self.distance_graph[vertex2][vertex1]
            return True
        return False

    def delete_vertex(self, vertex):
        if vertex in self.distance_graph.keys():
            for bound_vertex in self.distance_graph[vertex]:
                del self.distance_graph[bound_vertex][vertex]
            del self.distance_graph[vertex]
            return True
        return False

    def print_distance_graph(self):
        for vertex in self.distance_graph:
            print(vertex, ':', self.distance_graph[vertex])

    def csv_parse_graph(self, address_file):
        with open(address_file, 'r') as address_file:
            address_reader = csv.reader(address_file)
            for row in address_reader:
                address = row[0]
                self.add_vertex(address)
        self.add_edge('4001 South 700 East', '4001 South 700 East', 0)
        self.add_edge('4001 South 700 East', '1060 Dalton Ave S', 7.2)
        self.add_edge('4001 South 700 East', '1330 2100 S', 3.8)
        self.add_edge('4001 South 700 East', '1488 4800 S', 11.0)
        self.add_edge('4001 South 700 East', '177 W Price Ave', 2.2)
        self.add_edge('4001 South 700 East', '195 W Oakland Ave', 3.5)
        self.add_edge('4001 South 700 East', '2010 W 500 S', 10.9)
        self.add_edge('4001 South 700 East', '2300 Parkway Blvd', 8.6)
        self.add_edge('4001 South 700 East', '233 Canyon Rd', 7.6)
        self.add_edge('4001 South 700 East', '2530 S 500 E', 2.8)
        self.add_edge('4001 South 700 East', '2600 Taylorsville Blvd', 6.4)
        self.add_edge('4001 South 700 East', '2835 Main St', 3.2)
        self.add_edge('4001 South 700 East', '300 State St', 7.6)
        self.add_edge('4001 South 700 East', '3060 Lester St', 5.2)
        self.add_edge('4001 South 700 East', '3148 S 1100 W', 4.4)
        self.add_edge('4001 South 700 East', '3365 S 900 W', 3.7)
        self.add_edge('4001 South 700 East', '3575 W Valley Central Station bus Loop', 7.6)
        self.add_edge('4001 South 700 East', '3595 Main St', 2.0)
        self.add_edge('4001 South 700 East', '380 W 2880 S', 3.6)
        self.add_edge('4001 South 700 East', '410 S State St', 6.5)
        self.add_edge('4001 South 700 East', '4300 S 1300 E', 1.9)
        self.add_edge('4001 South 700 East', '4580 S 2300 E', 3.4)
        self.add_edge('4001 South 700 East', '5025 State St', 2.4)
        self.add_edge('4001 South 700 East', '5100 South 2700 West', 6.4)
        self.add_edge('4001 South 700 East', '5383 South 900 East #104', 2.4)
        self.add_edge('4001 South 700 East', '600 E 900 South', 5.0)
        self.add_edge('4001 South 700 East', '6351 South 900 East', 3.6)
        self.add_edge('1060 Dalton Ave S', '1060 Dalton Ave S', 0)
        self.add_edge('1060 Dalton Ave S', '1330 2100 S', 7.1)
        self.add_edge('1060 Dalton Ave S', '1488 4800 S', 6.4)
        self.add_edge('1060 Dalton Ave S', '177 W Price Ave', 6.0)
        self.add_edge('1060 Dalton Ave S', '195 W Oakland Ave', 4.8)
        self.add_edge('1060 Dalton Ave S', '2010 W 500 S', 1.6)
        self.add_edge('1060 Dalton Ave S', '2300 Parkway Blvd', 2.8)
        self.add_edge('1060 Dalton Ave S', '233 Canyon Rd', 4.8)
        self.add_edge('1060 Dalton Ave S', '2530 S 500 E', 6.3)
        self.add_edge('1060 Dalton Ave S', '2600 Taylorsville Blvd', 7.3)
        self.add_edge('1060 Dalton Ave S', '2835 Main St', 5.3)
        self.add_edge('1060 Dalton Ave S', '300 State St', 4.8)
        self.add_edge('1060 Dalton Ave S', '3060 Lester St', 3.0)
        self.add_edge('1060 Dalton Ave S', '3148 S 1100 W', 4.6)
        self.add_edge('1060 Dalton Ave S', '3365 S 900 W', 4.5)
        self.add_edge('1060 Dalton Ave S', '3575 W Valley Central Station bus Loop', 7.4)
        self.add_edge('1060 Dalton Ave S', '3595 Main St', 6.0)
        self.add_edge('1060 Dalton Ave S', '380 W 2880 S', 5.0)
        self.add_edge('1060 Dalton Ave S', '410 S State St', 4.8)
        self.add_edge('1060 Dalton Ave S', '4300 S 1300 E', 9.5)
        self.add_edge('1060 Dalton Ave S', '4580 S 2300 E', 10.9)
        self.add_edge('1060 Dalton Ave S', '5025 State St', 8.3)
        self.add_edge('1060 Dalton Ave S', '5100 South 2700 West', 6.9)
        self.add_edge('1060 Dalton Ave S', '5383 South 900 East #104', 10.0)
        self.add_edge('1060 Dalton Ave S', '600 E 900 South', 4.4)
        self.add_edge('1060 Dalton Ave S', '6351 South 900 East', 13.0)
        self.add_edge('1330 2100 S', '1330 2100 S', 0)
        self.add_edge('1330 2100 S', '1488 4800 S', 6.2)
        self.add_edge('1330 2100 S', '177 W Price Ave', 4.4)
        self.add_edge('1330 2100 S', '195 W Oakland Ave', 2.8)
        self.add_edge('1330 2100 S', '2010 W 500 S', 8.6)
        self.add_edge('1330 2100 S', '2300 Parkway Blvd', 6.3)
        self.add_edge('1330 2100 S', '233 Canyon Rd', 5.3)
        self.add_edge('1330 2100 S', '2530 S 500 E', 1.6)
        self.add_edge('1330 2100 S', '2600 Taylorsville Blvd', 10.4)
        self.add_edge('1330 2100 S', '2835 Main St', 3.0)
        self.add_edge('1330 2100 S', '300 State St', 5.3)
        self.add_edge('1330 2100 S', '3060 Lester St', 6.5)
        self.add_edge('1330 2100 S', '3148 S 1100 W', 5.6)
        self.add_edge('1330 2100 S', '3365 S 900 W', 5.8)
        self.add_edge('1330 2100 S', '3575 W Valley Central Station bus Loop', 5.7)
        self.add_edge('1330 2100 S', '3595 Main St', 4.1)
        self.add_edge('1330 2100 S', '380 W 2880 S', 3.6)
        self.add_edge('1330 2100 S', '410 S State St', 4.3)
        self.add_edge('1330 2100 S', '4300 S 1300 E', 3.3)
        self.add_edge('1330 2100 S', '4580 S 2300 E', 5.0)
        self.add_edge('1330 2100 S', '5025 State St', 6.1)
        self.add_edge('1330 2100 S', '5100 South 2700 West', 9.7)
        self.add_edge('1330 2100 S', '5383 South 900 East #104', 6.1)
        self.add_edge('1330 2100 S', '600 E 900 South', 2.8)
        self.add_edge('1330 2100 S', '6351 South 900 East', 7.4)
        self.add_edge('1488 4800 S', '1488 4800 S', 0)
        self.add_edge('1488 4800 S', '177 W Price Ave', 5.6)
        self.add_edge('1488 4800 S', '195 W Oakland Ave', 6.9)
        self.add_edge('1488 4800 S', '2010 W 500 S', 8.6)
        self.add_edge('1488 4800 S', '2300 Parkway Blvd', 4.0)
        self.add_edge('1488 4800 S', '233 Canyon Rd', 11.1)
        self.add_edge('1488 4800 S', '2530 S 500 E', 7.3)
        self.add_edge('1488 4800 S', '2600 Taylorsville Blvd', 1.0)
        self.add_edge('1488 4800 S', '2835 Main St', 6.4)
        self.add_edge('1488 4800 S', '300 State St', 11.1)
        self.add_edge('1488 4800 S', '3060 Lester St', 3.9)
        self.add_edge('1488 4800 S', '3148 S 1100 W', 4.3)
        self.add_edge('1488 4800 S', '3365 S 900 W', 4.4)
        self.add_edge('1488 4800 S', '3575 W Valley Central Station bus Loop', 7.2)
        self.add_edge('1488 4800 S', '3595 Main St', 5.3)
        self.add_edge('1488 4800 S', '380 W 2880 S', 6.0)
        self.add_edge('1488 4800 S', '410 S State St', 10.6)
        self.add_edge('1488 4800 S', '4300 S 1300 E', 5.9)
        self.add_edge('1488 4800 S', '4580 S 2300 E', 7.4)
        self.add_edge('1488 4800 S', '5025 State St', 4.7)
        self.add_edge('1488 4800 S', '5100 South 2700 West', 0.6)
        self.add_edge('1488 4800 S', '5383 South 900 East #104', 6.4)
        self.add_edge('1488 4800 S', '600 E 900 South', 10.1)
        self.add_edge('1488 4800 S', '6351 South 900 East', 10.1)
        self.add_edge('177 W Price Ave', '177 W Price Ave', 0)
        self.add_edge('177 W Price Ave', '195 W Oakland Ave', 1.9)
        self.add_edge('177 W Price Ave', '2010 W 500 S', 7.9)
        self.add_edge('177 W Price Ave', '2300 Parkway Blvd', 5.1)
        self.add_edge('177 W Price Ave', '233 Canyon Rd', 7.5)
        self.add_edge('177 W Price Ave', '2530 S 500 E', 2.6)
        self.add_edge('177 W Price Ave', '2600 Taylorsville Blvd', 6.5)
        self.add_edge('177 W Price Ave', '2835 Main St', 1.5)
        self.add_edge('177 W Price Ave', '300 State St', 7.5)
        self.add_edge('177 W Price Ave', '3060 Lester St', 3.2)
        self.add_edge('177 W Price Ave', '3148 S 1100 W', 2.4)
        self.add_edge('177 W Price Ave', '3365 S 900 W', 2.7)
        self.add_edge('177 W Price Ave', '3575 W Valley Central Station bus Loop', 1.4)
        self.add_edge('177 W Price Ave', '3595 Main St', 0.5)
        self.add_edge('177 W Price Ave', '380 W 2880 S', 1.7)
        self.add_edge('177 W Price Ave', '410 S State St', 6.5)
        self.add_edge('177 W Price Ave', '4300 S 1300 E', 3.2)
        self.add_edge('177 W Price Ave', '4580 S 2300 E', 5.2)
        self.add_edge('177 W Price Ave', '5025 State St', 2.5)
        self.add_edge('177 W Price Ave', '5100 South 2700 West', 6.0)
        self.add_edge('177 W Price Ave', '5383 South 900 East #104', 4.2)
        self.add_edge('177 W Price Ave', '600 E 900 South', 5.4)
        self.add_edge('177 W Price Ave', '6351 South 900 East', 5.5)
        self.add_edge('195 W Oakland Ave', '195 W Oakland Ave', 0)
        self.add_edge('195 W Oakland Ave', '2010 W 500 S', 6.3)
        self.add_edge('195 W Oakland Ave', '2300 Parkway Blvd', 4.3)
        self.add_edge('195 W Oakland Ave', '233 Canyon Rd', 4.5)
        self.add_edge('195 W Oakland Ave', '2530 S 500 E', 1.5)
        self.add_edge('195 W Oakland Ave', '2600 Taylorsville Blvd', 8.7)
        self.add_edge('195 W Oakland Ave', '2835 Main St', 0.8)
        self.add_edge('195 W Oakland Ave', '300 State St', 4.5)
        self.add_edge('195 W Oakland Ave', '3060 Lester St', 3.9)
        self.add_edge('195 W Oakland Ave', '3148 S 1100 W', 3.0)
        self.add_edge('195 W Oakland Ave', '3365 S 900 W', 3.8)
        self.add_edge('195 W Oakland Ave', '3575 W Valley Central Station bus Loop', 5.7)
        self.add_edge('195 W Oakland Ave', '3595 Main St', 1.9)
        self.add_edge('195 W Oakland Ave', '380 W 2880 S', 1.1)
        self.add_edge('195 W Oakland Ave', '410 S State St', 3.5)
        self.add_edge('195 W Oakland Ave', '4300 S 1300 E', 4.9)
        self.add_edge('195 W Oakland Ave', '4580 S 2300 E', 6.9)
        self.add_edge('195 W Oakland Ave', '5025 State St', 4.2)
        self.add_edge('195 W Oakland Ave', '5100 South 2700 West', 9.0)
        self.add_edge('195 W Oakland Ave', '5383 South 900 East #104', 5.9)
        self.add_edge('195 W Oakland Ave', '600 E 900 South', 3.5)
        self.add_edge('195 W Oakland Ave', '6351 South 900 East', 7.2)
        self.add_edge('2010 W 500 S', '2010 W 500 S', 0)
        self.add_edge('2010 W 500 S', '2300 Parkway Blvd', 4.0)
        self.add_edge('2010 W 500 S', '233 Canyon Rd', 4.2)
        self.add_edge('2010 W 500 S', '2530 S 500 E', 8.0)
        self.add_edge('2010 W 500 S', '2600 Taylorsville Blvd', 8.6)
        self.add_edge('2010 W 500 S', '2835 Main St', 6.9)
        self.add_edge('2010 W 500 S', '300 State St', 4.2)
        self.add_edge('2010 W 500 S', '3060 Lester St', 4.2)
        self.add_edge('2010 W 500 S', '3148 S 1100 W', 8.0)
        self.add_edge('2010 W 500 S', '3365 S 900 W', 5.8)
        self.add_edge('2010 W 500 S', '3575 W Valley Central Station bus Loop', 7.2)
        self.add_edge('2010 W 500 S', '3595 Main St', 7.7)
        self.add_edge('2010 W 500 S', '380 W 2880 S', 6.6)
        self.add_edge('2010 W 500 S', '410 S State St', 3.2)
        self.add_edge('2010 W 500 S', '4300 S 1300 E', 11.2)
        self.add_edge('2010 W 500 S', '4580 S 2300 E', 12.7)
        self.add_edge('2010 W 500 S', '5025 State St', 10.0)
        self.add_edge('2010 W 500 S', '5100 South 2700 West', 8.2)
        self.add_edge('2010 W 500 S', '5383 South 900 East #104', 11.7)
        self.add_edge('2010 W 500 S', '600 E 900 South', 5.1)
        self.add_edge('2010 W 500 S', '6351 South 900 East', 14.2)
        self.add_edge('2300 Parkway Blvd', '2300 Parkway Blvd', 0)
        self.add_edge('2300 Parkway Blvd', '233 Canyon Rd', 7.7)
        self.add_edge('2300 Parkway Blvd', '2530 S 500 E', 9.3)
        self.add_edge('2300 Parkway Blvd', '2600 Taylorsville Blvd', 4.6)
        self.add_edge('2300 Parkway Blvd', '2835 Main St', 4.8)
        self.add_edge('2300 Parkway Blvd', '300 State St', 7.7)
        self.add_edge('2300 Parkway Blvd', '3060 Lester St', 1.6)
        self.add_edge('2300 Parkway Blvd', '3148 S 1100 W', 3.3)
        self.add_edge('2300 Parkway Blvd', '3365 S 900 W', 3.4)
        self.add_edge('2300 Parkway Blvd', '3575 W Valley Central Station bus Loop', 3.1)
        self.add_edge('2300 Parkway Blvd', '3595 Main St', 5.1)
        self.add_edge('2300 Parkway Blvd', '380 W 2880 S', 4.6)
        self.add_edge('2300 Parkway Blvd', '410 S State St', 6.7)
        self.add_edge('2300 Parkway Blvd', '4300 S 1300 E', 8.1)
        self.add_edge('2300 Parkway Blvd', '4580 S 2300 E', 10.4)
        self.add_edge('2300 Parkway Blvd', '5025 State St', 7.8)
        self.add_edge('2300 Parkway Blvd', '5100 South 2700 West', 4.2)
        self.add_edge('2300 Parkway Blvd', '5383 South 900 East #104', 9.5)
        self.add_edge('2300 Parkway Blvd', '600 E 900 South', 6.2)
        self.add_edge('2300 Parkway Blvd', '6351 South 900 East', 10.7)
        self.add_edge('233 Canyon Rd', '233 Canyon Rd', 0)
        self.add_edge('233 Canyon Rd', '2530 S 500 E', 4.8)
        self.add_edge('233 Canyon Rd', '2600 Taylorsville Blvd', 11.9)
        self.add_edge('233 Canyon Rd', '2835 Main St', 4.7)
        self.add_edge('233 Canyon Rd', '300 State St', 0.6)
        self.add_edge('233 Canyon Rd', '3060 Lester St', 7.6)
        self.add_edge('233 Canyon Rd', '3148 S 1100 W', 7.8)
        self.add_edge('233 Canyon Rd', '3365 S 900 W', 6.6)
        self.add_edge('233 Canyon Rd', '3575 W Valley Central Station bus Loop', 7.2)
        self.add_edge('233 Canyon Rd', '3595 Main St', 5.9)
        self.add_edge('233 Canyon Rd', '380 W 2880 S', 5.4)
        self.add_edge('233 Canyon Rd', '410 S State St', 1.0)
        self.add_edge('233 Canyon Rd', '4300 S 1300 E', 8.5)
        self.add_edge('233 Canyon Rd', '4580 S 2300 E', 10.3)
        self.add_edge('233 Canyon Rd', '5025 State St', 7.8)
        self.add_edge('233 Canyon Rd', '5100 South 2700 West', 11.5)
        self.add_edge('233 Canyon Rd', '5383 South 900 East #104', 9.5)
        self.add_edge('233 Canyon Rd', '600 E 900 South', 2.8)
        self.add_edge('233 Canyon Rd', '6351 South 900 East', 14.1)
        self.add_edge('2530 S 500 E', '2530 S 500 E', 0)
        self.add_edge('2530 S 500 E', '2600 Taylorsville Blvd', 9.4)
        self.add_edge('2530 S 500 E', '2835 Main St', 1.1)
        self.add_edge('2530 S 500 E', '300 State St', 5.1)
        self.add_edge('2530 S 500 E', '3060 Lester St', 4.6)
        self.add_edge('2530 S 500 E', '3148 S 1100 W', 3.7)
        self.add_edge('2530 S 500 E', '3365 S 900 W', 4.0)
        self.add_edge('2530 S 500 E', '3575 W Valley Central Station bus Loop', 6.7)
        self.add_edge('2530 S 500 E', '3595 Main St', 2.3)
        self.add_edge('2530 S 500 E', '380 W 2880 S', 1.8)
        self.add_edge('2530 S 500 E', '410 S State St', 4.1)
        self.add_edge('2530 S 500 E', '4300 S 1300 E', 3.8)
        self.add_edge('2530 S 500 E', '4580 S 2300 E', 5.8)
        self.add_edge('2530 S 500 E', '5025 State St', 4.3)
        self.add_edge('2530 S 500 E', '5100 South 2700 West', 7.8)
        self.add_edge('2530 S 500 E', '5383 South 900 East #104', 4.8)
        self.add_edge('2530 S 500 E', '600 E 900 South', 3.2)
        self.add_edge('2530 S 500 E', '6351 South 900 East', 6.0)
        self.add_edge('2600 Taylorsville Blvd', '2600 Taylorsville Blvd', 0)
        self.add_edge('2600 Taylorsville Blvd', '2835 Main St', 7.3)
        self.add_edge('2600 Taylorsville Blvd', '300 State St', 12.0)
        self.add_edge('2600 Taylorsville Blvd', '3060 Lester St', 4.9)
        self.add_edge('2600 Taylorsville Blvd', '3148 S 1100 W', 5.2)
        self.add_edge('2600 Taylorsville Blvd', '3365 S 900 W', 5.4)
        self.add_edge('2600 Taylorsville Blvd', '3575 W Valley Central Station bus Loop', 8.1)
        self.add_edge('2600 Taylorsville Blvd', '3595 Main St', 6.2)
        self.add_edge('2600 Taylorsville Blvd', '380 W 2880 S', 6.9)
        self.add_edge('2600 Taylorsville Blvd', '410 S State St', 11.5)
        self.add_edge('2600 Taylorsville Blvd', '4300 S 1300 E', 6.9)
        self.add_edge('2600 Taylorsville Blvd', '4580 S 2300 E', 8.3)
        self.add_edge('2600 Taylorsville Blvd', '5025 State St', 4.1)
        self.add_edge('2600 Taylorsville Blvd', '5100 South 2700 West', 0.4)
        self.add_edge('2600 Taylorsville Blvd', '5383 South 900 East #104', 4.9)
        self.add_edge('2600 Taylorsville Blvd', '600 E 900 South', 11.0)
        self.add_edge('2600 Taylorsville Blvd', '6351 South 900 East', 6.8)
        self.add_edge('2835 Main St', '2835 Main St', 0)
        self.add_edge('2835 Main St', '300 State St', 4.7)
        self.add_edge('2835 Main St', '3060 Lester St', 3.5)
        self.add_edge('2835 Main St', '3148 S 1100 W', 2.6)
        self.add_edge('2835 Main St', '3365 S 900 W', 2.9)
        self.add_edge('2835 Main St', '3575 W Valley Central Station bus Loop', 6.3)
        self.add_edge('2835 Main St', '3595 Main St', 1.2)
        self.add_edge('2835 Main St', '380 W 2880 S', 1.0)
        self.add_edge('2835 Main St', '410 S State St', 3.7)
        self.add_edge('2835 Main St', '4300 S 1300 E', 4.1)
        self.add_edge('2835 Main St', '4580 S 2300 E', 6.2)
        self.add_edge('2835 Main St', '5025 State St', 3.4)
        self.add_edge('2835 Main St', '5100 South 2700 West', 6.9)
        self.add_edge('2835 Main St', '5383 South 900 East #104', 5.2)
        self.add_edge('2835 Main St', '600 E 900 South', 3.7)
        self.add_edge('2835 Main St', '6351 South 900 East', 6.4)
        self.add_edge('300 State St', '300 State St', 0)
        self.add_edge('300 State St', '3060 Lester St', 7.3)
        self.add_edge('300 State St', '3148 S 1100 W', 7.8)
        self.add_edge('300 State St', '3365 S 900 W', 6.6)
        self.add_edge('300 State St', '3575 W Valley Central Station bus Loop', 7.2)
        self.add_edge('300 State St', '3595 Main St', 5.9)
        self.add_edge('300 State St', '380 W 2880 S', 5.4)
        self.add_edge('300 State St', '410 S State St', 1.0)
        self.add_edge('300 State St', '4300 S 1300 E', 8.5)
        self.add_edge('300 State St', '4580 S 2300 E', 10.3)
        self.add_edge('300 State St', '5025 State St', 7.8)
        self.add_edge('300 State St', '5100 South 2700 West', 11.5)
        self.add_edge('300 State St', '5383 South 900 East #104', 9.5)
        self.add_edge('300 State St', '600 E 900 South', 2.8)
        self.add_edge('300 State St', '6351 South 900 East', 14.1)
        self.add_edge('3060 Lester St', '3060 Lester St', 0)
        self.add_edge('3060 Lester St', '3148 S 1100 W', 1.3)
        self.add_edge('3060 Lester St', '3365 S 900 W', 1.5)
        self.add_edge('3060 Lester St', '3575 W Valley Central Station bus Loop', 4.0)
        self.add_edge('3060 Lester St', '3595 Main St', 3.2)
        self.add_edge('3060 Lester St', '380 W 2880 S', 3.0)
        self.add_edge('3060 Lester St', '410 S State St', 6.9)
        self.add_edge('3060 Lester St', '4300 S 1300 E', 6.2)
        self.add_edge('3060 Lester St', '4580 S 2300 E', 8.2)
        self.add_edge('3060 Lester St', '5025 State St', 5.5)
        self.add_edge('3060 Lester St', '5100 South 2700 West', 4.4)
        self.add_edge('3060 Lester St', '5383 South 900 East #104', 7.2)
        self.add_edge('3060 Lester St', '600 E 900 South', 6.4)
        self.add_edge('3060 Lester St', '6351 South 900 East', 10.5)
        self.add_edge('3148 S 1100 W', '3148 S 1100 W', 0)
        self.add_edge('3148 S 1100 W', '3365 S 900 W', 0.6)
        self.add_edge('3148 S 1100 W', '3575 W Valley Central Station bus Loop', 6.4)
        self.add_edge('3148 S 1100 W', '3595 Main St', 2.4)
        self.add_edge('3148 S 1100 W', '380 W 2880 S', 2.2)
        self.add_edge('3148 S 1100 W', '410 S State St', 6.8)
        self.add_edge('3148 S 1100 W', '4300 S 1300 E', 5.3)
        self.add_edge('3148 S 1100 W', '4580 S 2300 E', 7.4)
        self.add_edge('3148 S 1100 W', '5025 State St', 4.6)
        self.add_edge('3148 S 1100 W', '5100 South 2700 West', 4.8)
        self.add_edge('3148 S 1100 W', '5383 South 900 East #104', 6.3)
        self.add_edge('3148 S 1100 W', '600 E 900 South', 6.5)
        self.add_edge('3148 S 1100 W', '6351 South 900 East', 8.8)
        self.add_edge('3365 S 900 W', '3365 S 900 W', 0)
        self.add_edge('3365 S 900 W', '3575 W Valley Central Station bus Loop', 5.6)
        self.add_edge('3365 S 900 W', '3595 Main St', 1.6)
        self.add_edge('3365 S 900 W', '380 W 2880 S', 1.7)
        self.add_edge('3365 S 900 W', '410 S State St', 6.4)
        self.add_edge('3365 S 900 W', '4300 S 1300 E', 4.9)
        self.add_edge('3365 S 900 W', '4580 S 2300 E', 6.9)
        self.add_edge('3365 S 900 W', '5025 State St', 4.2)
        self.add_edge('3365 S 900 W', '5100 South 2700 West', 5.6)
        self.add_edge('3365 S 900 W', '5383 South 900 East #104', 5.9)
        self.add_edge('3365 S 900 W', '600 E 900 South', 5.7)
        self.add_edge('3365 S 900 W', '6351 South 900 East', 8.4)
        self.add_edge('3575 W Valley Central Station bus Loop', '3575 W Valley Central Station bus Loop', 0)
        self.add_edge('3575 W Valley Central Station bus Loop', '3595 Main St', 7.1)
        self.add_edge('3575 W Valley Central Station bus Loop', '380 W 2880 S', 6.1)
        self.add_edge('3575 W Valley Central Station bus Loop', '410 S State St', 7.2)
        self.add_edge('3575 W Valley Central Station bus Loop', '4300 S 1300 E', 10.6)
        self.add_edge('3575 W Valley Central Station bus Loop', '4580 S 2300 E', 12.0)
        self.add_edge('3575 W Valley Central Station bus Loop', '5025 State St', 9.4)
        self.add_edge('3575 W Valley Central Station bus Loop', '5100 South 2700 West', 7.5)
        self.add_edge('3575 W Valley Central Station bus Loop', '5383 South 900 East #104', 11.1)
        self.add_edge('3575 W Valley Central Station bus Loop', '600 E 900 South', 6.2)
        self.add_edge('3575 W Valley Central Station bus Loop', '6351 South 900 East', 13.6)
        self.add_edge('3595 Main St', '3595 Main St', 0)
        self.add_edge('3595 Main St', '380 W 2880 S', 1.6)
        self.add_edge('3595 Main St', '410 S State St', 4.9)
        self.add_edge('3595 Main St', '4300 S 1300 E', 3.0)
        self.add_edge('3595 Main St', '4580 S 2300 E', 5.0)
        self.add_edge('3595 Main St', '5025 State St', 2.3)
        self.add_edge('3595 Main St', '5100 South 2700 West', 5.5)
        self.add_edge('3595 Main St', '5383 South 900 East #104', 4.0)
        self.add_edge('3595 Main St', '600 E 900 South', 5.1)
        self.add_edge('3595 Main St', '6351 South 900 East', 5.2)
        self.add_edge('380 W 2880 S', '380 W 2880 S', 0)
        self.add_edge('380 W 2880 S', '410 S State St', 4.4)
        self.add_edge('380 W 2880 S', '4300 S 1300 E', 4.6)
        self.add_edge('380 W 2880 S', '4580 S 2300 E', 6.6)
        self.add_edge('380 W 2880 S', '5025 State St', 3.9)
        self.add_edge('380 W 2880 S', '5100 South 2700 West', 6.5)
        self.add_edge('380 W 2880 S', '5383 South 900 East #104', 5.6)
        self.add_edge('380 W 2880 S', '600 E 900 South', 4.3)
        self.add_edge('380 W 2880 S', '6351 South 900 East', 6.9)
        self.add_edge('410 S State St', '410 S State St', 0)
        self.add_edge('410 S State St', '4300 S 1300 E', 7.5)
        self.add_edge('410 S State St', '4580 S 2300 E', 9.3)
        self.add_edge('410 S State St', '5025 State St', 6.8)
        self.add_edge('410 S State St', '5100 South 2700 West', 11.4)
        self.add_edge('410 S State St', '5383 South 900 East #104', 8.5)
        self.add_edge('410 S State St', '600 E 900 South', 1.8)
        self.add_edge('410 S State St', '6351 South 900 East', 13.1)
        self.add_edge('4300 S 1300 E', '4300 S 1300 E', 0)
        self.add_edge('4300 S 1300 E', '4580 S 2300 E', 2.0)
        self.add_edge('4300 S 1300 E', '5025 State St', 2.9)
        self.add_edge('4300 S 1300 E', '5100 South 2700 West', 6.4)
        self.add_edge('4300 S 1300 E', '5383 South 900 East #104', 2.8)
        self.add_edge('4300 S 1300 E', '600 E 900 South', 6.0)
        self.add_edge('4300 S 1300 E', '6351 South 900 East', 4.1)
        self.add_edge('4580 S 2300 E', '4580 S 2300 E', 0)
        self.add_edge('4580 S 2300 E', '5025 State St', 4.4)
        self.add_edge('4580 S 2300 E', '5100 South 2700 West', 7.9)
        self.add_edge('4580 S 2300 E', '5383 South 900 East #104', 3.4)
        self.add_edge('4580 S 2300 E', '600 E 900 South', 7.9)
        self.add_edge('4580 S 2300 E', '6351 South 900 East', 4.7)
        self.add_edge('5025 State St', '5025 State St', 0)
        self.add_edge('5025 State St', '5100 South 2700 West', 4.5)
        self.add_edge('5025 State St', '5383 South 900 East #104', 1.7)
        self.add_edge('5025 State St', '600 E 900 South', 6.8)
        self.add_edge('5025 State St', '6351 South 900 East', 3.1)
        self.add_edge('5100 South 2700 West', '5100 South 2700 West', 0)
        self.add_edge('5100 South 2700 West', '5383 South 900 East #104', 5.4)
        self.add_edge('5100 South 2700 West', '600 E 900 South', 10.6)
        self.add_edge('5100 South 2700 West', '6351 South 900 East', 7.8)
        self.add_edge('5383 South 900 East #104', '5383 South 900 East #104', 0)
        self.add_edge('5383 South 900 East #104', '600 E 900 South', 7.0)
        self.add_edge('5383 South 900 East #104', '6351 South 900 East', 1.3)
        self.add_edge('600 E 900 South', '600 E 900 South', 0)
        self.add_edge('600 E 900 South', '6351 South 900 East', 8.3)
        self.add_edge('6351 South 900 East', '6351 South 900 East', 0)


