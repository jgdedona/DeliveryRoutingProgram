import csv

class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_undirected_edge(self, vertex_a, vertex_b, weight):
        self.edge_weights[(vertex_a, vertex_b)] = weight
        self.edge_weights[(vertex_b, vertex_a)] = weight
        self.adjacency_list[vertex_a].append(vertex_b)
        self.adjacency_list[vertex_b].append(vertex_a)

    # O(n) for time, O(1) for space
    def check_distance(self, vertex_a, vertex_b):
        key_check_tuple = (vertex_a, vertex_b)
        if key_check_tuple in self.edge_weights:
            return self.edge_weights[key_check_tuple]
        print("Invalid vertices")


# O(n^2) for time and space
def create_distance_graph(csv_file):
    distance_graph = Graph()

    with open(csv_file) as file:
        distance_info = csv.reader(file, delimiter=',')

        row_num = 0
        row_0 = []
        for row in distance_info:
            if row_num == 0:
                for i in range(27):
                    row_0.append(row[i+2].strip())

            if row_num > 0:
                distance_graph.add_vertex(row[1].strip())

                for i in range(row_num):
                    distance_graph.add_undirected_edge(row[1].strip(), row_0[i], float(row[i+2]))
            row_num += 1

    return distance_graph


# O(n^2) for time complexity, O(1) for space
def nearest_neighbor_traversal(distance_graph, truck_object):
    start_point = 'HUB'
    traveled_distance = 0.0
    min_distance = -1.0
    min_vertex = None
    vertex_list = [package.address for package in truck_object]

    while len(vertex_list) > 1:
        for vertex in vertex_list:
            distance = distance_graph.check_distance(start_point, vertex)
            if distance < min_distance or min_distance == -1.0:
                min_distance = distance
                min_vertex = vertex

        start_point = min_vertex
        vertex_list.remove(min_vertex)
        traveled_distance += min_distance
        min_distance = -1.0

    traveled_distance += distance_graph.check_distance(start_point, 'HUB')
    truck_object.miles = traveled_distance

    return traveled_distance


    # Start at hub
    # Iterate through list to find nearest vertex
    # travel to nearest vertex
    # set current location to new vertex
    # remove package containing vertex from list
    # repeat steps two through five until list empty
    # return to hub