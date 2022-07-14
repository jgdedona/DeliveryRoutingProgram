import csv


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    # O(n) for time, O(1) for space
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    # O(n) for time, O(1) for space
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
    """
    create_distance_graph:
    This function utilizes a pre-formatted csv file to create a graph data structure and populate
    it with address and distance data.

    Args:
    csv_file: This is a string argument that denotes the location of a pre-formatted csv file containing address
    and distance data.

    Returns:
    distance_graph: This function returns a Graph object.

    Time complexity: Because functionFoo has nested for loops that operate on each input exactly twice,
    it's time complexity is O(n^2).

    Space complexity: Because each entry is stored in the data structure twice due to the nature
    of undirected edges, the space complexity is O(n^2).
    """
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
