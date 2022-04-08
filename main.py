import Graph
import Packages

if __name__ == '__main__':
    package_hash = Packages.create_package_hash('WGUPS Package File.csv')
    distance_graph = Graph.create_distance_graph('WGUPS Distance Table Edited.csv')
