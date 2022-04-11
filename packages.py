import csv
import hash

class Package:
    def __init__(self, packageId, address, city, state, zip, deliveryDeadline, massKilo, notes, status, truck):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.massKilo = massKilo
        self.notes = notes
        self.status = status
        self.truck = truck

    def __str__(self):
        return str(self.packageId + ', ' + self.address + ', ' + self.city + ', ' + self.state + ', '
                   + self.zip + ', ' + self.deliveryDeadline + ', ' + self.massKilo + ', ' + self.notes
                   + ', ' + self.status + ', ' + self.truck)


# O(n) for time and space
def create_package_hash(csv_file):
    """
    create_package_hash:
    This function utilizes a pre-formatted csv file to create a hash table data structure and populate
    it with package data.

    Args:
    csv_file: This is a string argument that denotes the location of a pre-formatted csv file containing
    package data.

    Returns:
    package_hash: This function returns a HashMap object.

    Time complexity: Because the function iterates over each row exactly once, the time complexity is O(n).

    Space complexity: Because each entry is stored in the data structure once,
    the space complexity is O(n^2).
    """
    package_hash = hash.HashMap()

    with open(csv_file) as file:
        packageInfo = csv.reader(file, delimiter=',')

        for row in packageInfo:
            if len(row[7]) == 0:
                notes = 'None'
            else:
                notes = row[7]
            package_hash.insert(int(row[0]), Package(row[0], row[1], row[2], row[3], row[4],
                                                        row[5], row[6], notes, 'Hub', row[8]))
    return package_hash
