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
        graph.append(City_node("City_" + str(i + 1), random.randrange(0, 10), random.randrange(0, 10)))
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
    # nodes_to_visit = [root]
    root_cpy = City_node(root.name,root.x,root.y)
    root_cpy.connected_nodes = root.connected_nodes
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)  # 0
        # print(current_node.name)
        current_node.path.append(current_node.name)
        if len(current_node.path) == len(root.connected_nodes) + 1:
            # print("path cost " + str(current_node.cost))
            if best_cost < 0 or current_node.cost < best_cost:
                # if current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            for child in current_node.connected_nodes:
                if (child.name not in current_node.path):
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    new_node.connected_nodes = list(child.connected_nodes)
                    nodes_to_visit.append(new_node)
    print("################")
    print("BFS")
    print(best_cost)
    print(best_path)
    # return best_path


def dfs(root):
    # nodes_to_visit = [root]
    root_cpy = City_node(root.name, root.x, root.y)
    root_cpy.connected_nodes = root.connected_nodes
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)  # 0
        # print(current_node.name)

        current_node.path.append(current_node.name)
        if len(current_node.path) == len(root.connected_nodes) + 1:
            # print("path cost " + str(current_node.cost))
            if best_cost < 0 or current_node.cost < best_cost:
                # if current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            temp_nodes_to_visit = []
            for child in current_node.connected_nodes:
                if (child.name not in current_node.path):
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    new_node.connected_nodes = list(child.connected_nodes)

                    temp_nodes_to_visit.append(new_node)
                    # nodes_to_visit.append(new_node)
            nodes_to_visit = temp_nodes_to_visit + nodes_to_visit
    print("################")
    print("DFS")
    print(best_cost)
    print(best_path)
def zachlanny(root):
    # nodes_to_visit = [root]
    root_cpy = City_node(root.name, root.x, root.y)
    root_cpy.connected_nodes = root.connected_nodes
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)  # 0
        # print(current_node.name)

        current_node.path.append(current_node.name)
        if len(current_node.path) == len(root.connected_nodes) + 1:
            # print("path cost " + str(current_node.cost))
            if best_cost < 0 or current_node.cost < best_cost:
                # if current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            temp_nodes_to_visit = []
            for child in current_node.connected_nodes:
                if (child.name not in current_node.path):
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    new_node.connected_nodes = list(child.connected_nodes)

                    temp_nodes_to_visit.append(new_node)
                    # nodes_to_visit.append(new_node)
                    # print(new_node.name + "cost is " + str(new_node.cost))
            newlist = sorted(temp_nodes_to_visit, key=lambda x: x.cost, reverse=False)
            # print_list(newlist)
            nodes_to_visit.append(newlist[0])


    print("################")
    print("GREEDY")
    print(best_cost)
    print(best_path)
    # return best_path


new_graph = generate_graph(12)
new_graph2 = new_graph
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
# print_list(new_graph)
dfs(new_graph[0])
zachlanny(new_graph[0])
