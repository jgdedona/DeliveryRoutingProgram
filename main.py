import Simulation


if __name__ == '__main__':

    time_string = input("Please enter a time in the following 24 hour format: HH:MM:SS \n")


    truck_one_delivery = Simulation.nearest_neighbor_traversal(Simulation.truck_one, time_string)
    Simulation.truck_one_iteration_two.time = Simulation.truck_one.time
    print(Simulation.truck_one_iteration_two.time)

    truck_two_deliver = Simulation.nearest_neighbor_traversal(Simulation.truck_two, time_string)

    truck_one_it_two_delivery = Simulation.nearest_neighbor_traversal(Simulation.truck_one_iteration_two, time_string)
