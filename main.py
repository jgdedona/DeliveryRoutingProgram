import Graph
import Packages
import Truck

if __name__ == '__main__':
    package_hash = Packages.create_package_hash('WGUPS Package File.csv')
    distance_graph = Graph.create_distance_graph('WGUPS Distance Table Edited.csv')

    truck_one = Truck.Truck()
    truck_two = Truck.Truck()
    truck_one_iteration_two = Truck.Truck()

    for i in range(len(package_hash)):
        for j in range (len(package_hash[i])):
            if package_hash[i][j][1].truck == 'truck_one':
                truck_one.add_package(package_hash[i][j][1])
            elif package_hash[i][j][1].truck == 'truck_two':
                truck_two.add_package(package_hash[i][j][1])
            else:
                truck_one_iteration_two.add_package(package_hash[i][j][1])