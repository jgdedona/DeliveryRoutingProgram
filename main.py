import simulation
import truck
from datetime import datetime
from datetime import date
from datetime import time


if __name__ == '__main__':

    menu = '1: View status for all packages\n2: View status for a specified package\n' + \
           '3: View combined mileage of all trucks\n4: Exit'
    print(menu)
    menu_selection = input("Please select a menu item: ")

    while menu_selection not in ['1', '2', '3', '4']:
        menu_selection = input('Invalid selection. Please try again: ')

    while menu_selection != '4':  # Continues to re-run the program until option 4 (exit) is selected

        # O(n) for time and space
        package_hash = simulation.create_hash_table()

        truck_one = truck.Truck()
        truck_two = truck.Truck()
        truck_two.time = datetime.combine(date.today(), time.fromisoformat('09:05:00'))  # Ensures truck_two does not
        # depart until 09:05
        truck_one_iteration_two = truck.Truck()

        # O(n) for time, O(1) for space
        simulation.fill_truck_objects(package_hash, truck_one, truck_two, truck_one_iteration_two)

        time_string = input("Please enter a time in the following 24 hour format: HH:MM:SS \n")

        # O(n^2) for time, O(1) for space for every call of Simulation.nearest_neighbor_traversal in the try block
        try:
            truck_one_delivery = simulation.nearest_neighbor_traversal(truck_one, time_string)
            truck_two_delivery = simulation.nearest_neighbor_traversal(truck_two, time_string)
            truck_one_iteration_two.time = truck_one.time # Ensures truck_one_iteration_two does not depart until
            # truck_one returns
            truck_one_it_two_delivery = simulation.nearest_neighbor_traversal(truck_one_iteration_two, time_string)
        except ValueError:
            print("Invalid time entry")
            continue

        # O(n) for time, O(1) for space, prints all package info from package_hash
        if menu_selection == '1':
            for package_list in package_hash:
                for package in package_list:
                    print(package[1])
        # O(n) for time, O(1) for space, prints package info for specified package
        elif menu_selection == '2':
            key = input("Please enter a package ID to search for: ")
            valid = False
            while valid == False:
                try:
                    print(package_hash.search(int(key)))
                    valid = True
                except ValueError:
                    key = input("Invalid ID. Please try again: ")
        # O(1) for time and space, adds mileage for each truck and displays the sum
        elif menu_selection == '3':
            total = truck_one_delivery + truck_two_delivery + truck_one_it_two_delivery
            print(round(total, 2))

        print('\n' + menu)
        menu_selection = input("Please select a menu item: ")

    exit()

