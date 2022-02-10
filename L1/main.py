import math


class City_node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


def calculate_distance(node1: City_node, node2: City_node):
    return math.sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))

def create_all_paths(cities: list):
    while(cities):
        # print_list(cities)
        cities.pop(0)
        print_list(cities)
        print("\n")

def get_node_index(node: City_node, cities: list):
    for idx, city in enumerate(cities):
        if city.name == node.name:
            return idx

# def create_graph (root: City_node, cities: list):



def print_list(c_list: list):
    for city in c_list:
        print(city.name)

cities_list = [
    City_node('A', 1, 5),
    City_node('B', 5, 7),
    City_node('C', 2, 11),
    City_node('D', 5, 6),
    City_node('E', 41, 32),
    City_node('F', 21, 2),
    City_node('G', 15, 1),
    City_node('H', 31, 12),
    City_node('I', 4, 9)
]

index = get_node_index(cities_list[2], cities_list)
print(index)
cities_list.pop(index)
print_list(cities_list)

# print_list(cities_list)
# create_all_paths(cities_list)
# dist = calculate_distance(cities_list[0], cities_list[3])
# print(dist)