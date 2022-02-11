import math
import random


class City_node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connected_nodes = []
        self.path = []
        self.cost = 0


def calculate_distance(node1: City_node, node2: City_node):
    return math.sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))

#
# def get_node_index(node: City_node, cities: list):
#     for idx, city in enumerate(cities):
#         if city.name == node.name:
#             return idx


def generate_graph(n: int):
    graph = []
    for i in range(0, n):
        graph.append(City_node("City_" + str(i + 1), random.randrange(0, 5), random.randrange(0, 5)))
        # graph.append(City_node("City_"+ str(i+1), i,2*i))
    for city in graph:
        for node in graph:
            if city is not node:
                city.connected_nodes.append(node)
    return graph


def print_list(c_list: list):
    for city in c_list:
        print(city.name)
        # print(city.cost)
        for nb in city.connected_nodes:
            print("\t" + nb.name + " " + str(calculate_distance(city, nb)))


#
def bfs(root):
    nodes_to_visit = [root]
    best_path = []
    best_cost = math.inf
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)  # 0
        current_node.path.append(current_node.name)
        if len(current_node.path) == len(root.connected_nodes)+1:
            if current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            for child in current_node.connected_nodes:
                if (child.name not in current_node.path):
                    temp = City_node(child.name, child.x, child.y)
                    temp.cost = current_node.cost + calculate_distance(current_node, temp)
                    temp.path = list(current_node.path)
                    temp.connected_nodes = list(child.connected_nodes)
                    nodes_to_visit.append(temp)
    print("################")
    print(best_cost)
    print(best_path)
    # return best_path


def dfs(root: City_node, cities: list):
    cities2 = cities.copy()  # pass copy
    best_path = []
    best_distance = math.inf
    ########################
    # if root.connected_nodes == 0:
    #     root.paths.append(root.path)
    #     return root
    # else:
    #     current_cost = math.inf
    #     current_path = []
    #     for node in root.connected_nodes:
    #         if node.name in root.path:
    #             continue
    #         # root.path.append(node.name)
    #         # root.cost += calculate_distance(root, node)
    #         ret = dfs(City_node(node.name, node.x, node.y, node.path.append(node.name), node.cost + calculate_distance(root,node)))
    #         root.paths.append(ret.paths)
    #         # if ret.cost < current_cost:
    #         #     current_cost = ret.cost
    #         #     current_path = ret.path

    ########################
    while len(cities2) > 0:
        # print ("cities2 len = " + str(len(cities2)))
        current_city = cities2.pop(0)
        print(current_city.name)
        if current_city.name == root.name:
            print("skipping " + current_city.name)
            continue
        current_path = [root.name, current_city.name]
        current_distance = 0
        for neighbour in current_city.connected_nodes:
            if neighbour.name not in current_path:
                current_path.append(neighbour.name)
                print(current_path)
                current_distance += calculate_distance(current_city, neighbour)
            if neighbour == current_city.connected_nodes[-1]:
                current_path.append(root.name)
                current_distance += calculate_distance(neighbour, root)
        print(current_distance)

        if current_distance < best_distance:
            best_distance = current_distance
            best_path = current_path
    print(best_distance)
    return best_path

new_graph = generate_graph(10)
g2 = [
    City_node("City_1", 0, 0),
    City_node("City_2", 1, 0),
    City_node("City_3", 0, 2)
]
for city in g2:
    for node in g2:
        if city is not node:
            city.connected_nodes.append(node)

print_list(new_graph)
bfs(new_graph[0])