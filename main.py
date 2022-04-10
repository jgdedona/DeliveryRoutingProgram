import Simulation


if __name__ == '__main__':

    # Implement while loop to keep going until exit is selected
    menu = '1: View status for all packages\n2: View status for a specified package\n' + \
           '3: View combined mileage of all trucks\n4: Exit'
    print(menu)
    menu_selection = input("Please select a menu item: ")

    while menu_selection not in ['1', '2', '3', '4']:
        menu_selection = input('Invalid selection. Please try again: ')

    while menu_selection != '4':

        time_string = input("Please enter a time in the following 24 hour format: HH:MM:SS \n")

        truck_one_delivery = Simulation.nearest_neighbor_traversal(Simulation.truck_one, time_string)

        truck_two_delivery = Simulation.nearest_neighbor_traversal(Simulation.truck_two, time_string)

        Simulation.truck_one_iteration_two.time = Simulation.truck_one.time
        truck_one_it_two_delivery = Simulation.nearest_neighbor_traversal(Simulation.truck_one_iteration_two, time_string)

        if menu_selection == '1':
            for package_list in Simulation.package_hash:
                for package in package_list:
                    print(package[1])
        elif menu_selection == '2':
            key = input("Please enter a package ID to search for: ")
            valid = False
            while valid == False:
                try:
                    print(Simulation.package_hash.search(int(key)))
                    valid = True
                except ValueError:
                    key = input("Invalid ID. Please try again: ")
        elif menu_selection == '3':
            sum = truck_one_delivery + truck_two_delivery + truck_one_it_two_delivery
            print(sum)

        print('\n' + menu)
        menu_selection = input("Please select a menu item: ")

    exit()

