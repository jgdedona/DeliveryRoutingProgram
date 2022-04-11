from datetime import datetime
from datetime import date
from datetime import time
import Graph
import Packages

# O(n^2) for time and space
distance_graph = Graph.create_distance_graph('WGUPS Distance Table.csv')

# O(n) for time and space
def create_hash_table():
    return Packages.create_package_hash('WGUPS Package File.csv')

# O(n) for time, O(1) for space, creates references to package object existing in package_hash rather than copying the objects
def fill_truck_objects(package_hash, truck_one, truck_two, truck_one_iteration_two):
    """
    create_distance_graph:
    This function requires an existing hash table and three existing truck objects. It utilizes the package_hash
    to fill the truck objects' package lists.

    Args:
    package_hash: Hash table containing package objects.
    truck_one: First truck object.
    truck_two: Second truck object.
    truck_one_iteration_two: Third truck object.

    Returns:
    Nothing is returned because all parameters are passed as references, so they are modified in place.

    Time complexity: Because the function iterates through every entry in the hash table once,
    the time complexity is O(n)

    Space complexity: Because the function creates references to package objects existing in package_hash
    rather than copying the objects, the space complexity is O(1).
    """
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
    """
    nearest_neighbor_traversal:
    This function utilizes a truck object and time string to determine a delivery route
    using the nearest neighbor algorithm.

    Args:
    truck_object: The function utilizes the truck object's package list to determine delivery address
    and perform distance lookups. Package items are also updated and removed within the function.

    Returns:
    traveled_distance: The total distance traveled by the truck, computed based on the truck object's
    package list and the respective distance calculations. The traveled_distance int is also constrained
    by the time_string parameter.
    time_string: A time string provided in a 24 hour HH:MM:SS format. It is utilized to determine how
    many delivers can take place in the alloted time based on distance and speed calculations for each
    package.

    Time complexity:

    Space complexity:
    """

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