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


def create_distance_graph(csv_file):
    distance_graph = Graph()

    with open(csv_file) as file:
        distance_info = csv.reader(file, delimiter=',')

        row_num = 0
        row_0 = []
        for row in distance_info:
            if row_num == 0:
                for i in range(27):
                    row_0.append(row[i+2])

            if row_num > 0:
                distance_graph.add_vertex(row[1])

                for i in range(row_num-1):
                    distance_graph.add_undirected_edge(row[1], row_0[i], row[i+2])
            row_num += 1

    return distance_graph