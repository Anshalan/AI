import datetime
import math
import random


class City_node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.connected_nodes = []
        self.path = []
        self.total_estimation = 0
        self.cost = 0


def calculate_distance(node1: City_node, node2: City_node):
    return math.sqrt(pow(node1.x - node2.x, 2) + pow(node1.y - node2.y, 2))


def generate_graph(n: int):
    graph = []
    for i in range(0, n):
        graph.append(City_node("City_" + str(i + 1), random.randrange(0, 5), random.randrange(0, 5)))
    return graph


def print_list(c_list: list):
    for city in c_list:
        print(city.name)
        for nb in city.connected_nodes:
            print("\t" + nb.name + " " + str(calculate_distance(city, nb)))


def bfs(root, graph):
    root_cpy = City_node(root.name, root.x, root.y)
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)
        current_node.path.append(current_node.name)
        if len(current_node.path) == len(graph):
            current_node.path.append(root.name)
            current_node.cost += calculate_distance(current_node, root)
        if len(current_node.path) == len(graph) + 1:
            if best_cost < 0 or current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            for child in graph:
                if child.name not in current_node.path:
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    nodes_to_visit.append(new_node)
    # print("################")
    # print("BFS ")
    # print(best_cost)
    # print(best_path)
    return [best_path, best_cost]


def dfs(root, graph):
    root_cpy = City_node(root.name, root.x, root.y)
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)  # 0
        current_node.path.append(current_node.name)
        if len(current_node.path) == len(graph):
            current_node.path.append(root.name)
            current_node.cost += calculate_distance(current_node, root)
        if len(current_node.path) == len(graph) + 1:
            if best_cost < 0 or current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            temp_nodes_to_visit = []
            for child in graph:
                if child.name not in current_node.path:
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    temp_nodes_to_visit.append(new_node)
            nodes_to_visit = temp_nodes_to_visit + nodes_to_visit
    # print("################")
    # print("DFS")
    # print(best_cost)
    # print(best_path)
    return [best_path, best_cost]


def greedy(root, graph):
    root_cpy = City_node(root.name, root.x, root.y)
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)  # 0
        current_node.path.append(current_node.name)
        if len(current_node.path) == len(graph):
            current_node.path.append(root.name)
            current_node.cost += calculate_distance(current_node, root)
        if len(current_node.path) == len(graph) + 1:

            if best_cost < 0 or current_node.cost < best_cost:
                best_cost = current_node.cost
                best_path = current_node.path
        else:
            temp_nodes_to_visit = []
            for child in graph:
                if child.name not in current_node.path:
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    temp_nodes_to_visit.append(new_node)
            newlist = sorted(temp_nodes_to_visit, key=lambda x: x.cost, reverse=False)
            nodes_to_visit.append(newlist[0])
    # print("################")
    # print("GREEDY")
    # print(best_cost)
    # print(best_path)
    return [best_path, best_cost]


def a_star(root, graph):
    root_cpy = City_node(root.name, root.x, root.y)
    nodes_to_visit = [root_cpy]
    best_path = []
    best_cost = -1
    while len(nodes_to_visit) > 0:
        nodes_to_visit.sort(key=lambda x: x.total_estimation)
        current_node = nodes_to_visit.pop(0)  # 0
        current_node.path.append(current_node.name)
        if len(current_node.path) >= len(graph):
            if len(current_node.path) == len(graph) + 1:
                best_cost = current_node.cost
                best_path = current_node.path
                break
            new_node = City_node(root.name, root.x, root.y)
            new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
            new_node.path = list(current_node.path)
            new_node.total_estimation = new_node.cost + calculate_distance(new_node, root)
            nodes_to_visit.append(new_node)
        else:
            temp_nodes_to_visit = []
            for child in graph:
                if (child.name not in current_node.path):
                    new_node = City_node(child.name, child.x, child.y)
                    new_node.cost = current_node.cost + calculate_distance(current_node, new_node)
                    new_node.path = list(current_node.path)
                    new_node.total_estimation = new_node.cost + calculate_distance(new_node, root)
                    temp_nodes_to_visit.append(new_node)
            nodes_to_visit = temp_nodes_to_visit + nodes_to_visit
    # print("################")
    # print("A_STAR ")
    # print(best_cost)
    # print(best_path)
    return [best_path, best_cost]


for i in range(1, 11):
    graph = generate_graph(i)

    start_time = datetime.datetime.now()
    bfs_res = bfs(graph[0], graph)
    end_time = datetime.datetime.now()
    bfs_execution_time = (end_time - start_time).total_seconds() * 1000

    start_time = datetime.datetime.now()
    dfs_res = dfs(graph[0], graph)
    end_time = datetime.datetime.now()
    dfs_execution_time = (end_time - start_time).total_seconds() * 1000

    start_time = datetime.datetime.now()
    greedy_res = greedy(graph[0], graph)
    end_time = datetime.datetime.now()
    z_execution_time = (end_time - start_time).total_seconds() * 1000

    start_time = datetime.datetime.now()
    a_star_res = a_star(graph[0], graph)
    end_time = datetime.datetime.now()
    a_execution_time = (end_time - start_time).total_seconds() * 1000

    print("for " + str(i) + " nodes:"
          + "\n\tbfs time:    {0}ms".format(round(bfs_execution_time, 1)) + "\tcost:{0} path: {1}".format(round(bfs_res[1], 3), bfs_res[0])
          + "\n\tdfs time:    {0}ms".format(round(dfs_execution_time, 1))+ "\tcost:{0} path: {1}".format(round(dfs_res[1], 3), dfs_res[0])
          + "\n\tgreedy time: {0}ms".format(round(z_execution_time, 1))+ "\tcost:{0} path: {1}".format(round(greedy_res[1], 3), greedy_res[0])
          + "\n\ta* time:     {0}ms".format(round(a_execution_time, 1))+ "\tcost:{0} path: {1}".format(round(a_star_res[1], 3), a_star_res[0]))


