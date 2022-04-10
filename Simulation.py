from datetime import datetime
from datetime import date
from datetime import time
import Graph
import Packages
import Truck

package_hash = Packages.create_package_hash('WGUPS Package File.csv')
distance_graph = Graph.create_distance_graph('WGUPS Distance Table.csv')

truck_one = Truck.Truck()

truck_two = Truck.Truck()
truck_two.time = datetime.combine(date.today(), time.fromisoformat('09:05:00'))

truck_one_iteration_two = Truck.Truck()

for i in range(len(package_hash)):
    for j in range(len(package_hash[i])):
        if package_hash[i][j][1].truck == 'truck_one':
            truck_one.add_package(package_hash[i][j][1])
        elif package_hash[i][j][1].truck == 'truck_two':
            truck_two.add_package(package_hash[i][j][1])
        else:
            truck_one_iteration_two.add_package(package_hash[i][j][1])

# O(n^2) for time complexity, O(1) for space
def nearest_neighbor_traversal(truck_object, time_string):

    if truck_object.time >= datetime.combine(date.today(), time.fromisoformat(time_string)):
        return 0

    for package in truck_object:
        package.status = 'En Route'

    start_point = 'HUB'
    traveled_distance = 0.0
    min_distance = -1.0
    min_vertex = None
    current_package = None

    while len(truck_object.packages) > 0:
        for package in truck_object:
            distance = distance_graph.check_distance(start_point, package.address)
            if distance < min_distance or min_distance == -1.0:
                min_distance = distance
                min_vertex = package.address
                current_package = package

        truck_object.add_time(min_distance)

        if truck_object.time > datetime.combine(date.today(), time.fromisoformat(time_string)):
            return traveled_distance

        truck_object.remove_package(current_package)
        current_package.status = 'Delivered'

        start_point = min_vertex
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