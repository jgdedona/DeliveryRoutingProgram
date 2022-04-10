import Simulation
import Truck
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

    while menu_selection != '4':

        package_hash = Simulation.create_hash_table()

        truck_one = Truck.Truck()
        truck_two = Truck.Truck()
        truck_two.time = datetime.combine(date.today(), time.fromisoformat('09:05:00'))
        truck_one_iteration_two = Truck.Truck()

        Simulation.fill_truck_objects(package_hash, truck_one, truck_two, truck_one_iteration_two)

        time_string = input("Please enter a time in the following 24 hour format: HH:MM:SS \n")

        try:
            truck_one_delivery = Simulation.nearest_neighbor_traversal(truck_one, time_string)
            truck_two_delivery = Simulation.nearest_neighbor_traversal(truck_two, time_string)
            truck_one_iteration_two.time = truck_one.time
            truck_one_it_two_delivery = Simulation.nearest_neighbor_traversal(truck_one_iteration_two, time_string)
        except ValueError:
            print("Invalid time entry")
            continue

        if menu_selection == '1':
            for package_list in package_hash:
                for package in package_list:
                    print(package[1])
        elif menu_selection == '2':
            key = input("Please enter a package ID to search for: ")
            valid = False
            while valid == False:
                try:
                    print(package_hash.search(int(key)))
                    valid = True
                except ValueError:
                    key = input("Invalid ID. Please try again: ")
        elif menu_selection == '3':
            sum = truck_one_delivery + truck_two_delivery + truck_one_it_two_delivery
            print(round(sum, 2))

        print('\n' + menu)
        menu_selection = input("Please select a menu item: ")

    exit()

